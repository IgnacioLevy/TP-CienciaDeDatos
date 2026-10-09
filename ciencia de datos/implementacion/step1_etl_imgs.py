# -*- coding: utf-8 -*-
import os, warnings
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score, davies_bouldin_score
from sklearn.compose import ColumnTransformer

warnings.filterwarnings('ignore')

BASE      = r'E:\cosas\facu\Ciencia de Datos\ciencia de datos-20261008T230846Z-1-001\ciencia de datos'
DATA_PATH = os.path.join(BASE, 'recursos', 'secondary_data.csv')
OUT_DIR   = os.path.join(BASE, 'implementacion', 'entrega2')
os.makedirs(OUT_DIR, exist_ok=True)

PALETTE = ['#6C63FF','#FF6584','#43D9AD','#FFB347','#5EB8FF','#FF6F61']
plt.rcParams.update({'font.family':'DejaVu Sans','axes.facecolor':'#1a1a2e',
    'figure.facecolor':'#0f0f1a','axes.edgecolor':'#444466','axes.labelcolor':'#e0e0ff',
    'xtick.color':'#a0a0cc','ytick.color':'#a0a0cc','text.color':'#e0e0ff',
    'grid.color':'#2a2a4a','grid.linewidth':0.5})

print('Cargando dataset...', flush=True)
df_raw = pd.read_csv(DATA_PATH, sep=';')
n_orig_rows, n_orig_cols = df_raw.shape
null_pct_orig = df_raw.isnull().sum() / len(df_raw) * 100
target = df_raw['class'].copy()
df = df_raw.drop(columns=['class']).copy()
n_dup = df.duplicated().sum()
df = df.drop_duplicates()
null_pct = df.isnull().sum() / len(df) * 100
drop_cols = null_pct[null_pct > 70].index.tolist()
print(f'drop_cols={drop_cols}', flush=True)
df = df.drop(columns=drop_cols)
num_cols = df.select_dtypes(include=['float64','int64']).columns.tolist()
cat_cols = df.select_dtypes(include='object').columns.tolist()
for col in num_cols: df[col] = df[col].fillna(df[col].median())
for col in cat_cols: df[col] = df[col].fillna(df[col].mode()[0])

COLS_MORFO = ['cap-diameter','cap-shape','cap-surface','cap-color',
    'stem-height','stem-width','stem-color','stem-surface',
    'gill-color','gill-attachment','gill-spacing','has-ring','ring-type']
df_model = df[COLS_MORFO].copy()
n_final_rows, n_final_cols = df_model.shape
print(f'{n_final_rows} x {n_final_cols}', flush=True)

num_c = df_model.select_dtypes(include=['float64','int64']).columns.tolist()
cat_c = df_model.select_dtypes(include='object').columns.tolist()
preprocessor = ColumnTransformer(transformers=[
    ('num', StandardScaler(), num_c),
    ('cat', OneHotEncoder(handle_unknown='ignore', sparse_output=False), cat_c)])
X = preprocessor.fit_transform(df_model)
pca = PCA(n_components=2, random_state=42)
X_pca = pca.fit_transform(X)
var_exp = pca.explained_variance_ratio_ * 100

print('KMeans...', flush=True)
results = {}
for k in [5,6]:
    km = KMeans(n_clusters=k, random_state=42, n_init=15, max_iter=500)
    labels = km.fit_predict(X)
    sil = silhouette_score(X_pca, labels, sample_size=10_000, random_state=42)
    db  = davies_bouldin_score(X_pca, labels)
    sizes = pd.Series(labels).value_counts().sort_index()
    pct   = (sizes / len(labels) * 100).round(1)
    results[k] = {'labels':labels,'sil':sil,'db':db,'sizes':sizes,'pct':pct}
    print(f'K={k} sil={sil:.4f} db={db:.4f}', flush=True)

CLUSTER_NAMES = {0:'Anillados convexos marrones',1:'Grandes de poros',
    2:'Pegajosos sin anillo',3:'Pequenos sin anillo',
    4:'Esfericos amarillos raros',5:'Grandes blancos'}
df_model['cluster'] = results[6]['labels']
df_model['cluster_nombre'] = df_model['cluster'].map(CLUSTER_NAMES)

csv_path = os.path.join(OUT_DIR, 'dataset_clustering.csv')
df_model.to_csv(csv_path, index=False, encoding='utf-8')
print(f'CSV: {csv_path}', flush=True)

# IMAGENES
def savefig(path):
    plt.tight_layout()
    plt.savefig(path, dpi=150, bbox_inches='tight', facecolor=plt.gcf().get_facecolor())
    plt.close()

# nulos
fig,ax = plt.subplots(figsize=(12,4))
cs = null_pct_orig.drop('class').sort_values(ascending=False)
cb = ['#FF6584' if p>70 else '#6C63FF' for p in cs]
cs.plot(kind='bar',ax=ax,color=cb,edgecolor='#0f0f1a')
ax.axhline(70,color='#FFB347',linestyle='--',linewidth=1.8,label='Umbral 70%')
ax.set_title('Porcentaje de Valores Nulos por Columna',fontsize=13,fontweight='bold',color='#e0e0ff')
ax.set_xlabel('Columna'); ax.set_ylabel('% Nulos')
ax.legend(facecolor='#1a1a2e',edgecolor='#444466'); ax.set_facecolor('#1a1a2e')
plt.xticks(rotation=45,ha='right',fontsize=8)
img_nulos = os.path.join(OUT_DIR,'img_nulos.png')
savefig(img_nulos)

# scatter k6
fig,ax = plt.subplots(figsize=(10,7))
patches=[]
for cid in range(6):
    mask=results[6]['labels']==cid
    ax.scatter(X_pca[mask,0],X_pca[mask,1],c=PALETTE[cid],s=2.5,alpha=0.4,linewidths=0,rasterized=True)
    pct_c=results[6]['pct'][cid]
    patches.append(mpatches.Patch(color=PALETTE[cid],label=f'C{cid}: {CLUSTER_NAMES[cid]} ({pct_c:.0f}%)'))
ax.legend(handles=patches,fontsize=9,loc='upper right',facecolor='#1a1a2e',edgecolor='#6C63FF',framealpha=0.95)
ax.set_title(f'Clustering K=6 -- PCA 2D | Sil={results[6]["sil"]:.4f} DB={results[6]["db"]:.4f}',fontsize=12,color='#6C63FF')
ax.set_xlabel(f'PC1 ({var_exp[0]:.1f}%)'); ax.set_ylabel(f'PC2 ({var_exp[1]:.1f}%)')
ax.grid(True,linestyle='--',alpha=0.3); ax.set_facecolor('#1a1a2e')
img_scatter = os.path.join(OUT_DIR,'img_scatter_k6.png')
savefig(img_scatter)

# scatter comp
fig,axes=plt.subplots(1,2,figsize=(18,7))
fig.suptitle('Comparacion K=5 vs K=6 -- PCA 2D',fontsize=14,fontweight='bold',color='#e0e0ff')
for ax,k in zip(axes,[5,6]):
    pk=[]
    for cid in range(k):
        mask=results[k]['labels']==cid
        ax.scatter(X_pca[mask,0],X_pca[mask,1],c=PALETTE[cid],s=2,alpha=0.35,linewidths=0,rasterized=True)
        pct_c=results[k]['pct'][cid]
        n=CLUSTER_NAMES.get(cid,f'Cluster {cid}') if k==6 else f'Cluster {cid}'
        pk.append(mpatches.Patch(color=PALETTE[cid],label=f'C{cid}: {n} ({pct_c:.0f}%)'))
    ax.legend(handles=pk,fontsize=8,loc='upper right',facecolor='#1a1a2e',edgecolor='#6C63FF',framealpha=0.9)
    ax.set_title(f'K={k} | Sil={results[k]["sil"]:.4f} | DB={results[k]["db"]:.4f}',fontsize=11,color='#6C63FF')
    ax.set_xlabel(f'PC1 ({var_exp[0]:.1f}%)'); ax.set_ylabel(f'PC2 ({var_exp[1]:.1f}%)')
    ax.grid(True,linestyle='--',alpha=0.3); ax.set_facecolor('#1a1a2e')
img_scatter_comp = os.path.join(OUT_DIR,'img_scatter_comp.png')
savefig(img_scatter_comp)

# barras
fig,ax=plt.subplots(figsize=(10,5))
pct6=results[6]['pct']
bars=ax.bar(range(6),pct6.values,color=PALETTE[:6],edgecolor='#0f0f1a',linewidth=0.8)
ax.axhline(100/6,color='#FF6584',linestyle='--',linewidth=1.5,label='Ideal (16.7%)')
for bar,p in zip(bars,pct6.values):
    ax.text(bar.get_x()+bar.get_width()/2,bar.get_height()+0.3,f'{p:.1f}%',ha='center',fontsize=10,color='#e0e0ff',fontweight='bold')
nc=[CLUSTER_NAMES[i] for i in range(6)]
ax.set_xticks(range(6)); ax.set_xticklabels([f'C{i}\n{n[:12]}' for i,n in enumerate(nc)],fontsize=8)
ax.set_title('Distribucion de Tamanos por Cluster (K=6)',fontsize=13,color='#43D9AD',fontweight='bold')
ax.set_ylabel('% del dataset'); ax.set_facecolor('#1a1a2e')
ax.legend(fontsize=9,facecolor='#1a1a2e',edgecolor='#444466')
ax.grid(True,linestyle='--',alpha=0.3)
for sp in ax.spines.values(): sp.set_edgecolor('#444466')
img_barras = os.path.join(OUT_DIR,'img_barras_k6.png')
savefig(img_barras)

# metricas
fig,axes=plt.subplots(1,2,figsize=(10,4))
fig.suptitle('Metricas -- K=5 vs K=6',fontsize=13,fontweight='bold',color='#e0e0ff')
ks=[5,6]; sils=[results[k]['sil'] for k in ks]; dbs=[results[k]['db'] for k in ks]
axes[0].bar(ks,sils,color=['#6C63FF','#43D9AD'],edgecolor='#0f0f1a',width=0.5)
for k,s in zip(ks,sils): axes[0].text(k,s+0.003,f'{s:.4f}',ha='center',fontsize=10,color='#e0e0ff')
axes[0].set_title('Silhouette Score (mejor alto)',color='#6C63FF')
axes[0].set_xticks(ks); axes[0].set_xticklabels([f'K={k}' for k in ks]); axes[0].set_facecolor('#1a1a2e')
axes[1].bar(ks,dbs,color=['#6C63FF','#43D9AD'],edgecolor='#0f0f1a',width=0.5)
for k,d in zip(ks,dbs): axes[1].text(k,d+0.01,f'{d:.4f}',ha='center',fontsize=10,color='#e0e0ff')
axes[1].set_title('Davies-Bouldin (mejor bajo)',color='#43D9AD')
axes[1].set_xticks(ks); axes[1].set_xticklabels([f'K={k}' for k in ks]); axes[1].set_facecolor('#1a1a2e')
for ax in axes:
    ax.grid(True,linestyle='--',alpha=0.4)
    for sp in ax.spines.values(): sp.set_edgecolor('#444466')
img_metricas = os.path.join(OUT_DIR,'img_metricas.png')
savefig(img_metricas)

# kmeans diagram
np.random.seed(42)
fig,axes=plt.subplots(1,3,figsize=(15,5))
fig.suptitle('Como funciona K-Means',fontsize=14,fontweight='bold',color='#e0e0ff')
pts=np.vstack([np.random.randn(60,2)+[0,0],np.random.randn(60,2)+[5,5],np.random.randn(60,2)+[0,5]])
axes[0].scatter(pts[:,0],pts[:,1],c='#a0a0cc',s=25,alpha=0.6)
ci=np.array([[1,1],[3,4],[2,6]],dtype=float)
axes[0].scatter(ci[:,0],ci[:,1],c='#FFB347',s=200,marker='*',zorder=5,label='Centroides iniciales')
axes[0].set_title('Paso 1: Inicializar centroides',color='#FFB347',fontsize=11)
axes[0].legend(fontsize=8,facecolor='#1a1a2e'); axes[0].set_facecolor('#1a1a2e')
axes[0].grid(True,linestyle='--',alpha=0.3)
km_d=KMeans(n_clusters=3,random_state=42,n_init=5)
dl=km_d.fit_predict(pts)
for i in range(3):
    mask=dl==i; axes[1].scatter(pts[mask,0],pts[mask,1],c=PALETTE[i],s=25,alpha=0.6)
axes[1].scatter(km_d.cluster_centers_[:,0],km_d.cluster_centers_[:,1],c='#FFB347',s=200,marker='*',zorder=5,label='Centroides finales')
axes[1].set_title('Paso 2: Asignar al centroide mas cercano',color='#43D9AD',fontsize=10)
axes[1].legend(fontsize=8,facecolor='#1a1a2e'); axes[1].set_facecolor('#1a1a2e')
axes[1].grid(True,linestyle='--',alpha=0.3)
for i in range(3):
    mask=dl==i; axes[2].scatter(pts[mask,0],pts[mask,1],c=PALETTE[i],s=25,alpha=0.6,label=f'Cluster {i}')
    cx,cy=km_d.cluster_centers_[i]
    circle=plt.Circle((cx,cy),1.8,color=PALETTE[i],fill=False,linestyle='--',linewidth=1.5,alpha=0.5)
    axes[2].add_patch(circle)
axes[2].scatter(km_d.cluster_centers_[:,0],km_d.cluster_centers_[:,1],c='#FFB347',s=200,marker='*',zorder=5)
axes[2].set_title('Paso 3: Recalcular y converger',color='#FF6584',fontsize=11)
axes[2].legend(fontsize=8,facecolor='#1a1a2e'); axes[2].set_facecolor('#1a1a2e')
axes[2].grid(True,linestyle='--',alpha=0.3)
for ax in axes:
    for sp in ax.spines.values(): sp.set_edgecolor('#444466')
img_kmeans_diag = os.path.join(OUT_DIR,'img_kmeans_diagrama.png')
savefig(img_kmeans_diag)

print('Imagenes OK', flush=True)

# Guardar variables para el segundo script
import json
meta = {
    'n_orig_rows': int(n_orig_rows), 'n_orig_cols': int(n_orig_cols),
    'n_final_rows': int(n_final_rows), 'n_final_cols': int(n_final_cols),
    'n_dup': int(n_dup), 'drop_cols': drop_cols,
    'var_exp': [float(v) for v in var_exp],
    'results_5_sil': float(results[5]['sil']), 'results_5_db': float(results[5]['db']),
    'results_6_sil': float(results[6]['sil']), 'results_6_db': float(results[6]['db']),
    'sizes_6': {str(k): int(v) for k,v in results[6]['sizes'].items()},
    'pct_6': {str(k): float(v) for k,v in results[6]['pct'].items()},
    'sizes_5': {str(k): int(v) for k,v in results[5]['sizes'].items()},
    'pct_5': {str(k): float(v) for k,v in results[5]['pct'].items()},
    'img_nulos': img_nulos, 'img_scatter': img_scatter,
    'img_scatter_comp': img_scatter_comp, 'img_barras': img_barras,
    'img_metricas': img_metricas, 'img_kmeans_diag': img_kmeans_diag,
    'OUT_DIR': OUT_DIR, 'csv_path': csv_path,
}
meta_path = os.path.join(OUT_DIR, '_meta.json')
with open(meta_path,'w',encoding='utf-8') as f: json.dump(meta, f, ensure_ascii=False, indent=2)
print(f'Meta guardada: {meta_path}', flush=True)
