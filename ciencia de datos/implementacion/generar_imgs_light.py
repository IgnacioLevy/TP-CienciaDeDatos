# -*- coding: utf-8 -*-
import os, json, warnings
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.patches as patches
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
from sklearn.compose import ColumnTransformer

warnings.filterwarnings('ignore')

BASE = r"E:\cosas\facu\Ciencia de Datos\ciencia de datos-20261008T230846Z-1-001\ciencia de datos"
DATA_PATH = os.path.join(BASE, "recursos", "secondary_data.csv")
OUT_DIR = os.path.join(BASE, "implementacion", "entrega2")
META_PATH = os.path.join(OUT_DIR, "_meta.json")

with open(META_PATH, "r", encoding="utf-8") as f:
    meta = json.load(f)

LIGHT_PALETTE = ['#4F46E5', '#E11D48', '#059669', '#D97706', '#0284C7', '#7C3AED']

plt.rcParams.update({
    'font.family': 'DejaVu Sans',
    'axes.facecolor': '#F8FAFC',
    'figure.facecolor': '#FFFFFF',
    'axes.edgecolor': '#CBD5E1',
    'axes.labelcolor': '#1E293B',
    'xtick.color': '#334155',
    'ytick.color': '#334155',
    'text.color': '#0F172A',
    'grid.color': '#E2E8F0',
    'grid.linewidth': 0.8
})

def savefig(fig, path):
    plt.tight_layout()
    fig.savefig(path, dpi=180, bbox_inches='tight', facecolor='#FFFFFF')
    plt.close(fig)

print("1. Generando pipeline light...", flush=True)
# 1. Pipeline Light
fig, ax = plt.subplots(figsize=(14, 3.2), facecolor='#FFFFFF')
ax.set_facecolor('#FFFFFF')
ax.set_xlim(0, 14)
ax.set_ylim(0, 3.2)
ax.axis('off')

steps = [
    ("01. Auditoría", "61.069 filas crudas\nEliminación 146 dup.", "#4F46E5"),
    ("02. Poda Morfo", "Descarte >70% nulos\nExclusión de 'class'", "#0284C7"),
    ("03. Imputación", "Mediana (continuas)\nModa (nominales)", "#059669"),
    ("04. Vectorización", "StandardScaler +\nOneHot (13 vars)", "#D97706"),
    ("05. K-Means", "K=6 (Davies-B.=0.84)\nProyección PCA 2D", "#E11D48"),
    ("06. Taxonomía", "6 Morfotipos\nFenotipos biológicos", "#7C3AED")
]

card_w = 1.95
card_h = 2.2
gap = 0.35
start_x = 0.35
y = 0.5

for i, (title, desc, col) in enumerate(steps):
    x = start_x + i * (card_w + gap)
    rect = patches.FancyBboxPatch((x, y), card_w, card_h, boxstyle="round,pad=0.08,rounding_size=0.15",
                                  facecolor='#F8FAFC', edgecolor=col, linewidth=2.0)
    ax.add_patch(rect)
    ax.text(x + card_w/2, y + card_h - 0.35, title, color='#0F172A', fontsize=10.5, fontweight='bold', ha='center', va='center')
    ax.text(x + card_w/2, y + card_h/2 - 0.25, desc, color='#475569', fontsize=9, ha='center', va='center', linespacing=1.3)
    if i < len(steps) - 1:
        arr_x = x + card_w + 0.05
        ax.annotate("", xy=(arr_x + gap - 0.1, y + card_h/2), xytext=(arr_x, y + card_h/2),
                    arrowprops=dict(arrowstyle="->", color='#4F46E5', lw=2.4))

img_pipeline_light = os.path.join(OUT_DIR, "img_pipeline_light.png")
savefig(fig, img_pipeline_light)

print("2. Generando nulos light...", flush=True)
# 2. Nulos Light
df_raw = pd.read_csv(DATA_PATH, sep=';')
null_pct_orig = df_raw.isnull().sum() / len(df_raw) * 100
cs = null_pct_orig.drop('class').sort_values(ascending=False)
cb = ['#EF4444' if p > 70 else '#4F46E5' for p in cs]

fig, ax = plt.subplots(figsize=(11, 4.5), facecolor='#FFFFFF')
cs.plot(kind='bar', ax=ax, color=cb, edgecolor='#0F172A', linewidth=0.5)
ax.axhline(70, color='#D97706', linestyle='--', linewidth=2.0, label='Umbral de Poda (70%)')
ax.set_title('Porcentaje de Valores Faltantes por Variable (Secondary Mushroom)', fontsize=13, fontweight='bold', color='#0F172A', pad=10)
ax.set_xlabel('Atributos del Dataset', fontsize=10, fontweight='bold', color='#1E293B')
ax.set_ylabel('% de Valores Nulos', fontsize=10, fontweight='bold', color='#1E293B')
ax.legend(facecolor='#FFFFFF', edgecolor='#CBD5E1', fontsize=10)
ax.grid(True, linestyle='--', alpha=0.6, axis='y')
plt.xticks(rotation=45, ha='right', fontsize=9)
img_nulos_light = os.path.join(OUT_DIR, "img_nulos_light.png")
savefig(fig, img_nulos_light)

print("3. Generando K-Means diagrama light...", flush=True)
# 3. K-Means Diagrama Light
np.random.seed(42)
fig, axes = plt.subplots(1, 3, figsize=(14, 4.2), facecolor='#FFFFFF')
fig.suptitle('Ciclo de Funcionamiento del Algoritmo K-Means', fontsize=13, fontweight='bold', color='#0F172A')
pts = np.vstack([np.random.randn(60, 2) + [0, 0], np.random.randn(60, 2) + [5, 5], np.random.randn(60, 2) + [0, 5]])

# Step 1
axes[0].scatter(pts[:, 0], pts[:, 1], c='#64748B', s=30, alpha=0.6, edgecolors='none')
ci = np.array([[1, 1], [3, 4], [2, 6]], dtype=float)
axes[0].scatter(ci[:, 0], ci[:, 1], c='#D97706', s=220, marker='*', zorder=5, label='Semillas iniciales')
axes[0].set_title('Paso 1: Inicializar Centroides', color='#D97706', fontsize=11, fontweight='bold')
axes[0].legend(fontsize=9, facecolor='#FFFFFF', edgecolor='#CBD5E1')
axes[0].grid(True, linestyle='--', alpha=0.5)

# Step 2
km_d = KMeans(n_clusters=3, random_state=42, n_init=5)
dl = km_d.fit_predict(pts)
for i in range(3):
    mask = dl == i
    axes[1].scatter(pts[mask, 0], pts[mask, 1], c=LIGHT_PALETTE[i], s=30, alpha=0.7, edgecolors='none')
axes[1].scatter(km_d.cluster_centers_[:, 0], km_d.cluster_centers_[:, 1], c='#D97706', s=220, marker='*', zorder=5, label='Centroides')
axes[1].set_title('Paso 2: Asignación Euclídea', color='#4F46E5', fontsize=11, fontweight='bold')
axes[1].legend(fontsize=9, facecolor='#FFFFFF', edgecolor='#CBD5E1')
axes[1].grid(True, linestyle='--', alpha=0.5)

# Step 3
for i in range(3):
    mask = dl == i
    axes[2].scatter(pts[mask, 0], pts[mask, 1], c=LIGHT_PALETTE[i], s=30, alpha=0.7, edgecolors='none', label=f'Cluster {i}')
    cx, cy = km_d.cluster_centers_[i]
    circle = plt.Circle((cx, cy), 1.8, color=LIGHT_PALETTE[i], fill=False, linestyle='--', linewidth=1.8, alpha=0.7)
    axes[2].add_patch(circle)
axes[2].scatter(km_d.cluster_centers_[:, 0], km_d.cluster_centers_[:, 1], c='#D97706', s=220, marker='*', zorder=5)
axes[2].set_title('Paso 3: Recálculo y Convergencia', color='#059669', fontsize=11, fontweight='bold')
axes[2].legend(fontsize=9, facecolor='#FFFFFF', edgecolor='#CBD5E1')
axes[2].grid(True, linestyle='--', alpha=0.5)

img_kmeans_diag_light = os.path.join(OUT_DIR, "img_kmeans_diagrama_light.png")
savefig(fig, img_kmeans_diag_light)

print("4. Generando métricas light...", flush=True)
# 4. Métricas Light
fig, axes = plt.subplots(1, 2, figsize=(9.5, 3.8), facecolor='#FFFFFF')
fig.suptitle('Evaluación de Modelos: K=5 vs K=6', fontsize=12, fontweight='bold', color='#0F172A')
ks = [5, 6]
sils = [meta['results_5_sil'], meta['results_6_sil']]
dbs = [meta['results_5_db'], meta['results_6_db']]

axes[0].bar(ks, sils, color=['#4F46E5', '#059669'], edgecolor='#0F172A', width=0.45)
for k, s in zip(ks, sils):
    axes[0].text(k, s + 0.005, f'{s:.4f}', ha='center', fontsize=10.5, color='#0F172A', fontweight='bold')
axes[0].set_title('Silhouette Score (Mayor = Mejor)', color='#4F46E5', fontsize=11, fontweight='bold')
axes[0].set_xticks(ks)
axes[0].set_xticklabels([f'K={k}' for k in ks], fontsize=10, fontweight='bold')
axes[0].set_ylim(0, 0.42)
axes[0].grid(True, linestyle='--', alpha=0.5, axis='y')

axes[1].bar(ks, dbs, color=['#4F46E5', '#059669'], edgecolor='#0F172A', width=0.45)
for k, d in zip(ks, dbs):
    axes[1].text(k, d + 0.015, f'{d:.4f}', ha='center', fontsize=10.5, color='#0F172A', fontweight='bold')
axes[1].set_title('Davies-Bouldin Index (Menor = Mejor)', color='#059669', fontsize=11, fontweight='bold')
axes[1].set_xticks(ks)
axes[1].set_xticklabels([f'K={k}' for k in ks], fontsize=10, fontweight='bold')
axes[1].set_ylim(0, 1.05)
axes[1].grid(True, linestyle='--', alpha=0.5, axis='y')

img_metricas_light = os.path.join(OUT_DIR, "img_metricas_light.png")
savefig(fig, img_metricas_light)

print("5. Procesando dataset para scatter y barras...", flush=True)
# Load clean dataset
df_model = pd.read_csv(os.path.join(OUT_DIR, "dataset_clustering.csv"))
COLS_MORFO = ['cap-diameter','cap-shape','cap-surface','cap-color',
    'stem-height','stem-width','stem-color','stem-surface',
    'gill-color','gill-attachment','gill-spacing','has-ring','ring-type']

num_c = ['cap-diameter', 'stem-height', 'stem-width']
cat_c = [c for c in COLS_MORFO if c not in num_c]

preprocessor = ColumnTransformer(transformers=[
    ('num', StandardScaler(), num_c),
    ('cat', OneHotEncoder(handle_unknown='ignore', sparse_output=False), cat_c)])
X = preprocessor.fit_transform(df_model[COLS_MORFO])

pca = PCA(n_components=2, random_state=42)
X_pca = pca.fit_transform(X)
var_exp = meta['var_exp']

CLUSTER_NAMES = {
    0: 'Anillados convexos marrones',
    1: 'Grandes de poros',
    2: 'Pegajosos sin anillo',
    3: 'Pequeños sin anillo',
    4: 'Esféricos amarillos raros',
    5: 'Grandes blancos'
}

# 5. Scatter K=6 Light
print("Generando scatter K=6 light...", flush=True)
fig, ax = plt.subplots(figsize=(9.5, 6.2), facecolor='#FFFFFF')
patches_list = []
for cid in range(6):
    mask = df_model['cluster'] == cid
    ax.scatter(X_pca[mask, 0], X_pca[mask, 1], c=LIGHT_PALETTE[cid], s=3.0, alpha=0.45, linewidths=0, rasterized=True)
    pct_c = meta['pct_6'][str(cid)]
    patches_list.append(mpatches.Patch(color=LIGHT_PALETTE[cid], label=f'C{cid}: {CLUSTER_NAMES[cid]} ({pct_c:.1f}%)'))

ax.legend(handles=patches_list, fontsize=9.5, loc='upper right', facecolor='#FFFFFF', edgecolor='#CBD5E1', framealpha=0.95)
ax.set_title(f'Clusterización K=6 -- PCA 2D (Silhouette: {meta["results_6_sil"]:.4f} | Davies-Bouldin: {meta["results_6_db"]:.4f})',
             fontsize=12, fontweight='bold', color='#0F172A', pad=10)
ax.set_xlabel(f'Componente Principal 1 ({var_exp[0]:.1f}% varianza)', fontsize=10, fontweight='bold')
ax.set_ylabel(f'Componente Principal 2 ({var_exp[1]:.1f}% varianza)', fontsize=10, fontweight='bold')
ax.grid(True, linestyle='--', alpha=0.6)
img_scatter_k6_light = os.path.join(OUT_DIR, "img_scatter_k6_light.png")
savefig(fig, img_scatter_k6_light)

# 6. Scatter Comp K=5 vs K=6 Light
print("Generando scatter comp light...", flush=True)
km5 = KMeans(n_clusters=5, random_state=42, n_init=10)
labels_5 = km5.fit_predict(X)

fig, axes = plt.subplots(1, 2, figsize=(16, 5.8), facecolor='#FFFFFF')
fig.suptitle('Comparación de Estructura de Conglomerados: K=5 vs K=6 (PCA 2D)', fontsize=13, fontweight='bold', color='#0F172A')

for ax, k, labs in zip(axes, [5, 6], [labels_5, df_model['cluster'].values]):
    pk = []
    for cid in range(k):
        mask = labs == cid
        ax.scatter(X_pca[mask, 0], X_pca[mask, 1], c=LIGHT_PALETTE[cid], s=2.5, alpha=0.4, linewidths=0, rasterized=True)
        pct_c = (mask.sum() / len(labs)) * 100
        n = CLUSTER_NAMES.get(cid, f'Cluster {cid}') if k == 6 else f'Cluster {cid}'
        pk.append(mpatches.Patch(color=LIGHT_PALETTE[cid], label=f'C{cid}: {n[:18]} ({pct_c:.0f}%)'))
    ax.legend(handles=pk, fontsize=8.5, loc='upper right', facecolor='#FFFFFF', edgecolor='#CBD5E1', framealpha=0.95)
    sil_v = meta['results_5_sil'] if k == 5 else meta['results_6_sil']
    db_v = meta['results_5_db'] if k == 5 else meta['results_6_db']
    ax.set_title(f'Modelo K={k} | Sil={sil_v:.4f} | DB={db_v:.4f}', fontsize=11, fontweight='bold', color='#4F46E5')
    ax.set_xlabel(f'PC1 ({var_exp[0]:.1f}%)', fontsize=9.5)
    ax.set_ylabel(f'PC2 ({var_exp[1]:.1f}%)', fontsize=9.5)
    ax.grid(True, linestyle='--', alpha=0.6)

img_scatter_comp_light = os.path.join(OUT_DIR, "img_scatter_comp_light.png")
savefig(fig, img_scatter_comp_light)

# 7. Barras K=6 Light
print("Generando barras K=6 light...", flush=True)
fig, ax = plt.subplots(figsize=(9.5, 4.6), facecolor='#FFFFFF')
pct6 = [meta['pct_6'][str(i)] for i in range(6)]
bars = ax.bar(range(6), pct6, color=LIGHT_PALETTE[:6], edgecolor='#0F172A', linewidth=0.6)
ax.axhline(100/6, color='#EF4444', linestyle='--', linewidth=1.8, label='Equidistribución Ideal (16.7%)')

for bar, p in zip(bars, pct6):
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.6, f'{p:.1f}%', ha='center', fontsize=10.5, color='#0F172A', fontweight='bold')

nc = [CLUSTER_NAMES[i] for i in range(6)]
ax.set_xticks(range(6))
ax.set_xticklabels([f'C{i}\n{n[:12]}' for i, n in enumerate(nc)], fontsize=9, fontweight='bold')
ax.set_title('Distribución de Especímenes por Cluster (K=6)', fontsize=12, fontweight='bold', color='#0F172A')
ax.set_ylabel('% del Total de Muestras', fontsize=10, fontweight='bold')
ax.set_ylim(0, 42)
ax.legend(fontsize=9.5, facecolor='#FFFFFF', edgecolor='#CBD5E1')
ax.grid(True, linestyle='--', alpha=0.5, axis='y')
img_barras_light = os.path.join(OUT_DIR, "img_barras_k6_light.png")
savefig(fig, img_barras_light)

print("Todas las imágenes en modo claro generadas exitosamente!", flush=True)
