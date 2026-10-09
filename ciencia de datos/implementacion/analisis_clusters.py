# ============================================================
#  ANÁLISIS DE CLUSTERS — Secondary Mushroom Dataset
#  Objetivo: Encontrar la combinación de columnas y K=5/6
#  que produzca clusters más uniformes e interpretables
# ============================================================

import os
import warnings
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score, davies_bouldin_score
from sklearn.compose import ColumnTransformer

warnings.filterwarnings("ignore")

DATA_PATH  = r"d:\Cathy\Documentos\ciencia de datos\recursos\secondary_data.csv"
OUTPUT_DIR = r"d:\Cathy\Documentos\ciencia de datos\implementacion\graficos_analisis"
os.makedirs(OUTPUT_DIR, exist_ok=True)

PALETTE = [
    "#6C63FF", "#FF6584", "#43D9AD", "#FFB347", "#5EB8FF", "#FF6F61"
]

plt.rcParams.update({
    "font.family":      "DejaVu Sans",
    "axes.facecolor":   "#1a1a2e",
    "figure.facecolor": "#0f0f1a",
    "axes.edgecolor":   "#444466",
    "axes.labelcolor":  "#e0e0ff",
    "xtick.color":      "#a0a0cc",
    "ytick.color":      "#a0a0cc",
    "text.color":       "#e0e0ff",
    "grid.color":       "#2a2a4a",
    "grid.linewidth":   0.5,
})

# ════════════════════════════════════════════════════════════
# 1. CARGA Y LIMPIEZA BASE
# ════════════════════════════════════════════════════════════
df_raw = pd.read_csv(DATA_PATH, sep=";")
df = df_raw.copy()

target = df["class"].copy()
df = df.drop(columns=["class"])
df = df.drop_duplicates()

# Eliminar columnas con >70% nulos
null_pct = df.isnull().sum() / len(df) * 100
drop_cols = null_pct[null_pct > 70].index.tolist()
df = df.drop(columns=drop_cols)

# Imputar restantes
num_cols_base = df.select_dtypes(include=["float64", "int64"]).columns.tolist()
cat_cols_base = df.select_dtypes(include="object").columns.tolist()
for col in num_cols_base:
    df[col] = df[col].fillna(df[col].median())
for col in cat_cols_base:
    df[col] = df[col].fillna(df[col].mode()[0])

print(f"Dataset base: {df.shape[0]:,} filas x {df.shape[1]} columnas")
print(f"Columnas disponibles: {df.columns.tolist()}\n")

# ════════════════════════════════════════════════════════════
# 2. DEFINICIÓN DE CONJUNTOS DE COLUMNAS A PROBAR
# ════════════════════════════════════════════════════════════
# Columnas disponibles tras limpieza:
# Numéricas  : cap-diameter, stem-height, stem-width
# Categóricas: cap-shape, cap-surface, cap-color,
#              does-bruise-or-bleed, gill-attachment, gill-spacing,
#              gill-color, stem-surface, stem-color,
#              has-ring, ring-type, habitat, season

COLUMN_SETS = {
    # A: Todas las columnas disponibles (16 cols)
    "A_todas_16": {
        "desc": "Todas las columnas (16)",
        "cols": df.columns.tolist()
    },
    # B: Sin variables ambientales — solo morfología (14 cols)
    "B_morfologicas_14": {
        "desc": "Sin habitat y season — morfología pura (14)",
        "cols": [c for c in df.columns if c not in ["habitat", "season"]]
    },
    # C: Solo características del sombrero + tallo + láminas (13 cols)
    "C_sombrero_tallo_13": {
        "desc": "Sombrero + Tallo + Láminas (13)",
        "cols": [
            "cap-diameter", "cap-shape", "cap-surface", "cap-color",
            "stem-height", "stem-width", "stem-color", "stem-surface",
            "gill-color", "gill-attachment", "gill-spacing",
            "has-ring", "ring-type"
        ]
    },
    # D: Las 11 columnas más informativas morfológicamente
    "D_clave_11": {
        "desc": "11 columnas clave morfológicas",
        "cols": [
            "cap-diameter", "cap-shape", "cap-color",
            "stem-height", "stem-width", "stem-color",
            "gill-color", "gill-attachment",
            "does-bruise-or-bleed", "has-ring", "ring-type"
        ]
    },
    # E: Forma + Color + Tamaño (11 cols, enfoque visual)
    "E_visual_11": {
        "desc": "11 columnas visuales: forma, color, tamaño",
        "cols": [
            "cap-diameter", "cap-shape", "cap-surface", "cap-color",
            "stem-height", "stem-width",
            "gill-color", "gill-spacing",
            "stem-color", "has-ring", "habitat"
        ]
    },
}

# ════════════════════════════════════════════════════════════
# 3. PIPELINE: PARA CADA CONJUNTO Y K=5,6 → MÉTRICAS + ANÁLISIS
# ════════════════════════════════════════════════════════════
K_VALUES   = [5, 6]
all_results = {}  # {set_name: {k: {labels, sil, db, X_pca}}}
metrics_rows = []

print("=" * 65)
print("  COMPARATIVA DE CONJUNTOS DE COLUMNAS  (K=5 y K=6)")
print("=" * 65)

for set_name, set_info in COLUMN_SETS.items():
    cols = set_info["cols"]
    # asegurar que todas las columnas existen
    cols = [c for c in cols if c in df.columns]
    df_sub = df[cols].copy()

    num_c = df_sub.select_dtypes(include=["float64", "int64"]).columns.tolist()
    cat_c = df_sub.select_dtypes(include="object").columns.tolist()

    pre = ColumnTransformer([
        ("num", StandardScaler(), num_c),
        ("cat", OneHotEncoder(handle_unknown="ignore", sparse_output=False), cat_c)
    ])
    X = pre.fit_transform(df_sub)
    pca = PCA(n_components=2, random_state=42)
    X_pca = pca.fit_transform(X)
    var_exp = pca.explained_variance_ratio_ * 100

    all_results[set_name] = {
        "desc": set_info["desc"],
        "cols": cols,
        "num_c": num_c,
        "cat_c": cat_c,
        "df_sub": df_sub,
        "X": X,
        "X_pca": X_pca,
        "var_exp": var_exp,
        "kmeans": {}
    }

    print(f"\n  [{set_name}] {set_info['desc']}")
    print(f"  Columnas ({len(cols)}): {cols}")

    for k in K_VALUES:
        km = KMeans(n_clusters=k, random_state=42, n_init=15, max_iter=500)
        labels = km.fit_predict(X)
        sil = silhouette_score(X_pca, labels, sample_size=10_000, random_state=42)
        db  = davies_bouldin_score(X_pca, labels)

        # tamaño de cada cluster (uniformidad)
        sizes    = pd.Series(labels).value_counts().sort_index()
        pct      = (sizes / len(labels) * 100).round(1)
        std_size = pct.std()

        all_results[set_name]["kmeans"][k] = {
            "labels":   labels,
            "sil":      sil,
            "db":       db,
            "sizes":    sizes,
            "pct":      pct,
            "std_size": std_size,
        }
        metrics_rows.append({
            "Conjunto": set_name,
            "Descripcion": set_info["desc"],
            "N_cols": len(cols),
            "K": k,
            "Silhouette": round(sil, 4),
            "DB": round(db, 4),
            "StdTamano_%": round(std_size, 2),
        })
        dist = "  |  ".join([f"C{i}:{p:.0f}%" for i, p in pct.items()])
        print(f"    K={k} | Sil={sil:.4f} | DB={db:.4f} | StdTam={std_size:.1f}% | [{dist}]")

# ════════════════════════════════════════════════════════════
# 4. TABLA RESUMEN COMPARATIVA
# ════════════════════════════════════════════════════════════
df_met = pd.DataFrame(metrics_rows)
print("\n" + "=" * 65)
print("  TABLA RESUMEN")
print("=" * 65)
print(df_met.to_string(index=False))
df_met.to_csv(os.path.join(OUTPUT_DIR, "comparativa_conjuntos.csv"), index=False)

# mejor configuración: mayor Silhouette + menor StdTamaño (más uniforme)
df_met["score_global"] = df_met["Silhouette"] - df_met["StdTamano_%"] * 0.01
best_row = df_met.loc[df_met["score_global"].idxmax()]
print(f"\n  >> MEJOR CONFIGURACIÓN: {best_row['Conjunto']} con K={int(best_row['K'])}")
print(f"     Silhouette={best_row['Silhouette']} | DB={best_row['DB']} | StdTam={best_row['StdTamano_%']}%")

# ════════════════════════════════════════════════════════════
# 5. ANÁLISIS DE PERFILES DE CLUSTER (mejor configuración)
# ════════════════════════════════════════════════════════════
best_set = best_row["Conjunto"]
best_k   = int(best_row["K"])
print(f"\n{'=' * 65}")
print(f"  PERFIL DE CLUSTERS — {best_set}  K={best_k}")
print(f"{'=' * 65}")

best_info   = all_results[best_set]
best_labels = best_info["kmeans"][best_k]["labels"]
df_analisis = best_info["df_sub"].copy()
df_analisis["cluster"] = best_labels

# Nombres de clusters basados en características dominantes
CLUSTER_NAMES = {}
profile_rows  = []

for cid in sorted(df_analisis["cluster"].unique()):
    grp = df_analisis[df_analisis["cluster"] == cid]

    # Rasgos dominantes
    rasgos = []
    for col in best_info["num_c"]:
        val = grp[col].mean()
        ref = df_analisis[col].mean()
        if val > ref * 1.15:
            rasgos.append(f"{col}=GRANDE")
        elif val < ref * 0.85:
            rasgos.append(f"{col}=PEQUEÑO")

    for col in best_info["cat_c"]:
        moda     = grp[col].mode()[0]
        freq     = (grp[col] == moda).sum() / len(grp)
        freq_ref = (df_analisis[col] == moda).sum() / len(df_analisis)
        if freq > freq_ref * 1.2 and freq > 0.35:
            rasgos.append(f"{col}={moda}({freq:.0%})")

    pct_size = len(grp) / len(df_analisis) * 100

    # Nombre automático: combinando los 3 rasgos más distintivos
    nombre = "Hongo " + " / ".join(rasgos[:3]) if rasgos else f"Cluster {cid}"
    CLUSTER_NAMES[cid] = nombre

    print(f"\n  Cluster {cid} ({pct_size:.1f}% del dataset = {len(grp):,} hongos)")
    print(f"  Nombre sugerido: {nombre}")
    print(f"  Rasgos dominantes: {rasgos[:6]}")

    for col in best_info["num_c"]:
        profile_rows.append({"Cluster": cid, "Columna": col, "Valor": f"{grp[col].mean():.2f} (media)"})
    for col in best_info["cat_c"]:
        moda = grp[col].mode()[0]
        freq = (grp[col] == moda).sum() / len(grp)
        profile_rows.append({"Cluster": cid, "Columna": col, "Valor": f"{moda} ({freq:.0%})"})

df_profile = pd.DataFrame(profile_rows)
df_profile.to_csv(os.path.join(OUTPUT_DIR, f"perfil_clusters_{best_set}_K{best_k}.csv"), index=False)
print(f"\n  Perfil guardado en: perfil_clusters_{best_set}_K{best_k}.csv")

# ════════════════════════════════════════════════════════════
# 6. GRÁFICOS
# ════════════════════════════════════════════════════════════

# ── 6a. Scatter PCA por cada conjunto (K=5 y K=6, 2 columnas) ─
for set_name, info in all_results.items():
    X_pca   = info["X_pca"]
    var_exp = info["var_exp"]
    fig, axes = plt.subplots(1, 2, figsize=(16, 6))
    fig.suptitle(f"Clustering PCA\n{info['desc']}", fontsize=14,
                 fontweight="bold", color="#e0e0ff")
    for ax, k in zip(axes, K_VALUES):
        km_res = info["kmeans"][k]
        labels = km_res["labels"]
        for cid in np.unique(labels):
            mask = labels == cid
            ax.scatter(X_pca[mask, 0], X_pca[mask, 1],
                       c=PALETTE[cid % len(PALETTE)], s=2,
                       alpha=0.35, linewidths=0, rasterized=True)
        patches = [mpatches.Patch(color=PALETTE[i % len(PALETTE)],
                   label=f"C{i} ({km_res['pct'][i]:.0f}%)")
                   for i in range(k)]
        ax.legend(handles=patches, fontsize=8, loc="upper right",
                  facecolor="#1a1a2e", edgecolor="#444466")
        ax.set_title(f"K={k} | Sil={km_res['sil']:.3f} | DB={km_res['db']:.3f}",
                     fontsize=11, color="#6C63FF")
        ax.set_xlabel(f"PC1 ({var_exp[0]:.1f}%)", fontsize=9)
        ax.set_ylabel(f"PC2 ({var_exp[1]:.1f}%)", fontsize=9)
        ax.grid(True, linestyle="--", alpha=0.3)
    plt.tight_layout()
    fname = f"scatter_{set_name}.png"
    plt.savefig(os.path.join(OUTPUT_DIR, fname), dpi=150, bbox_inches="tight",
                facecolor=fig.get_facecolor())
    plt.close()
    print(f"  v {fname}")

# ── 6b. Heatmap de perfiles del mejor conjunto ────────────────
print("\n  Generando heatmap de perfiles...")
best_labels_arr = all_results[best_set]["kmeans"][best_k]["labels"]
df_heat = all_results[best_set]["df_sub"].copy()
df_heat["cluster"] = best_labels_arr

# codificar categóricas numéricamente para el heatmap
df_heat_enc = df_heat.copy()
for col in all_results[best_set]["cat_c"]:
    df_heat_enc[col] = pd.Categorical(df_heat_enc[col]).codes

profile_mean = df_heat_enc.groupby("cluster").mean()
profile_norm = (profile_mean - profile_mean.mean()) / (profile_mean.std() + 1e-9)

fig, ax = plt.subplots(figsize=(max(12, len(profile_norm.columns) * 0.7), 5))
im = ax.imshow(profile_norm.values, aspect="auto", cmap="RdYlGn",
               vmin=-2, vmax=2)
ax.set_xticks(range(len(profile_norm.columns)))
ax.set_xticklabels(profile_norm.columns, rotation=45, ha="right", fontsize=8)
ax.set_yticks(range(best_k))
ax.set_yticklabels([f"C{i}" for i in range(best_k)], fontsize=10)
plt.colorbar(im, ax=ax, label="Z-score (relativo al promedio global)")
ax.set_title(f"Heatmap de Perfiles por Cluster\n{all_results[best_set]['desc']} — K={best_k}",
             fontsize=13, fontweight="bold", color="#e0e0ff")
plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, f"heatmap_perfil_{best_set}_K{best_k}.png"),
            dpi=150, bbox_inches="tight", facecolor=fig.get_facecolor())
plt.close()
print(f"  v heatmap_perfil_{best_set}_K{best_k}.png")

# ── 6c. Barras de distribución de tamaños ────────────────────
fig, axes = plt.subplots(len(COLUMN_SETS), 2,
                         figsize=(14, 3.5 * len(COLUMN_SETS)))
fig.suptitle("Distribución de tamaño de clusters (uniformidad)",
             fontsize=15, fontweight="bold", color="#e0e0ff", y=1.01)

for row_idx, (set_name, info) in enumerate(all_results.items()):
    for col_idx, k in enumerate(K_VALUES):
        ax  = axes[row_idx, col_idx]
        pct = info["kmeans"][k]["pct"]
        bars = ax.bar(range(k), pct.values,
                      color=[PALETTE[i % len(PALETTE)] for i in range(k)],
                      edgecolor="#0f0f1a", linewidth=0.5)
        for bar, p in zip(bars, pct.values):
            ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.5,
                    f"{p:.1f}%", ha="center", va="bottom", fontsize=8, color="#e0e0ff")
        ax.axhline(100/k, color="#FF6584", linestyle="--", linewidth=1.2,
                   label=f"Ideal ({100/k:.1f}%)")
        ax.set_title(f"{info['desc'][:40]}\nK={k} | StdTam={info['kmeans'][k]['std_size']:.1f}%",
                     fontsize=9, color="#43D9AD")
        ax.set_xlabel("Cluster")
        ax.set_ylabel("% del dataset")
        ax.legend(fontsize=7, facecolor="#1a1a2e", edgecolor="#444466")
        ax.set_xticks(range(k))
        ax.set_xticklabels([f"C{i}" for i in range(k)])
        ax.set_facecolor("#1a1a2e")
        for sp in ax.spines.values(): sp.set_edgecolor("#444466")

plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, "barras_uniformidad.png"),
            dpi=150, bbox_inches="tight", facecolor=fig.get_facecolor())
plt.close()
print("  v barras_uniformidad.png")

# ── 6d. Scatter final con nombres de cluster (mejor config) ───
fig, axes = plt.subplots(1, 2, figsize=(18, 7))
fig.suptitle(f"Clusters con nombres — {all_results[best_set]['desc']}",
             fontsize=14, fontweight="bold", color="#e0e0ff")

X_pca_best = all_results[best_set]["X_pca"]
var_best   = all_results[best_set]["var_exp"]

for ax, k in zip(axes, K_VALUES):
    labels = all_results[best_set]["kmeans"][k]["labels"]
    for cid in np.unique(labels):
        mask = labels == cid
        ax.scatter(X_pca_best[mask, 0], X_pca_best[mask, 1],
                   c=PALETTE[cid % len(PALETTE)], s=2,
                   alpha=0.4, linewidths=0, rasterized=True)
    # Re-calcular nombres para este K
    df_tmp = all_results[best_set]["df_sub"].copy()
    df_tmp["cluster"] = labels
    patches = []
    for cid in range(k):
        grp    = df_tmp[df_tmp["cluster"] == cid]
        rasgos = []
        for col in all_results[best_set]["cat_c"]:
            moda = grp[col].mode()[0]
            freq = (grp[col] == moda).sum() / len(grp)
            if freq > 0.5:
                rasgos.append(f"{moda}")
        nombre_corto = "/".join(rasgos[:2]) if rasgos else f"C{cid}"
        pct_c = all_results[best_set]["kmeans"][k]["pct"][cid]
        patches.append(mpatches.Patch(color=PALETTE[cid % len(PALETTE)],
                       label=f"C{cid} {nombre_corto} ({pct_c:.0f}%)"))
    ax.legend(handles=patches, fontsize=7.5, loc="upper right",
              facecolor="#1a1a2e", edgecolor="#444466")
    sil = all_results[best_set]["kmeans"][k]["sil"]
    ax.set_title(f"K={k} | Silhouette={sil:.4f}", fontsize=12, color="#6C63FF")
    ax.set_xlabel(f"PC1 ({var_best[0]:.1f}%)", fontsize=9)
    ax.set_ylabel(f"PC2 ({var_best[1]:.1f}%)", fontsize=9)
    ax.grid(True, linestyle="--", alpha=0.3)

plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, f"scatter_nombrado_{best_set}.png"),
            dpi=150, bbox_inches="tight", facecolor=fig.get_facecolor())
plt.close()
print(f"  v scatter_nombrado_{best_set}.png")

print(f"\n  Todos los graficos en: {OUTPUT_DIR}")
print("  ANALISIS COMPLETADO.\n")
