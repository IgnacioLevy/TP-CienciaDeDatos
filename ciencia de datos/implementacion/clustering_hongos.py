# ============================================================
#  CLUSTERING DE HONGOS — Secondary Mushroom Dataset
#  Entrega 2 — Ciencia de Datos
# ============================================================
# Columnas del dataset:
#   Métricas  : cap-diameter, stem-height, stem-width
#   Nominales : cap-shape, cap-surface, cap-color,
#               does-bruise-bleed, gill-attachment, gill-spacing,
#               gill-color, stem-root, stem-surface, stem-color,
#               veil-type, veil-color, has-ring, ring-type,
#               spore-print-color, habitat, season
#   Target    : class (p=poisonous, e=edible) — NO se usa en clustering
# ============================================================

import os
import warnings
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import seaborn as sns
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans, MiniBatchKMeans
from sklearn.metrics import silhouette_score, davies_bouldin_score
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

warnings.filterwarnings("ignore")

# ── rutas ──────────────────────────────────────────────────
DATA_PATH   = r"d:\Cathy\Documentos\ciencia de datos\recursos\secondary_data.csv"
OUTPUT_DIR  = r"d:\Cathy\Documentos\ciencia de datos\implementacion\graficos"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# paleta de colores premium por cluster (hasta 12)
PALETTE = [
    "#6C63FF","#FF6584","#43D9AD","#FFB347","#5EB8FF",
    "#FF6F61","#A8E063","#C9B1FF","#FF9AA2","#B5EAD7",
    "#FFDAC1","#E2B0FF"
]

# ════════════════════════════════════════════════════════════
# 1.  CARGA Y PRIMERA VISTA
# ════════════════════════════════════════════════════════════
print("=" * 60)
print("  1. CARGA DEL DATASET")
print("=" * 60)

df_raw = pd.read_csv(DATA_PATH, sep=";")
print(f"  Filas: {df_raw.shape[0]:,}   Columnas: {df_raw.shape[1]}")
print(f"  Columnas: {df_raw.columns.tolist()}\n")

# ════════════════════════════════════════════════════════════
# 2.  LIMPIEZA
# ════════════════════════════════════════════════════════════
print("=" * 60)
print("  2. LIMPIEZA DE DATOS")
print("=" * 60)

df = df_raw.copy()

# --- 2a. Separar y descartar la columna target -----------
target = df["class"].copy()
df = df.drop(columns=["class"])
print("  v Columna 'class' separada (no se usa en clustering).")

# --- 2b. Duplicados --------------------------------------
n_dup = df.duplicated().sum()
df = df.drop_duplicates()
print(f"  v Duplicados eliminados: {n_dup}")

# --- 2c. Porcentaje de nulos por columna -----------------
null_pct = df.isnull().sum() / len(df) * 100
print("\n  Nulos por columna (solo las que tienen):")
has_nulls = null_pct[null_pct > 0].sort_values(ascending=False)
print(has_nulls.to_string() if not has_nulls.empty else "    Ninguna columna tiene nulos.")

# Eliminar columnas con > 70% de nulos
drop_cols_null = null_pct[null_pct > 70].index.tolist()
if drop_cols_null:
    df = df.drop(columns=drop_cols_null)
    print(f"\n  v Columnas eliminadas por >70% nulos: {drop_cols_null}")
else:
    print("\n  v Ninguna columna supera el 70% de nulos.")

# --- 2d. Columnas de baja varianza (una sola categoria) ---
low_var_cols = []
for col in df.select_dtypes(include="object").columns:
    if df[col].nunique(dropna=False) <= 1:
        low_var_cols.append(col)
if low_var_cols:
    df = df.drop(columns=low_var_cols)
    print(f"  v Columnas con varianza cero eliminadas: {low_var_cols}")
else:
    print("  v Ninguna columna con varianza cero detectada.")

# --- 2e. Imputacion de nulos restantes -------------------
num_cols = df.select_dtypes(include=["float64", "int64"]).columns.tolist()
cat_cols = df.select_dtypes(include="object").columns.tolist()

for col in num_cols:
    median = df[col].median()
    filled = df[col].isnull().sum()
    df[col] = df[col].fillna(median)
    if filled > 0:
        print(f"  v '{col}': {filled} nulos -> mediana ({median:.2f})")

for col in cat_cols:
    moda = df[col].mode()[0]
    filled = df[col].isnull().sum()
    df[col] = df[col].fillna(moda)
    if filled > 0:
        print(f"  v '{col}': {filled} nulos -> moda ('{moda}')")

print(f"\n  Dataset limpio: {df.shape[0]:,} filas x {df.shape[1]} columnas")
print(f"  Columnas numericas : {num_cols}")
print(f"  Columnas categoricas: {cat_cols}\n")

# ════════════════════════════════════════════════════════════
# 3.  TRANSFORMACION — One-Hot + Scaler
# ════════════════════════════════════════════════════════════
print("=" * 60)
print("  3. CODIFICACION Y NORMALIZACION")
print("=" * 60)

preprocessor = ColumnTransformer(transformers=[
    ("num", StandardScaler(), num_cols),
    ("cat", OneHotEncoder(handle_unknown="ignore", sparse_output=False), cat_cols)
])

X = preprocessor.fit_transform(df)
print(f"  v Matriz transformada: {X.shape[0]:,} x {X.shape[1]} features")

# ════════════════════════════════════════════════════════════
# 4.  REDUCCION DIMENSIONAL — PCA para visualizacion
# ════════════════════════════════════════════════════════════
print("\n  Ajustando PCA (2 componentes para visualizacion)...")
pca = PCA(n_components=2, random_state=42)
X_pca = pca.fit_transform(X)
var_exp = pca.explained_variance_ratio_ * 100
print(f"  v Varianza explicada: PC1={var_exp[0]:.1f}%  PC2={var_exp[1]:.1f}%  Total={sum(var_exp):.1f}%\n")

# ════════════════════════════════════════════════════════════
# 5.  MODELOS DE CLUSTERING (K = 7 a 12)
# ════════════════════════════════════════════════════════════
print("=" * 60)
print("  5. ENTRENAMIENTO DE MODELOS (K = 7 a 12)")
print("=" * 60)

K_VALUES = range(7, 13)   # 7,8,9,10,11,12

models = {
    "K-Means": lambda k: KMeans(n_clusters=k, random_state=42, n_init=10, max_iter=300),
    "Mini-Batch K-Means": lambda k: MiniBatchKMeans(n_clusters=k, random_state=42, n_init=10, batch_size=4096),
}

results = {}

for model_name, model_fn in models.items():
    results[model_name] = {}
    print(f"\n  -- {model_name} --")
    for k in K_VALUES:
        model = model_fn(k)
        labels = model.fit_predict(X)
        inertia = model.inertia_ if hasattr(model, "inertia_") else None
        sil     = silhouette_score(X_pca, labels, sample_size=10_000, random_state=42)
        db      = davies_bouldin_score(X_pca, labels)
        results[model_name][k] = {
            "labels": labels,
            "inertia": inertia,
            "silhouette": sil,
            "db": db,
        }
        print(f"    K={k:2d} | Inertia={inertia:>15,.0f} | Silhouette={sil:.4f} | DB={db:.4f}")

# ════════════════════════════════════════════════════════════
# 6.  RESUMEN DE METRICAS
# ════════════════════════════════════════════════════════════
print("\n" + "=" * 60)
print("  6. TABLA RESUMEN DE METRICAS")
print("=" * 60)

rows = []
for model_name, ks in results.items():
    for k, v in ks.items():
        rows.append({
            "Modelo": model_name,
            "K": k,
            "Inertia": round(v["inertia"]) if v["inertia"] else None,
            "Silhouette": round(v["silhouette"], 4),
            "Davies-Bouldin": round(v["db"], 4),
        })

df_metrics = pd.DataFrame(rows)
print(df_metrics.to_string(index=False))
df_metrics.to_csv(os.path.join(OUTPUT_DIR, "metricas_clustering.csv"), index=False)
print(f"\n  v Metricas guardadas en graficos/metricas_clustering.csv")

# ════════════════════════════════════════════════════════════
# 7.  GRAFICOS
# ════════════════════════════════════════════════════════════
print("\n" + "=" * 60)
print("  7. GENERANDO GRAFICOS")
print("=" * 60)

plt.rcParams.update({
    "font.family": "DejaVu Sans",
    "axes.facecolor":  "#1a1a2e",
    "figure.facecolor": "#0f0f1a",
    "axes.edgecolor":  "#444466",
    "axes.labelcolor": "#e0e0ff",
    "xtick.color":     "#a0a0cc",
    "ytick.color":     "#a0a0cc",
    "text.color":      "#e0e0ff",
    "grid.color":      "#2a2a4a",
    "grid.linewidth":  0.5,
})

colors_models = ["#6C63FF", "#43D9AD"]

# ── 7a. Curvas de Codo (Inertia) ─────────────────────────
fig, axes = plt.subplots(1, len(models), figsize=(7 * len(models), 5))
fig.suptitle("Curva de Codo - Inertia por K", fontsize=16, fontweight="bold",
             color="#e0e0ff", y=1.02)

for ax, (model_name, ks) in zip(axes, results.items()):
    ks_list   = list(ks.keys())
    inertias  = [v["inertia"] for v in ks.values()]
    ax.plot(ks_list, inertias, "o-", color="#6C63FF", linewidth=2.5, markersize=8)
    for k, iner in zip(ks_list, inertias):
        ax.annotate(f"{iner:,.0f}", (k, iner), textcoords="offset points",
                    xytext=(0, 10), ha="center", fontsize=7, color="#a0a0cc")
    ax.set_title(model_name, fontsize=13, color="#6C63FF")
    ax.set_xlabel("Numero de Clusters (K)")
    ax.set_ylabel("Inertia (WCSS)")
    ax.grid(True, linestyle="--", alpha=0.5)
    ax.set_xticks(ks_list)

plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, "01_curva_de_codo.png"), dpi=150, bbox_inches="tight",
            facecolor=fig.get_facecolor())
plt.close()
print("  v 01_curva_de_codo.png")

# ── 7b. Silhouette Score vs K ────────────────────────────
fig, ax = plt.subplots(figsize=(9, 5))
fig.suptitle("Coeficiente de Silueta por K y Modelo", fontsize=16,
             fontweight="bold", color="#e0e0ff")

for (model_name, ks), col in zip(results.items(), colors_models):
    ks_list = list(ks.keys())
    sils    = [v["silhouette"] for v in ks.values()]
    ax.plot(ks_list, sils, "o-", label=model_name, color=col, linewidth=2.5, markersize=8)

ax.set_xlabel("Numero de Clusters (K)")
ax.set_ylabel("Silhouette Score (mayor = mejor)")
ax.legend(facecolor="#1a1a2e", edgecolor="#444466")
ax.grid(True, linestyle="--", alpha=0.5)
ax.set_xticks(list(K_VALUES))
plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, "02_silhouette_score.png"), dpi=150, bbox_inches="tight",
            facecolor=fig.get_facecolor())
plt.close()
print("  v 02_silhouette_score.png")

# ── 7c. Davies-Bouldin vs K ──────────────────────────────
fig, ax = plt.subplots(figsize=(9, 5))
fig.suptitle("Davies-Bouldin Score por K y Modelo", fontsize=16,
             fontweight="bold", color="#e0e0ff")

for (model_name, ks), col in zip(results.items(), colors_models):
    ks_list = list(ks.keys())
    dbs     = [v["db"] for v in ks.values()]
    ax.plot(ks_list, dbs, "s-", label=model_name, color=col, linewidth=2.5, markersize=8)

ax.set_xlabel("Numero de Clusters (K)")
ax.set_ylabel("Davies-Bouldin Score (menor = mejor)")
ax.legend(facecolor="#1a1a2e", edgecolor="#444466")
ax.grid(True, linestyle="--", alpha=0.5)
ax.set_xticks(list(K_VALUES))
plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, "03_davies_bouldin.png"), dpi=150, bbox_inches="tight",
            facecolor=fig.get_facecolor())
plt.close()
print("  v 03_davies_bouldin.png")

# ── 7d. Scatter plots PCA — un grafico por (modelo x K) ──
print("\n  Generando scatter plots PCA (1 por modelo x K)...")

for model_name, ks in results.items():
    fig, axes = plt.subplots(2, 3, figsize=(18, 11))
    fig.suptitle(f"Clustering PCA - {model_name}", fontsize=18, fontweight="bold",
                 color="#e0e0ff", y=1.01)

    for ax, (k, v) in zip(axes.flat, ks.items()):
        labels = v["labels"]
        unique_labels = np.unique(labels)
        for cluster_id in unique_labels:
            mask = labels == cluster_id
            ax.scatter(
                X_pca[mask, 0], X_pca[mask, 1],
                c=PALETTE[cluster_id % len(PALETTE)],
                s=2, alpha=0.35, linewidths=0, rasterized=True
            )
        legend_patches = [
            mpatches.Patch(color=PALETTE[i % len(PALETTE)], label=f"Cluster {i}")
            for i in unique_labels
        ]
        ax.legend(handles=legend_patches, fontsize=7, loc="upper right",
                  facecolor="#1a1a2e", edgecolor="#444466", markerscale=2)
        ax.set_title(f"K = {k} | Sil={v['silhouette']:.3f}", fontsize=12, color="#6C63FF")
        ax.set_xlabel(f"PC1 ({var_exp[0]:.1f}%)", fontsize=9)
        ax.set_ylabel(f"PC2 ({var_exp[1]:.1f}%)", fontsize=9)
        ax.grid(True, linestyle="--", alpha=0.3)

    plt.tight_layout()
    safe_name = model_name.lower().replace(" ", "_").replace("-", "_")
    fname = f"04_scatter_pca_{safe_name}.png"
    plt.savefig(os.path.join(OUTPUT_DIR, fname), dpi=150, bbox_inches="tight",
                facecolor=fig.get_facecolor())
    plt.close()
    print(f"  v {fname}")

# ── 7e. Dashboard comparativo final ──────────────────────
print("\n  Generando dashboard comparativo final...")

fig = plt.figure(figsize=(20, 14))
fig.patch.set_facecolor("#0f0f1a")
fig.suptitle("Dashboard - Comparativa de Clustering de Hongos\nSecondary Mushroom Dataset",
             fontsize=20, fontweight="bold", color="#e0e0ff", y=0.98)

gs = fig.add_gridspec(3, 4, hspace=0.5, wspace=0.4)

# Fila 0: curvas de codo
for col_idx, (model_name, ks) in enumerate(results.items()):
    ax = fig.add_subplot(gs[0, col_idx * 2: col_idx * 2 + 2])
    ks_list  = list(ks.keys())
    inertias = [v["inertia"] for v in ks.values()]
    ax.plot(ks_list, inertias, "o-", color="#6C63FF", linewidth=2)
    ax.set_title(f"Codo - {model_name}", fontsize=11, color="#6C63FF")
    ax.set_xlabel("K"); ax.set_ylabel("Inertia")
    ax.grid(True, linestyle="--", alpha=0.4); ax.set_xticks(ks_list)
    ax.set_facecolor("#1a1a2e")
    for sp in ax.spines.values(): sp.set_edgecolor("#444466")

# Fila 1: silhouette + DB comparativos
ax_sil = fig.add_subplot(gs[1, 0:2])
ax_db  = fig.add_subplot(gs[1, 2:4])

for (model_name, ks), col in zip(results.items(), colors_models):
    ks_list = list(ks.keys())
    sils = [v["silhouette"] for v in ks.values()]
    dbs  = [v["db"] for v in ks.values()]
    ax_sil.plot(ks_list, sils, "o-", label=model_name, color=col, linewidth=2)
    ax_db.plot(ks_list, dbs,  "s-", label=model_name, color=col, linewidth=2)

for ax, title, ylabel in [
    (ax_sil, "Silhouette Score", "Score (mayor = mejor)"),
    (ax_db,  "Davies-Bouldin",   "Score (menor = mejor)"),
]:
    ax.set_title(title, fontsize=11, color="#43D9AD")
    ax.set_xlabel("K"); ax.set_ylabel(ylabel)
    ax.legend(facecolor="#1a1a2e", edgecolor="#444466", fontsize=8)
    ax.grid(True, linestyle="--", alpha=0.4); ax.set_xticks(list(K_VALUES))
    ax.set_facecolor("#1a1a2e")
    for sp in ax.spines.values(): sp.set_edgecolor("#444466")

# Fila 2: scatter del mejor K para cada modelo
for col_idx, (model_name, ks) in enumerate(results.items()):
    best_k = max(ks, key=lambda k: ks[k]["silhouette"])
    v = ks[best_k]
    ax = fig.add_subplot(gs[2, col_idx * 2: col_idx * 2 + 2])
    labels = v["labels"]
    for cluster_id in np.unique(labels):
        mask = labels == cluster_id
        ax.scatter(X_pca[mask, 0], X_pca[mask, 1],
                   c=PALETTE[cluster_id % len(PALETTE)],
                   s=1.5, alpha=0.3, linewidths=0, rasterized=True)
    ax.set_title(f"{model_name} - Mejor K={best_k}\nSil={v['silhouette']:.4f}",
                 fontsize=10, color="#FF6584")
    ax.set_xlabel(f"PC1 ({var_exp[0]:.1f}%)", fontsize=8)
    ax.set_ylabel(f"PC2 ({var_exp[1]:.1f}%)", fontsize=8)
    ax.grid(True, linestyle="--", alpha=0.3)
    ax.set_facecolor("#1a1a2e")
    for sp in ax.spines.values(): sp.set_edgecolor("#444466")

plt.savefig(os.path.join(OUTPUT_DIR, "05_dashboard_final.png"), dpi=150,
            bbox_inches="tight", facecolor=fig.get_facecolor())
plt.close()
print("  v 05_dashboard_final.png")

# ════════════════════════════════════════════════════════════
# 8.  RESUMEN FINAL
# ════════════════════════════════════════════════════════════
print("\n" + "=" * 60)
print("  8. RESUMEN FINAL")
print("=" * 60)
for model_name, ks in results.items():
    best_k = max(ks, key=lambda k: ks[k]["silhouette"])
    v = ks[best_k]
    print(f"  {model_name:25s} -> Mejor K={best_k} | Silhouette={v['silhouette']:.4f} | DB={v['db']:.4f}")

print(f"\n  Todos los graficos guardados en:\n  {OUTPUT_DIR}")
print("\n  PIPELINE COMPLETADO.\n")
