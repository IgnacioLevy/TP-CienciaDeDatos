# -*- coding: utf-8 -*-
import os, sys, json
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN
from pptx.enum.shapes import MSO_SHAPE
from pptx.dml.color import RGBColor

BASE = r"E:\cosas\facu\Ciencia de Datos\ciencia de datos-20261008T230846Z-1-001\ciencia de datos"
ENTREGA_DIR = os.path.join(BASE, "implementacion", "entrega2")
PPTX_PATH = os.path.join(ENTREGA_DIR, "presentacion_entrega2.pptx")
META_PATH = os.path.join(ENTREGA_DIR, "_meta.json")

with open(META_PATH, "r", encoding="utf-8") as f:
    meta = json.load(f)

# Light Mode Colors Palette
BG_COLOR       = RGBColor(248, 250, 252)   # #F8FAFC Soft Light Background
CARD_BG        = RGBColor(255, 255, 255)   # #FFFFFF Crisp White Card
CARD_BG_ALT    = RGBColor(241, 245, 249)   # #F1F5F9 Soft Tint Box
BORDER_COLOR   = RGBColor(203, 213, 225)   # #CBD5E1 Neutral Slate Border

# Accents
ACCENT_PURPLE  = RGBColor(79, 70, 229)     # #4F46E5 Vibrant Indigo
ACCENT_CYAN    = RGBColor(5, 150, 105)     # #059669 Emerald Green
ACCENT_PINK    = RGBColor(225, 29, 72)     # #E11D48 Coral Red
ACCENT_YELLOW  = RGBColor(217, 119, 6)     # #D97706 Warm Amber
ACCENT_BLUE    = RGBColor(2, 132, 199)     # #0284C7 Sky Blue

# Typography Colors (High Contrast)
TEXT_TITLE     = RGBColor(15, 23, 42)      # #0F172A Deep Navy / Almost Black
TEXT_BODY      = RGBColor(30, 41, 59)      # #1E293B High Contrast Slate
TEXT_MUTED     = RGBColor(71, 85, 105)     # #475569 Slate Muted
TEXT_SUBTLE    = RGBColor(100, 116, 139)   # #64748B Secondary Info

# Light Images
IMG_PIPELINE     = os.path.join(ENTREGA_DIR, "img_pipeline_light.png")
IMG_NULOS        = os.path.join(ENTREGA_DIR, "img_nulos_light.png")
IMG_KMEANS_DIAG  = os.path.join(ENTREGA_DIR, "img_kmeans_diagrama_light.png")
IMG_METRICAS     = os.path.join(ENTREGA_DIR, "img_metricas_light.png")
IMG_SCATTER_COMP = os.path.join(ENTREGA_DIR, "img_scatter_comp_light.png")
IMG_SCATTER_K6   = os.path.join(ENTREGA_DIR, "img_scatter_k6_light.png")
IMG_BARRAS       = os.path.join(ENTREGA_DIR, "img_barras_k6_light.png")


def set_slide_background(slide):
    bg = slide.background
    fill = bg.fill
    fill.solid()
    fill.fore_color.rgb = BG_COLOR

def add_header(slide, title, category="SEGUNDA ENTREGA | CIENCIA DE DATOS"):
    tb = slide.shapes.add_textbox(Inches(0.8), Inches(0.35), Inches(11.7), Inches(1.15))
    tf = tb.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0
    
    p0 = tf.paragraphs[0]
    p0.text = category.upper()
    p0.font.size = Pt(11.5)
    p0.font.bold = True
    p0.font.color.rgb = ACCENT_PURPLE
    
    p1 = tf.add_paragraph()
    p1.text = title
    p1.font.size = Pt(25)
    p1.font.bold = True
    p1.font.color.rgb = TEXT_TITLE
    p1.space_before = Pt(2)

def create_card(slide, left, top, width, height, bg_color=CARD_BG, border_color=BORDER_COLOR):
    shape = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
    shape.fill.solid()
    shape.fill.fore_color.rgb = bg_color
    if border_color:
        shape.line.color.rgb = border_color
        shape.line.width = Pt(1.4)
    else:
        shape.line.fill.background()
    return shape


def build_presentation():
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank_layout = prs.slide_layouts[6]

    # =========================================================================
    # SLIDE 1: PORTADA (LIGHT MODE)
    # =========================================================================
    slide1 = prs.slides.add_slide(blank_layout)
    set_slide_background(slide1)

    # Hero Main Card
    create_card(slide1, Inches(0.9), Inches(0.8), Inches(11.533), Inches(5.9), bg_color=CARD_BG, border_color=ACCENT_PURPLE)

    # Category Pill
    pill = slide1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(1.5), Inches(1.3), Inches(3.6), Inches(0.48))
    pill.fill.solid()
    pill.fill.fore_color.rgb = RGBColor(238, 242, 255)
    pill.line.color.rgb = ACCENT_PURPLE
    ptf = pill.text_frame
    ptf.margin_left = ptf.margin_top = ptf.margin_right = ptf.margin_bottom = 0
    pp = ptf.paragraphs[0]
    pp.text = "APRENDIZAJE NO SUPERVISADO"
    pp.font.size = Pt(12)
    pp.font.bold = True
    pp.font.color.rgb = ACCENT_PURPLE
    pp.alignment = PP_ALIGN.CENTER

    # Main Titles (Enlarged)
    tb_title = slide1.shapes.add_textbox(Inches(1.5), Inches(1.95), Inches(10.3), Inches(2.5))
    ttf = tb_title.text_frame
    ttf.word_wrap = True
    ttf.margin_left = ttf.margin_top = ttf.margin_right = ttf.margin_bottom = 0

    p_t1 = ttf.paragraphs[0]
    p_t1.text = "Clusterización de Hongos con K-Means"
    p_t1.font.size = Pt(40)
    p_t1.font.bold = True
    p_t1.font.color.rgb = TEXT_TITLE

    p_t2 = ttf.add_paragraph()
    p_t2.text = "Identificación de Morfotipos en el Secondary Mushroom Dataset"
    p_t2.font.size = Pt(20)
    p_t2.font.bold = True
    p_t2.font.color.rgb = ACCENT_CYAN
    p_t2.space_before = Pt(8)

    p_t3 = ttf.add_paragraph()
    p_t3.text = "Segunda Entrega de Trabajo Práctico | Ciencia de Datos"
    p_t3.font.size = Pt(15)
    p_t3.font.color.rgb = TEXT_MUTED
    p_t3.space_before = Pt(6)

    # Key Stat Badges (Enlarged)
    stats = [
        ("60.923", "Especímenes Limpios", ACCENT_PURPLE),
        ("13", "Variables Morfológicas", ACCENT_CYAN),
        ("K = 6", "Clusters Seleccionados", ACCENT_YELLOW),
        ("0.8425", "Índice Davies-Bouldin", ACCENT_PINK)
    ]
    stat_w = Inches(2.4)
    stat_gap = Inches(0.35)
    for i, (val, lbl, col) in enumerate(stats):
        bx = Inches(1.5) + i * (stat_w + stat_gap)
        by = Inches(4.75)
        create_card(slide1, bx, by, stat_w, Inches(1.4), bg_color=CARD_BG_ALT, border_color=col)
        tb_s = slide1.shapes.add_textbox(bx, by + Inches(0.18), stat_w, Inches(1.1))
        stf = tb_s.text_frame
        stf.word_wrap = True
        stf.margin_left = stf.margin_top = stf.margin_right = stf.margin_bottom = 0
        sp1 = stf.paragraphs[0]
        sp1.text = val
        sp1.font.size = Pt(28)
        sp1.font.bold = True
        sp1.font.color.rgb = col
        sp1.alignment = PP_ALIGN.CENTER
        sp2 = stf.add_paragraph()
        sp2.text = lbl
        sp2.font.size = Pt(12)
        sp2.font.bold = True
        sp2.font.color.rgb = TEXT_BODY
        sp2.alignment = PP_ALIGN.CENTER
        sp2.space_before = Pt(2)

    # =========================================================================
    # SLIDE 2: INTRODUCCIÓN Y RESUMEN DEL PROYECTO
    # =========================================================================
    slide2 = prs.slides.add_slide(blank_layout)
    set_slide_background(slide2)
    add_header(slide2, "Introducción y Visión General del Proyecto", "FASE PRELIMINAR")

    # Left Card: Propósito No Supervisado
    create_card(slide2, Inches(0.8), Inches(1.55), Inches(5.7), Inches(2.55))
    tb_c1 = slide2.shapes.add_textbox(Inches(1.05), Inches(1.7), Inches(5.2), Inches(2.25))
    tf1 = tb_c1.text_frame; tf1.word_wrap = True
    p = tf1.paragraphs[0]
    p.text = "🎯 Propósito de la Segunda Entrega"
    p.font.size = Pt(16); p.font.bold = True; p.font.color.rgb = ACCENT_PURPLE
    p2 = tf1.add_paragraph()
    p2.text = "• Agrupamiento no supervisado mediante K-Means sobre el Secondary Mushroom Dataset.\n" \
              "• Particionar los hongos según sus rasgos morfológicos externos observables.\n" \
              "• Excluir intencionalmente la variable 'class' (comestible/venenoso) para simular la catalogación taxonómica botánica real."
    p2.font.size = Pt(12.5); p2.font.color.rgb = TEXT_BODY; p2.space_before = Pt(8)

    # Right Card: Objetivos Analíticos
    create_card(slide2, Inches(6.8), Inches(1.55), Inches(5.7), Inches(2.55))
    tb_c2 = slide2.shapes.add_textbox(Inches(7.05), Inches(1.7), Inches(5.2), Inches(2.25))
    tf2 = tb_c2.text_frame; tf2.word_wrap = True
    p = tf2.paragraphs[0]
    p.text = "🔬 Metas Analíticas Concretas"
    p.font.size = Pt(16); p.font.bold = True; p.font.color.rgb = ACCENT_CYAN
    p2 = tf2.add_paragraph()
    p2.text = "• Depurar el dataset original (>61k filas), eliminando registros duplicados y dimensiones vacías.\n" \
              "• Comparar modelos con diferente número de clusters (K=5 vs K=6) usando Silhouette y Davies-Bouldin.\n" \
              "• Nombrar y caracterizar cada cluster descubierto en base a su perfil fenotípico dominante."
    p2.font.size = Pt(12.5); p2.font.color.rgb = TEXT_BODY; p2.space_before = Pt(8)

    # Bottom Area: Flowchart Pipeline
    create_card(slide2, Inches(0.8), Inches(4.3), Inches(11.7), Inches(2.85))
    tb_pl = slide2.shapes.add_textbox(Inches(1.05), Inches(4.45), Inches(11.2), Inches(0.35))
    pl_p = tb_pl.text_frame.paragraphs[0]
    pl_p.text = "PIPELINE INTEGRAL DE EJECUCIÓN (6 PASOS METODOLÓGICOS)"
    pl_p.font.size = Pt(12.5); pl_p.font.bold = True; pl_p.font.color.rgb = ACCENT_YELLOW

    if os.path.exists(IMG_PIPELINE):
        slide2.shapes.add_picture(IMG_PIPELINE, Inches(0.95), Inches(4.85), width=Inches(11.4))

    # =========================================================================
    # SLIDE 3: 1) CAMBIOS ENTRE EL DATASET ORIGINAL Y EL ACTUAL
    # =========================================================================
    slide3 = prs.slides.add_slide(blank_layout)
    set_slide_background(slide3)
    add_header(slide3, "1. Transformaciones: Dataset Original vs Actual", "TRANSFORMACIÓN DE DATOS")

    col_w = Inches(3.64)
    gap = Inches(0.39)

    # Card 1: Filas
    create_card(slide3, Inches(0.8), Inches(1.55), col_w, Inches(5.5), border_color=ACCENT_PURPLE)
    tb = slide3.shapes.add_textbox(Inches(1.0), Inches(1.75), Inches(3.24), Inches(5.1))
    tf = tb.text_frame; tf.word_wrap = True
    p = tf.paragraphs[0]; p.text = "FILAS & REGISTROS"; p.font.size = Pt(13); p.font.bold = True; p.font.color.rgb = ACCENT_PURPLE
    p = tf.add_paragraph(); p.text = "61.069  ➔  60.923"; p.font.size = Pt(21); p.font.bold = True; p.font.color.rgb = TEXT_TITLE; p.space_before = Pt(4)
    p = tf.add_paragraph()
    p.text = "\n• -146 Duplicados Exactos:\nSe eliminaron observaciones idénticas que distorsionaban el centro de gravedad de los centroides euclídeos.\n\n• Integridad Muestral:\nSe conservó el 99.76% del volumen original sin descartar familias ni géneros de hongos."
    p.font.size = Pt(12.5); p.font.color.rgb = TEXT_BODY

    # Card 2: Columnas
    create_card(slide3, Inches(0.8) + col_w + gap, Inches(1.55), col_w, Inches(5.5), border_color=ACCENT_CYAN)
    tb = slide3.shapes.add_textbox(Inches(1.0) + col_w + gap, Inches(1.75), Inches(3.24), Inches(5.1))
    tf = tb.text_frame; tf.word_wrap = True
    p = tf.paragraphs[0]; p.text = "COLUMNAS Y VARIABLES"; p.font.size = Pt(13); p.font.bold = True; p.font.color.rgb = ACCENT_CYAN
    p = tf.add_paragraph(); p.text = "21 vars  ➔  13 morfo"; p.font.size = Pt(21); p.font.bold = True; p.font.color.rgb = TEXT_TITLE; p.space_before = Pt(4)
    p = tf.add_paragraph()
    p.text = "\n• Exclusión de 'class':\nDescarte de etiqueta supervisada (comestible vs venenoso).\n\n• Poda de 4 columnas críticas:\nstem-root, veil-type, veil-color y spore-print (>70% vacías).\n\n• Variables de contexto fuera:\nhabitat y season removidas para aislar la fisonomía física."
    p.font.size = Pt(12.5); p.font.color.rgb = TEXT_BODY

    # Card 3: 13 Variables
    create_card(slide3, Inches(0.8) + (col_w + gap)*2, Inches(1.55), col_w, Inches(5.5), border_color=ACCENT_YELLOW)
    tb = slide3.shapes.add_textbox(Inches(1.0) + (col_w + gap)*2, Inches(1.75), Inches(3.24), Inches(5.1))
    tf = tb.text_frame; tf.word_wrap = True
    p = tf.paragraphs[0]; p.text = "LAS 13 MORFOLÓGICAS"; p.font.size = Pt(13); p.font.bold = True; p.font.color.rgb = ACCENT_YELLOW
    p = tf.add_paragraph(); p.text = "Anatomía del Hongo"; p.font.size = Pt(21); p.font.bold = True; p.font.color.rgb = TEXT_TITLE; p.space_before = Pt(4)
    p = tf.add_paragraph()
    p.text = "\n🍄 Sombrero (Pileus):\ncap-diameter, cap-shape, cap-surface, cap-color.\n\n🌱 Pie (Estípite):\nstem-height, stem-width, stem-color, stem-surface.\n\n🍂 Láminas (Himenio):\ngill-color, gill-attachment, gill-spacing.\n\n💍 Anillo (Velo):\nhas-ring, ring-type."
    p.font.size = Pt(12); p.font.color.rgb = TEXT_BODY

    # =========================================================================
    # SLIDE 4: 2) CÓMO TRATAMOS CON LOS DATOS NULOS
    # =========================================================================
    slide4 = prs.slides.add_slide(blank_layout)
    set_slide_background(slide4)
    add_header(slide4, "2. Tratamiento Riguroso de Datos Nulos", "CURACIÓN DE DATOS")

    # Left: Light Chart Image
    create_card(slide4, Inches(0.8), Inches(1.55), Inches(6.8), Inches(5.5))
    tb_img_t = slide4.shapes.add_textbox(Inches(1.05), Inches(1.7), Inches(6.3), Inches(0.35))
    tb_img_t.text_frame.paragraphs[0].text = "DIAGNÓSTICO DE VALORES NULOS POR VARIABLE"
    tb_img_t.text_frame.paragraphs[0].font.size = Pt(12); tb_img_t.text_frame.paragraphs[0].font.bold = True
    tb_img_t.text_frame.paragraphs[0].font.color.rgb = ACCENT_PINK

    if os.path.exists(IMG_NULOS):
        slide4.shapes.add_picture(IMG_NULOS, Inches(1.0), Inches(2.1), width=Inches(6.4))

    # Right: 3 Strategy Cards
    rw = Inches(4.6)
    rx = Inches(7.9)
    # Card 1: Poda
    create_card(slide4, rx, Inches(1.55), rw, Inches(1.7), border_color=ACCENT_PINK)
    tb = slide4.shapes.add_textbox(rx + Inches(0.2), Inches(1.7), rw - Inches(0.4), Inches(1.4))
    tf = tb.text_frame; tf.word_wrap = True
    p = tf.paragraphs[0]; p.text = "1. Poda Crítica (>70% Nulos)"; p.font.size = Pt(14); p.font.bold = True; p.font.color.rgb = ACCENT_PINK
    p = tf.add_paragraph()
    p.text = "Se eliminaron 4 columnas (stem-root 85%, veil-type 95%, veil-color 88%, spore-print 73%). Imputar con >70% de ausencia falsearía el espacio métrico."
    p.font.size = Pt(11.5); p.font.color.rgb = TEXT_BODY; p.space_before = Pt(4)

    # Card 2: Mediana
    create_card(slide4, rx, Inches(3.45), rw, Inches(1.7), border_color=ACCENT_CYAN)
    tb = slide4.shapes.add_textbox(rx + Inches(0.2), Inches(3.6), rw - Inches(0.4), Inches(1.4))
    tf = tb.text_frame; tf.word_wrap = True
    p = tf.paragraphs[0]; p.text = "2. Imputación por Mediana (Numéricas)"; p.font.size = Pt(14); p.font.bold = True; p.font.color.rgb = ACCENT_CYAN
    p = tf.add_paragraph()
    p.text = "Para cap-diameter, stem-height y stem-width (<2% nulos). La mediana protege el centroide de valores atípicos y distribuciones asimétricas."
    p.font.size = Pt(11.5); p.font.color.rgb = TEXT_BODY; p.space_before = Pt(4)

    # Card 3: Moda
    create_card(slide4, rx, Inches(5.35), rw, Inches(1.7), border_color=ACCENT_YELLOW)
    tb = slide4.shapes.add_textbox(rx + Inches(0.2), Inches(5.5), rw - Inches(0.4), Inches(1.4))
    tf = tb.text_frame; tf.word_wrap = True
    p = tf.paragraphs[0]; p.text = "3. Imputación por Moda (Categóricas)"; p.font.size = Pt(14); p.font.bold = True; p.font.color.rgb = ACCENT_YELLOW
    p = tf.add_paragraph()
    p.text = "Para cap-surface, stem-surface, gill-attachment (<19% nulos). Imputa la categoría morfológica dominante sin añadir clases inventadas."
    p.font.size = Pt(11.5); p.font.color.rgb = TEXT_BODY; p.space_before = Pt(4)

    # =========================================================================
    # SLIDE 5: 3) QUÉ SON LOS K-MEANS Y CÓMO FUNCIONA
    # =========================================================================
    slide5 = prs.slides.add_slide(blank_layout)
    set_slide_background(slide5)
    add_header(slide5, "3. Algoritmo K-Means: Concepto y Mecanismo", "FUNDAMENTO TEÓRICO")

    # Top Left: Definición
    create_card(slide5, Inches(0.8), Inches(1.55), Inches(5.9), Inches(2.25))
    tb = slide5.shapes.add_textbox(Inches(1.05), Inches(1.7), Inches(5.4), Inches(1.95))
    tf = tb.text_frame; tf.word_wrap = True
    p = tf.paragraphs[0]; p.text = "¿Qué es K-Means?"; p.font.size = Pt(16); p.font.bold = True; p.font.color.rgb = ACCENT_PURPLE
    p = tf.add_paragraph()
    p.text = "• Algoritmo de aprendizaje no supervisado de tipo particional.\n" \
              "• Objetivo: dividir N observaciones en K grupos disjuntos.\n" \
              "• Minimiza la inercia intra-cluster (WCSS):\n" \
              "   WCSS = ∑ ∑ ||x_i - μ_j||²\n" \
              "• Genera clusters compactos y cohesivos en el espacio métrico."
    p.font.size = Pt(12); p.font.color.rgb = TEXT_BODY; p.space_before = Pt(4)

    # Top Right: Ciclo de Convergencia
    create_card(slide5, Inches(7.0), Inches(1.55), Inches(5.5), Inches(2.25))
    tb = slide5.shapes.add_textbox(Inches(7.25), Inches(1.7), Inches(5.0), Inches(1.95))
    tf = tb.text_frame; tf.word_wrap = True
    p = tf.paragraphs[0]; p.text = "Ciclo de 4 Etapas"; p.font.size = Pt(16); p.font.bold = True; p.font.color.rgb = ACCENT_CYAN
    p = tf.add_paragraph()
    p.text = "1. Inicialización (k-means++): semillas dispersas con distancia probabilística.\n" \
              "2. Asignación: cada hongo va al centroide euclídeo más cercano.\n" \
              "3. Recálculo: los centroides se actualizan al promedio del cluster.\n" \
              "4. Convergencia: repite hasta variación nula (tol=1e-4)."
    p.font.size = Pt(12); p.font.color.rgb = TEXT_BODY; p.space_before = Pt(4)

    # Bottom: Diagram Image
    create_card(slide5, Inches(0.8), Inches(4.0), Inches(11.7), Inches(3.05))
    tb = slide5.shapes.add_textbox(Inches(1.05), Inches(4.1), Inches(11.2), Inches(0.35))
    tb.text_frame.paragraphs[0].text = "DIAGRAMA DEL PROCESO ITERATIVO DE K-MEANS"
    tb.text_frame.paragraphs[0].font.size = Pt(12); tb.text_frame.paragraphs[0].font.bold = True
    tb.text_frame.paragraphs[0].font.color.rgb = ACCENT_YELLOW

    if os.path.exists(IMG_KMEANS_DIAG):
        slide5.shapes.add_picture(IMG_KMEANS_DIAG, Inches(1.0), Inches(4.45), width=Inches(11.3))

    # =========================================================================
    # SLIDE 6: 3) PREPROCESAMIENTO Y SELECCIÓN DE K (K=5 VS K=6)
    # =========================================================================
    slide6 = prs.slides.add_slide(blank_layout)
    set_slide_background(slide6)
    add_header(slide6, "3. Preprocesamiento Vectorial y Selección de K", "EXPERIMENTACIÓN Y MÉTRICAS")

    # Left: Prep pipeline & Decision
    create_card(slide6, Inches(0.8), Inches(1.55), Inches(4.9), Inches(5.5))
    tb = slide6.shapes.add_textbox(Inches(1.05), Inches(1.75), Inches(4.4), Inches(5.1))
    tf = tb.text_frame; tf.word_wrap = True
    p = tf.paragraphs[0]; p.text = "PREPARACIÓN DE DATOS"; p.font.size = Pt(13); p.font.bold = True; p.font.color.rgb = ACCENT_PURPLE
    p = tf.add_paragraph()
    p.text = "• StandardScaler:\nEstandariza variables numéricas (media 0, std 1) para evitar que mm dominen sobre cm.\n\n" \
              "• OneHotEncoder:\nConvierte 10 variables categóricas en vectores binarios ortogonales sin inducir falso orden.\n\n" \
              "• PCA 2D:\nProyección a 2 componentes principales (32.9% de varianza explicada) para inspección visual."
    p.font.size = Pt(11.5); p.font.color.rgb = TEXT_BODY; p.space_before = Pt(4)

    p = tf.add_paragraph()
    p.text = "\n¿POR QUÉ ELEGIMOS K=6?"; p.font.size = Pt(13); p.font.bold = True; p.font.color.rgb = ACCENT_CYAN
    p = tf.add_paragraph()
    p.text = f"• Silhouette Score:\nK=5: {meta['results_5_sil']:.4f}  vs  K=6: {meta['results_6_sil']:.4f}\n(Ambos >0.32, excelente cohesión).\n\n" \
              f"• Davies-Bouldin (Menor es mejor):\nK=5: {meta['results_5_db']:.4f}  vs  K=6: {meta['results_6_db']:.4f}\n" \
              "K=6 logra clusters con menor dispersión y mayor nitidez.\n\n" \
              "• Aísla hongos raros gigantes y separa pies largos de porosos."
    p.font.size = Pt(11); p.font.color.rgb = TEXT_MUTED; p.space_before = Pt(2)

    # Right Top: Metrics Chart
    create_card(slide6, Inches(6.0), Inches(1.55), Inches(6.5), Inches(2.6))
    if os.path.exists(IMG_METRICAS):
        slide6.shapes.add_picture(IMG_METRICAS, Inches(6.1), Inches(1.65), width=Inches(6.3))

    # Right Bottom: Scatter comparison K=5 vs K=6
    create_card(slide6, Inches(6.0), Inches(4.35), Inches(6.5), Inches(2.7))
    if os.path.exists(IMG_SCATTER_COMP):
        slide6.shapes.add_picture(IMG_SCATTER_COMP, Inches(6.1), Inches(4.45), width=Inches(6.3))

    # =========================================================================
    # SLIDE 7: 4) VISIÓN GLOBAL DE LOS 6 CLUSTERS (K=6)
    # =========================================================================
    slide7 = prs.slides.add_slide(blank_layout)
    set_slide_background(slide7)
    add_header(slide7, "4. Visión Global de los 6 Clusters (Modelo K=6)", "RESULTADOS DEL CLUSTERING")

    # Left: Scatter PCA K=6
    create_card(slide7, Inches(0.8), Inches(1.55), Inches(6.3), Inches(5.5))
    tb = slide7.shapes.add_textbox(Inches(1.05), Inches(1.7), Inches(5.8), Inches(0.35))
    tb.text_frame.paragraphs[0].text = "PROYECCIÓN DE PUNTOS PCA 2D (K=6)"
    tb.text_frame.paragraphs[0].font.size = Pt(12); tb.text_frame.paragraphs[0].font.bold = True
    tb.text_frame.paragraphs[0].font.color.rgb = ACCENT_CYAN

    if os.path.exists(IMG_SCATTER_K6):
        slide7.shapes.add_picture(IMG_SCATTER_K6, Inches(0.95), Inches(2.1), width=Inches(6.0))

    # Right: Bar Chart Sizes K=6
    create_card(slide7, Inches(7.4), Inches(1.55), Inches(5.1), Inches(5.5))
    tb = slide7.shapes.add_textbox(Inches(7.6), Inches(1.7), Inches(4.7), Inches(0.35))
    tb.text_frame.paragraphs[0].text = "DISTRIBUCIÓN DE TAMAÑOS POR CLUSTER"
    tb.text_frame.paragraphs[0].font.size = Pt(12); tb.text_frame.paragraphs[0].font.bold = True
    tb.text_frame.paragraphs[0].font.color.rgb = ACCENT_PURPLE

    if os.path.exists(IMG_BARRAS):
        slide7.shapes.add_picture(IMG_BARRAS, Inches(7.5), Inches(2.1), width=Inches(4.8))

    # =========================================================================
    # SLIDE 8: 4) DETALLE DE CLUSTERS: C0, C1, C2
    # =========================================================================
    slide8 = prs.slides.add_slide(blank_layout)
    set_slide_background(slide8)
    add_header(slide8, "4. Caracterización de Clusters: C0, C1 y C2", "DESCRIPCIÓN DE MORFOTIPOS")

    clusters_p1 = [
        ("Cluster 0", "Anillados convexos marrones", ACCENT_PURPLE,
         f"{meta['sizes_6']['0']:,} ({meta['pct_6']['0']}%)",
         "Sombrero: 6.0 cm | Pie: 6.8 cm alto, 10.1 mm ancho",
         "100.0% con anillo evidente (has-ring='t')",
         "• Sombrero convexo ('x') de tono castaño ('n') o amarillo ('y').\n"
         "• Presencia obligatoria de anillo membranoso.\n"
         "• Láminas adnatas cerradas y pie cilíndrico blanquecino.\n"
         "• Morfotipo clásico de setas de campo tradicionales."),

        ("Cluster 1", "Grandes de poros (Boletales)", ACCENT_PINK,
         f"{meta['sizes_6']['1']:,} ({meta['pct_6']['1']}%)",
         "Sombrero: 13.6 cm | Pie: 9.4 cm alto, 34.3 mm ancho (Muy grueso)",
         "0.1% con anillo (prácticamente ausente)",
         "• Estípite sumamente engrosado y masivo (~34.3 mm).\n"
         "• Himenio característico de poros o decurrente (gill-attachment='p').\n"
         "• Sombrero ancho marrón oscuro o blanquecino.\n"
         "• Morfología típica del orden Boletales."),

        ("Cluster 2", "Pegajosos sin anillo (Morfología Media)", ACCENT_CYAN,
         f"{meta['sizes_6']['2']:,} ({meta['pct_6']['2']}%)",
         "Sombrero: 7.7 cm | Pie: 6.2 cm alto, 14.9 mm ancho",
         "7.7% con anillo (mayoritariamente desnudos)",
         "• Segundo cluster más numeroso (32.2% del dataset).\n"
         "• Cutícula típicamente lisa o viscosa/pegajosa (cap-surface='t').\n"
         "• Láminas decurrentes o adnatas de tonos marrones.\n"
         "• Estípite estándar sin estructuras anulares visibles.")
    ]

    for i, (cid, cname, col, cvol, cdim, cring, cdesc) in enumerate(clusters_p1):
        cx = Inches(0.8) + i * (col_w + gap)
        create_card(slide8, cx, Inches(1.55), col_w, Inches(5.5), border_color=col)
        tb = slide8.shapes.add_textbox(cx + Inches(0.2), Inches(1.75), col_w - Inches(0.4), Inches(5.1))
        tf = tb.text_frame; tf.word_wrap = True
        p = tf.paragraphs[0]; p.text = f"● {cid}"; p.font.size = Pt(15); p.font.bold = True; p.font.color.rgb = col
        p = tf.add_paragraph(); p.text = cname; p.font.size = Pt(14); p.font.bold = True; p.font.color.rgb = TEXT_TITLE; p.space_before = Pt(2)
        p = tf.add_paragraph(); p.text = f"Volumen: {cvol}"; p.font.size = Pt(12.5); p.font.bold = True; p.font.color.rgb = col; p.space_before = Pt(4)
        p = tf.add_paragraph()
        p.text = f"\n📏 Dimensiones:\n{cdim}\n\n💍 Anillo:\n{cring}\n\n🔬 Características Clave:\n{cdesc}"
        p.font.size = Pt(12); p.font.color.rgb = TEXT_BODY

    # =========================================================================
    # SLIDE 9: 4) DETALLE DE CLUSTERS: C3, C4, C5
    # =========================================================================
    slide9 = prs.slides.add_slide(blank_layout)
    set_slide_background(slide9)
    add_header(slide9, "4. Caracterización de Clusters: C3, C4 y C5", "DESCRIPCIÓN DE MORFOTIPOS")

    clusters_p2 = [
        ("Cluster 3", "Pequeños sin anillo (Gráciles / Micenas)", ACCENT_YELLOW,
         f"{meta['sizes_6']['3']:,} ({meta['pct_6']['3']}%)",
         "Sombrero: 3.0 cm | Pie: 4.7 cm alto, 4.5 mm ancho (Muy delgado)",
         "3.2% con anillo (96.8% desnudos)",
         "• El cluster más abundante del dataset (36.1%).\n"
         "• Hongos menudos y gráciles de pie filiforme (~4.5 mm).\n"
         "• Sombrero diminuto (~3.0 cm) y láminas adnatas apretadas.\n"
         "• Crecimiento típicamente gregario sobre hojarasca o corteza."),

        ("Cluster 4", "Esféricos gigantes amarillos (Raros)", ACCENT_BLUE,
         f"{meta['sizes_6']['4']:,} ({meta['pct_6']['4']}%)",
         "Sombrero: 50.3 cm (Gigante) | Pie: 6.5 cm, 35.1 mm ancho",
         "0.0% con anillo",
         "• Cluster altamente singular y homogéneo (0.6%).\n"
         "• Sombrero esférico monumental (cap-shape='o', 100%).\n"
         "• Coloración amarilla brillante ('y', 100%) con poros.\n"
         "• Morfología concordante con bejines gigantes (Calvatia)."),

        ("Cluster 5", "Grandes blancos de pie alto (Esbeltos)", RGBColor(194, 65, 12),
         f"{meta['sizes_6']['5']:,} ({meta['pct_6']['5']}%)",
         "Sombrero: 10.7 cm | Pie: 13.9 cm alto (Muy alto), 15.8 mm ancho",
         "78.0% con anillo membranoso",
         "• Especímenes esbeltos de gran longitud de estípite (~14 cm).\n"
         "• Sombrero amplio predominantemente blanco o pálido.\n"
         "• Elevada presencia de anillo (78%) e inserción libre/emarginada.\n"
         "• Perfil similar a especies de géneros Amanita o Lepiota.")
    ]

    for i, (cid, cname, col, cvol, cdim, cring, cdesc) in enumerate(clusters_p2):
        cx = Inches(0.8) + i * (col_w + gap)
        create_card(slide9, cx, Inches(1.55), col_w, Inches(5.5), border_color=col)
        tb = slide9.shapes.add_textbox(cx + Inches(0.2), Inches(1.75), col_w - Inches(0.4), Inches(5.1))
        tf = tb.text_frame; tf.word_wrap = True
        p = tf.paragraphs[0]; p.text = f"● {cid}"; p.font.size = Pt(15); p.font.bold = True; p.font.color.rgb = col
        p = tf.add_paragraph(); p.text = cname; p.font.size = Pt(14); p.font.bold = True; p.font.color.rgb = TEXT_TITLE; p.space_before = Pt(2)
        p = tf.add_paragraph(); p.text = f"Volumen: {cvol}"; p.font.size = Pt(12.5); p.font.bold = True; p.font.color.rgb = col; p.space_before = Pt(4)
        p = tf.add_paragraph()
        p.text = f"\n📏 Dimensiones:\n{cdim}\n\n💍 Anillo:\n{cring}\n\n🔬 Características Clave:\n{cdesc}"
        p.font.size = Pt(12); p.font.color.rgb = TEXT_BODY

    # =========================================================================
    # SLIDE 10: CONCLUSIONES Y SÍNTESIS FINAL
    # =========================================================================
    slide10 = prs.slides.add_slide(blank_layout)
    set_slide_background(slide10)
    add_header(slide10, "Síntesis de Resultados y Conclusiones", "CIERRE DE LA ENTREGA")

    gw = Inches(5.6)
    gh = Inches(2.6)
    gx1 = Inches(0.8); gx2 = Inches(6.8)
    gy1 = Inches(1.55); gy2 = Inches(4.45)

    boxes = [
        (gx1, gy1, "1. Curación Exitosa", ACCENT_PURPLE,
         "• Descarte de 146 duplicados exactos.\n"
         "• Eliminación de 4 columnas con >70% de datos faltantes.\n"
         "• Imputación por mediana y moda que preservó el 99.76% de los ejemplares sin distorsionar centroides."),

        (gx2, gy1, "2. Aislamiento No Supervisado", ACCENT_CYAN,
         "• Se excluyó rigurosamente la etiqueta 'class' (comestible/venenoso).\n"
         "• El modelo agrupó por afinidad física pura, reproduciendo la metodología de clasificación botánica real."),

        (gx1, gy2, "3. Validación Geométrica (K=6)", ACCENT_YELLOW,
         "• Davies-Bouldin de 0.8425 (superior a K=5 con 0.8722).\n"
         "• Coeficiente de Silhouette de 0.3284 confirma cohesión sólida.\n"
         "• PCA 2D explica el 32.9% de varianza facilitando la interpretabilidad visual."),

        (gx2, gy2, "4. Taxonomía de los 6 Grupos", ACCENT_PINK,
         "• Gran nitidez morfológica entre hongos pequeños (C3), gigantes porosos (C1), pies altos (C5) y singulares esféricos (C4).\n"
         "• Base limpia con cluster asignado guardada en 'dataset_clustering.csv'.")
    ]

    for bx, by, btitle, bcol, btext in boxes:
        create_card(slide10, bx, by, gw, gh, border_color=bcol)
        tb = slide10.shapes.add_textbox(bx + Inches(0.25), by + Inches(0.2), gw - Inches(0.5), gh - Inches(0.4))
        tf = tb.text_frame; tf.word_wrap = True
        p = tf.paragraphs[0]; p.text = btitle; p.font.size = Pt(16); p.font.bold = True; p.font.color.rgb = bcol
        p = tf.add_paragraph(); p.text = btext; p.font.size = Pt(12.5); p.font.color.rgb = TEXT_BODY; p.space_before = Pt(6)

    prs.save(PPTX_PATH)
    print(f"Presentación PPTX (Modo Claro + Fuentes Grandes) generada en: {PPTX_PATH}", flush=True)

if __name__ == "__main__":
    build_presentation()
