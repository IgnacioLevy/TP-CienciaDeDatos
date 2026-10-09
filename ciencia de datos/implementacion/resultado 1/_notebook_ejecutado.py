import os
import warnings
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import seaborn as sns
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score, davies_bouldin_score
from sklearn.compose import ColumnTransformer

warnings.filterwarnings('ignore')

# Rutas
DATA_PATH  = r'd:\Cathy\Documentos\ciencia de datos\recursos\secondary_data.csv'
OUTPUT_DIR = r'd:\Cathy\Documentos\ciencia de datos\implementacion\resultado 1'
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Paleta de colores para los clusters
PALETTE = ['#6C63FF', '#FF6584', '#43D9AD', '#FFB347', '#5EB8FF', '#FF6F61']

# Estilo oscuro premium
plt.rcParams.update({
    'font.family':      'DejaVu Sans',
    'axes.facecolor':   '#1a1a2e',
    'figure.facecolor': '#0f0f1a',
    'axes.edgecolor':   '#444466',
    'axes.labelcolor':  '#e0e0ff',
    'xtick.color':      '#a0a0cc',
    'ytick.color':      '#a0a0cc',
    'text.color':       '#e0e0ff',
    'grid.color':       '#2a2a4a',
    'grid.linewidth':   0.5,
})

print('Librerías importadas correctamente ✓')

df_raw = pd.read_csv(DATA_PATH, sep=';')

print(f'Dimensiones: {df_raw.shape[0]:,} filas × {df_raw.shape[1]} columnas')
print(f'\nColumnas: {df_raw.columns.tolist()}')
df_raw.head()

# Distribución de la variable target (solo informativo, no se usa en clustering)
print('Distribución de clases (target):')
print(df_raw['class'].value_counts())
print(f"\nComestibles: {(df_raw['class']=='e').sum():,} ({(df_raw['class']=='e').mean():.1%})")
print(f"Venenosos  : {(df_raw['class']=='p').sum():,} ({(df_raw['class']=='p').mean():.1%})")

df = df_raw.copy()

# Separar y descartar target
target = df['class'].copy()
df = df.drop(columns=['class'])

# Eliminar duplicados
n_dup = df.duplicated().sum()
df = df.drop_duplicates()
print(f'Duplicados eliminados: {n_dup}')

# Porcentaje de nulos por columna
null_pct = df.isnull().sum() / len(df) * 100
print('\n% de nulos por columna (ordenado desc):')
null_pct.sort_values(ascending=False)

# Visualizar nulos
fig, ax = plt.subplots(figsize=(11, 4))
colors_bar = ['#FF6584' if p > 70 else '#6C63FF' for p in null_pct.sort_values(ascending=False)]
null_pct.sort_values(ascending=False).plot(kind='bar', ax=ax, color=colors_bar, edgecolor='#0f0f1a')
ax.axhline(70, color='#FFB347', linestyle='--', linewidth=1.5, label='Umbral 70% (eliminación)')
ax.set_title('Porcentaje de Valores Nulos por Columna', fontsize=13, fontweight='bold', color='#e0e0ff')
ax.set_xlabel('Columna')
ax.set_ylabel('% Nulos')
ax.legend(facecolor='#1a1a2e', edgecolor='#444466')
ax.set_facecolor('#1a1a2e')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig(f'{OUTPUT_DIR}/nulos_por_columna.png', dpi=150, bbox_inches='tight', facecolor=fig.get_facecolor())
pass  # plt.show() desactivado en modo script

# Eliminar columnas con >70% de nulos
drop_cols = null_pct[null_pct > 70].index.tolist()
print(f'Columnas eliminadas (>70% nulos): {drop_cols}')
df = df.drop(columns=drop_cols)

# Imputar restantes
num_cols = df.select_dtypes(include=['float64', 'int64']).columns.tolist()
cat_cols = df.select_dtypes(include='object').columns.tolist()

for col in num_cols:
    df[col] = df[col].fillna(df[col].median())
for col in cat_cols:
    df[col] = df[col].fillna(df[col].mode()[0])

print(f'\nDataset limpio: {df.shape[0]:,} filas × {df.shape[1]} columnas')
print(f'Columnas numéricas  : {num_cols}')
print(f'Columnas categóricas: {cat_cols}')

# Selección de columnas morfológicas
COLS_SELECCIONADAS = [
    'cap-diameter', 'cap-shape', 'cap-surface', 'cap-color',
    'stem-height', 'stem-width', 'stem-color', 'stem-surface',
    'gill-color', 'gill-attachment', 'gill-spacing',
    'has-ring', 'ring-type'
]

df_model = df[COLS_SELECCIONADAS].copy()

num_c = df_model.select_dtypes(include=['float64', 'int64']).columns.tolist()
cat_c = df_model.select_dtypes(include='object').columns.tolist()

print(f'Columnas seleccionadas ({len(COLS_SELECCIONADAS)}): {COLS_SELECCIONADAS}')
print(f'\nNuméricas  : {num_c}')
print(f'Categóricas: {cat_c}')

# One-Hot Encoding + StandardScaler
preprocessor = ColumnTransformer(transformers=[
    ('num', StandardScaler(), num_c),
    ('cat', OneHotEncoder(handle_unknown='ignore', sparse_output=False), cat_c)
])

X = preprocessor.fit_transform(df_model)
print(f'Matriz transformada: {X.shape[0]:,} × {X.shape[1]} features')

pca = PCA(n_components=2, random_state=42)
X_pca = pca.fit_transform(X)
var_exp = pca.explained_variance_ratio_ * 100

print(f'PC1 explica: {var_exp[0]:.1f}%')
print(f'PC2 explica: {var_exp[1]:.1f}%')
print(f'Total:       {sum(var_exp):.1f}%')

results = {}

for k in [5, 6]:
    km = KMeans(n_clusters=k, random_state=42, n_init=15, max_iter=500)
    labels = km.fit_predict(X)
    sil    = silhouette_score(X_pca, labels, sample_size=10_000, random_state=42)
    db     = davies_bouldin_score(X_pca, labels)
    sizes  = pd.Series(labels).value_counts().sort_index()
    pct    = (sizes / len(labels) * 100).round(1)

    results[k] = {'labels': labels, 'sil': sil, 'db': db, 'sizes': sizes, 'pct': pct}

    print(f'K={k} | Silhouette={sil:.4f} | Davies-Bouldin={db:.4f}')
    print(f'  Distribución: {dict(pct.items())}\n')

# Tabla resumen de métricas
df_metrics = pd.DataFrame([
    {'K': k, 'Silhouette (↑ mejor)': v['sil'], 'Davies-Bouldin (↓ mejor)': v['db']}
    for k, v in results.items()
])
df_metrics.style.background_gradient(subset=['Silhouette (↑ mejor)'], cmap='Greens') \
                .background_gradient(subset=['Davies-Bouldin (↓ mejor)'], cmap='Reds_r') \
                .format({'Silhouette (↑ mejor)': '{:.4f}', 'Davies-Bouldin (↓ mejor)': '{:.4f}'})

# Gráfico comparativo de métricas
fig, axes = plt.subplots(1, 3, figsize=(15, 4))
fig.suptitle('Comparativa de Métricas — K=5 vs K=6', fontsize=14, fontweight='bold', color='#e0e0ff')

ks = list(results.keys())
sils = [results[k]['sil'] for k in ks]
dbs  = [results[k]['db']  for k in ks]

# Silhouette
axes[0].bar(ks, sils, color=['#6C63FF', '#43D9AD'], edgecolor='#0f0f1a', width=0.5)
for i, (k, s) in enumerate(zip(ks, sils)):
    axes[0].text(k, s + 0.005, f'{s:.4f}', ha='center', fontsize=10, color='#e0e0ff')
axes[0].set_title('Silhouette Score (↑ mejor)', color='#6C63FF')
axes[0].set_xticks(ks); axes[0].set_xticklabels([f'K={k}' for k in ks])
axes[0].set_facecolor('#1a1a2e')

# Davies-Bouldin
axes[1].bar(ks, dbs, color=['#6C63FF', '#43D9AD'], edgecolor='#0f0f1a', width=0.5)
for i, (k, d) in enumerate(zip(ks, dbs)):
    axes[1].text(k, d + 0.01, f'{d:.4f}', ha='center', fontsize=10, color='#e0e0ff')
axes[1].set_title('Davies-Bouldin (↓ mejor)', color='#43D9AD')
axes[1].set_xticks(ks); axes[1].set_xticklabels([f'K={k}' for k in ks])
axes[1].set_facecolor('#1a1a2e')

# Distribución de tamaños
for k in ks:
    pct = results[k]['pct']
    axes[2].bar([f'C{i}\n(K={k})' for i in range(k)],
                pct.values,
                color=[PALETTE[i % len(PALETTE)] for i in range(k)],
                alpha=0.8 if k == 5 else 0.5,
                edgecolor='#0f0f1a')
axes[2].axhline(100/5, color='#FFB347', linestyle='--', linewidth=1, label='Ideal K=5 (20%)')
axes[2].axhline(100/6, color='#FF6584', linestyle=':', linewidth=1, label='Ideal K=6 (16.7%)')
axes[2].set_title('Distribución de tamaños', color='#FF6584')
axes[2].set_ylabel('%'); axes[2].legend(fontsize=7, facecolor='#1a1a2e', edgecolor='#444466')
axes[2].set_facecolor('#1a1a2e')

for ax in axes:
    ax.grid(True, linestyle='--', alpha=0.4)
    for sp in ax.spines.values(): sp.set_edgecolor('#444466')

plt.tight_layout()
plt.savefig(f'{OUTPUT_DIR}/metricas_comparativa.png', dpi=150, bbox_inches='tight', facecolor=fig.get_facecolor())
pass  # plt.show() desactivado en modo script

# Nombres de clusters para K=6 (configuración final elegida)
K_FINAL = 6

CLUSTER_NAMES = {
    0: '🍄 Anillados convexos marrones',
    1: '🍄 Grandes de poros',
    2: '🍄 Pegajosos sin anillo',
    3: '🍄 Pequeños sin anillo',
    4: '🍄 Esféricos amarillos (raros)',
    5: '🍄 Grandes blancos'
}

df_analisis = df_model.copy()
df_analisis['cluster'] = results[K_FINAL]['labels']
df_analisis['nombre']  = df_analisis['cluster'].map(CLUSTER_NAMES)

print('Distribución de clusters:')
for cid, nombre in CLUSTER_NAMES.items():
    n = (df_analisis['cluster'] == cid).sum()
    pct = n / len(df_analisis) * 100
    print(f'  {nombre}: {n:,} hongos ({pct:.1f}%)')

# Tabla de perfil: media de numéricas y moda de categóricas por cluster
perfiles_num = df_analisis.groupby('cluster')[num_c].mean().round(2)
perfiles_num.index = [CLUSTER_NAMES[i] for i in perfiles_num.index]

print('Perfil numérico por cluster (medias):')
perfiles_num.style.background_gradient(cmap='Blues', axis=0)

# Moda y frecuencia de las columnas categóricas por cluster
print('Perfil categórico por cluster (moda | frecuencia):')
filas = []
for cid, nombre in CLUSTER_NAMES.items():
    grp = df_analisis[df_analisis['cluster'] == cid]
    fila = {'Cluster': nombre}
    for col in cat_c:
        moda = grp[col].mode()[0]
        freq = (grp[col] == moda).mean()
        fila[col] = f'{moda} ({freq:.0%})'
    filas.append(fila)

pd.DataFrame(filas).set_index('Cluster')

# ── Scatter PCA — K=5 vs K=6 lado a lado ──
fig, axes = plt.subplots(1, 2, figsize=(18, 7))
fig.suptitle('Clustering de Hongos — Proyección PCA 2D\nColumnas morfológicas: Sombrero + Tallo + Láminas',
             fontsize=15, fontweight='bold', color='#e0e0ff', y=1.02)

for ax, k in zip(axes, [5, 6]):
    labels  = results[k]['labels']
    nombres = CLUSTER_NAMES if k == 6 else {i: f'Cluster {i}' for i in range(k)}
    patches = []
    for cid in range(k):
        mask = labels == cid
        ax.scatter(X_pca[mask, 0], X_pca[mask, 1],
                   c=PALETTE[cid], s=2.5, alpha=0.4,
                   linewidths=0, rasterized=True)
        pct_c = results[k]['pct'][cid]
        nombre_corto = nombres.get(cid, f'C{cid}').replace('🍄 ', '')
        patches.append(mpatches.Patch(color=PALETTE[cid],
                       label=f'C{cid}: {nombre_corto} ({pct_c:.0f}%)'))

    ax.legend(handles=patches, fontsize=8.5, loc='upper right',
              facecolor='#1a1a2e', edgecolor='#6C63FF', framealpha=0.9)
    ax.set_title(f'K = {k} | Silhouette = {results[k]["sil"]:.4f} | DB = {results[k]["db"]:.4f}',
                 fontsize=12, color='#6C63FF')
    ax.set_xlabel(f'PC1 ({var_exp[0]:.1f}% varianza)', fontsize=10)
    ax.set_ylabel(f'PC2 ({var_exp[1]:.1f}% varianza)', fontsize=10)
    ax.grid(True, linestyle='--', alpha=0.3)

plt.tight_layout()
plt.savefig(f'{OUTPUT_DIR}/scatter_K5_K6.png', dpi=150, bbox_inches='tight', facecolor=fig.get_facecolor())
pass  # plt.show() desactivado en modo script

# ── Heatmap de perfiles de cluster (K=6) ──
df_heat = df_model.copy()
df_heat['cluster'] = results[K_FINAL]['labels']

df_enc = df_heat.copy()
for col in cat_c:
    df_enc[col] = pd.Categorical(df_enc[col]).codes

profile = df_enc.groupby('cluster').mean()
profile_norm = (profile - profile.mean()) / (profile.std() + 1e-9)
profile_norm.index = [CLUSTER_NAMES[i].replace('🍄 ', '') for i in profile_norm.index]

fig, ax = plt.subplots(figsize=(14, 5))
im = ax.imshow(profile_norm.values, aspect='auto', cmap='RdYlGn', vmin=-2, vmax=2)
ax.set_xticks(range(len(profile_norm.columns)))
ax.set_xticklabels(profile_norm.columns, rotation=45, ha='right', fontsize=9)
ax.set_yticks(range(K_FINAL))
ax.set_yticklabels(profile_norm.index, fontsize=9)
cbar = plt.colorbar(im, ax=ax, label='Z-score respecto al promedio global')
cbar.ax.yaxis.label.set_color('#e0e0ff')
ax.set_title('Heatmap de Perfiles Morfológicos por Cluster (K=6)',
             fontsize=14, fontweight='bold', color='#e0e0ff', pad=15)
plt.tight_layout()
plt.savefig(f'{OUTPUT_DIR}/heatmap_perfiles_K6.png', dpi=150, bbox_inches='tight', facecolor=fig.get_facecolor())
pass  # plt.show() desactivado en modo script

# ── Barras de tamaño de clusters ──
fig, axes = plt.subplots(1, 2, figsize=(14, 5))
fig.suptitle('Distribución de Tamaño de Clusters', fontsize=14, fontweight='bold', color='#e0e0ff')

for ax, k in zip(axes, [5, 6]):
    pct    = results[k]['pct']
    labels_text = [CLUSTER_NAMES.get(i, f'C{i}').replace('🍄 ', 'C'+str(i)+'\n') for i in range(k)]
    bars = ax.bar(range(k), pct.values,
                  color=[PALETTE[i] for i in range(k)],
                  edgecolor='#0f0f1a', linewidth=0.8)
    for bar, p in zip(bars, pct.values):
        ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.5,
                f'{p:.1f}%', ha='center', fontsize=9, color='#e0e0ff', fontweight='bold')
    ax.axhline(100/k, color='#FF6584', linestyle='--', linewidth=1.5,
               label=f'Distribución ideal ({100/k:.1f}%)')
    ax.set_title(f'K={k} | Uniformidad: StdTam={pct.std():.1f}%', fontsize=11, color='#43D9AD')
    ax.set_xlabel('Cluster'); ax.set_ylabel('% del dataset')
    ax.set_xticks(range(k))
    ax.set_xticklabels([f'C{i}' for i in range(k)])
    ax.legend(fontsize=8, facecolor='#1a1a2e', edgecolor='#444466')
    ax.set_facecolor('#1a1a2e')
    ax.grid(True, linestyle='--', alpha=0.3)
    for sp in ax.spines.values(): sp.set_edgecolor('#444466')

plt.tight_layout()
plt.savefig(f'{OUTPUT_DIR}/barras_tamaños.png', dpi=150, bbox_inches='tight', facecolor=fig.get_facecolor())
pass  # plt.show() desactivado en modo script

# ── Dashboard final ──
fig = plt.figure(figsize=(20, 13))
fig.patch.set_facecolor('#0f0f1a')
fig.suptitle('Dashboard Final — Clustering de Hongos (K=6)\nSecondary Mushroom Dataset · 13 columnas morfológicas',
             fontsize=18, fontweight='bold', color='#e0e0ff', y=0.99)

gs = fig.add_gridspec(2, 3, hspace=0.5, wspace=0.38)

# Scatter K=6
ax_scatter = fig.add_subplot(gs[0, 0:2])
labels_k6 = results[6]['labels']
patches = []
for cid in range(6):
    mask = labels_k6 == cid
    ax_scatter.scatter(X_pca[mask, 0], X_pca[mask, 1],
                       c=PALETTE[cid], s=2, alpha=0.4, linewidths=0, rasterized=True)
    nombre = CLUSTER_NAMES[cid].replace('🍄 ', '')
    pct_c  = results[6]['pct'][cid]
    patches.append(mpatches.Patch(color=PALETTE[cid], label=f'C{cid}: {nombre} ({pct_c:.0f}%)'))
ax_scatter.legend(handles=patches, fontsize=8, loc='upper right',
                  facecolor='#1a1a2e', edgecolor='#6C63FF')
ax_scatter.set_title(f'Clustering PCA · K=6 | Sil={results[6]["sil"]:.4f}',
                     fontsize=12, color='#6C63FF')
ax_scatter.set_xlabel(f'PC1 ({var_exp[0]:.1f}%)')
ax_scatter.set_ylabel(f'PC2 ({var_exp[1]:.1f}%)')
ax_scatter.set_facecolor('#1a1a2e')
ax_scatter.grid(True, linestyle='--', alpha=0.3)

# Barras de tamaño
ax_bar = fig.add_subplot(gs[0, 2])
pct6 = results[6]['pct']
ax_bar.bar(range(6), pct6.values, color=PALETTE[:6], edgecolor='#0f0f1a')
ax_bar.axhline(100/6, color='#FF6584', linestyle='--', linewidth=1.2)
for i, p in enumerate(pct6.values):
    ax_bar.text(i, p + 0.5, f'{p:.0f}%', ha='center', fontsize=8, color='#e0e0ff')
ax_bar.set_title('Tamaño de clusters', fontsize=11, color='#43D9AD')
ax_bar.set_xticks(range(6)); ax_bar.set_xticklabels([f'C{i}' for i in range(6)])
ax_bar.set_ylabel('%'); ax_bar.set_facecolor('#1a1a2e')
ax_bar.grid(True, linestyle='--', alpha=0.3)
for sp in ax_bar.spines.values(): sp.set_edgecolor('#444466')

# Heatmap
ax_heat = fig.add_subplot(gs[1, 0:3])
im = ax_heat.imshow(profile_norm.values, aspect='auto', cmap='RdYlGn', vmin=-2, vmax=2)
ax_heat.set_xticks(range(len(profile_norm.columns)))
ax_heat.set_xticklabels(profile_norm.columns, rotation=40, ha='right', fontsize=8)
ax_heat.set_yticks(range(K_FINAL))
ax_heat.set_yticklabels([f'C{i}: ' + CLUSTER_NAMES[i].replace('🍄 ', '') for i in range(K_FINAL)], fontsize=8)
plt.colorbar(im, ax=ax_heat, label='Z-score', shrink=0.8)
ax_heat.set_title('Perfil morfológico de cada cluster (heatmap)', fontsize=12, color='#e0e0ff')

plt.savefig(f'{OUTPUT_DIR}/dashboard_final.png', dpi=150, bbox_inches='tight', facecolor=fig.get_facecolor())
pass  # plt.show() desactivado en modo script
print('Dashboard guardado ✓')