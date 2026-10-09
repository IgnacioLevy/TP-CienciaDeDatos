# -*- coding: utf-8 -*-
import os, sys, json
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Image, Table, TableStyle, PageBreak, HRFlowable
)
from reportlab.pdfgen import canvas
import pymupdf

BASE = r"E:\cosas\facu\Ciencia de Datos\ciencia de datos-20261008T230846Z-1-001\ciencia de datos"
ENTREGA_DIR = os.path.join(BASE, "implementacion", "entrega2")
PDF_PATH = os.path.join(ENTREGA_DIR, "informe_entrega2.pdf")
META_PATH = os.path.join(ENTREGA_DIR, "_meta.json")

with open(META_PATH, "r", encoding="utf-8") as f:
    meta = json.load(f)

PAGE_WIDTH, PAGE_HEIGHT = letter  # 612 x 792 pt
MARGIN = 32
USABLE_WIDTH = PAGE_WIDTH - 2 * MARGIN  # 548 pt

class NumberedCanvas(canvas.Canvas):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_page_decorations(num_pages)
            super().showPage()
        super().save()

    def draw_page_decorations(self, page_count):
        self.saveState()
        self.setFont("Helvetica", 8)
        self.setFillColor(colors.HexColor("#64748B"))
        
        # Header (pages > 1)
        if self._pageNumber > 1:
            self.drawString(MARGIN, PAGE_HEIGHT - 22, "Ciencia de Datos | Segunda Entrega: Clusterización de Hongos (K-Means)")
            self.setStrokeColor(colors.HexColor("#CBD5E1"))
            self.setLineWidth(0.5)
            self.line(MARGIN, PAGE_HEIGHT - 26, PAGE_WIDTH - MARGIN, PAGE_HEIGHT - 26)
            
        # Footer (all pages)
        footer_text = f"Página {self._pageNumber} de {page_count}"
        self.drawRightString(PAGE_WIDTH - MARGIN, 16, footer_text)
        self.drawString(MARGIN, 16, "Secondary Mushroom Dataset | Pipeline de Clusterización & Análisis Morfológico")
        self.setStrokeColor(colors.HexColor("#CBD5E1"))
        self.setLineWidth(0.5)
        self.line(MARGIN, 24, PAGE_WIDTH - MARGIN, 24)
        self.restoreState()


def build_pdf():
    doc = SimpleDocTemplate(
        PDF_PATH,
        pagesize=letter,
        leftMargin=MARGIN,
        rightMargin=MARGIN,
        topMargin=32,
        bottomMargin=30
    )

    styles = getSampleStyleSheet()
    
    C_PRIMARY = colors.HexColor("#0F172A")     # Dark Slate / Navy
    C_ACCENT  = colors.HexColor("#4F46E5")     # Indigo
    C_TEXT    = colors.HexColor("#1E293B")     # Slate 800
    C_MUTED   = colors.HexColor("#475569")     # Slate 600
    C_BG_CARD = colors.HexColor("#F8FAFC")     # Soft light
    C_BORDER  = colors.HexColor("#CBD5E1")

    title_style = ParagraphStyle(
        'DocTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=18,
        leading=22,
        textColor=C_PRIMARY,
        spaceAfter=3
    )
    
    subtitle_style = ParagraphStyle(
        'DocSubtitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=10,
        leading=13,
        textColor=C_ACCENT,
        spaceAfter=6
    )

    h1_style = ParagraphStyle(
        'SectionHeading1',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=12,
        leading=15,
        textColor=C_PRIMARY,
        spaceBefore=4,
        spaceAfter=4,
        keepWithNext=True
    )

    h2_style = ParagraphStyle(
        'SectionHeading2',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=9.5,
        leading=12,
        textColor=C_ACCENT,
        spaceBefore=5,
        spaceAfter=3,
        keepWithNext=True
    )

    body_style = ParagraphStyle(
        'BodyDark',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8.5,
        leading=11.5,
        textColor=C_TEXT,
        spaceAfter=4
    )

    callout_style = ParagraphStyle(
        'CalloutText',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8,
        leading=10.5,
        textColor=colors.HexColor("#0F172A")
    )

    table_header_style = ParagraphStyle(
        'TableHeader',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=8,
        leading=10,
        textColor=colors.white,
        alignment=1
    )

    table_cell_style = ParagraphStyle(
        'TableCell',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=7.5,
        leading=9.5,
        textColor=C_TEXT
    )

    table_cell_bold = ParagraphStyle(
        'TableCellBold',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=7.5,
        leading=9.5,
        textColor=C_PRIMARY
    )

    step_title_style = ParagraphStyle(
        'StepTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=8,
        leading=10,
        textColor=C_ACCENT
    )

    story = []

    # =========================================================================
    # PÁGINA 1: INTRODUCCIÓN AL PROYECTO Y PASOS METODOLÓGICOS
    # =========================================================================
    story.append(Paragraph("INFORME SEGUNDA ENTREGA: CLUSTERIZACIÓN", title_style))
    story.append(Paragraph("Aprendizaje No Supervisado con K-Means sobre Secondary Mushroom Dataset", subtitle_style))
    story.append(HRFlowable(width="100%", thickness=1.5, color=C_ACCENT, spaceBefore=0, spaceAfter=6))

    meta_info = [
        [
            Paragraph("<b>Materia:</b> Ciencia de Datos", body_style),
            Paragraph("<b>Entrega:</b> 2da Entrega - Agrupamiento No Supervisado", body_style),
            Paragraph("<b>Muestras:</b> 60.923 | <b>Variables:</b> 13", body_style)
        ]
    ]
    t_meta = Table(meta_info, colWidths=[170, 220, 158])
    t_meta.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor("#F1F5F9")),
        ('BOX', (0,0), (-1,-1), 0.5, colors.HexColor("#CBD5E1")),
        ('TOPPADDING', (0,0), (-1,-1), 3),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3),
        ('LEFTPADDING', (0,0), (-1,-1), 8),
        ('RIGHTPADDING', (0,0), (-1,-1), 8),
    ]))
    story.append(t_meta)
    story.append(Spacer(1, 6))

    story.append(Paragraph("Introducción: Contexto y Objetivo del Proyecto", h1_style))
    story.append(Paragraph(
        "El presente proyecto de la materia <b>Ciencia de Datos</b> aborda el análisis sistemático y la minería de conocimiento sobre el "
        "<b>Secondary Mushroom Dataset</b>, una base de datos masiva con más de 61.000 observaciones de hongos y 21 atributos descriptivos, "
        "diseñada a partir de compendios taxonómicos de micología botánica.",
        body_style
    ))
    story.append(Paragraph(
        "<b>Propósito de la Segunda Entrega:</b> En esta etapa, el requerimiento principal consiste en desarrollar un modelo de "
        "<b>aprendizaje no supervisado mediante algoritmos de clusterización (K-Means)</b> para particionar los especímenes en conglomerados "
        "naturales según sus <b>propiedades morfológicas</b> (estructuras anatómicas de sombrero, estípite, láminas y anillo). "
        "El propósito es descubrir fenotipos homogéneos sin recurrir a la etiqueta de toxicidad (<i>class: edible/poisonous</i>), "
        "emulando la tarea taxonómica real de catalogación morfológica y analizando en profundidad cómo se agrupan los hongos en el espacio multidimensional.",
        body_style
    ))

    story.append(Paragraph("Pasos Metodológicos Seguidos para Lograr la Clusterización:", h2_style))
    story.append(Paragraph(
        "Para transformar la base de datos cruda y ruidosa en un agrupamiento consistente, validado e interpretable, se ejecutó un pipeline estructurado en 6 fases consecutivas:",
        body_style
    ))

    pasos_data = [
        [
            Paragraph("<b>Fase / Paso</b>", table_header_style),
            Paragraph("<b>Descripción de la Tarea Ejecutada</b>", table_header_style),
            Paragraph("<b>Resultado / Salida Técnica</b>", table_header_style)
        ],
        [
            Paragraph("<b>Paso 1: Auditoría y Limpieza Primaria</b>", step_title_style),
            Paragraph("Inspección de calidad, cuantificación de valores faltantes por atributo y detección de duplicados exactos generados en la digitalización.", table_cell_style),
            Paragraph(f"Eliminación de {meta['n_dup']} filas duplicadas (base de 60.923 registros). Diagnóstico de 4 columnas críticas con >70% de nulos.", table_cell_style)
        ],
        [
            Paragraph("<b>Paso 2: Filtrado Dimensional Morfológico</b>", step_title_style),
            Paragraph("Aislamiento estricto de variables físicas corporales del hongo. Descarte de la variable supervisada <i>class</i> y factores ecológicos externos (hábitat/estación).", table_cell_style),
            Paragraph("Selección de 13 atributos puramente morfológicos de sombrero, pie, láminas y anillo. Eliminación de 4 columnas con vacío de datos.", table_cell_style)
        ],
        [
            Paragraph("<b>Paso 3: Imputación Estadística de Nulos</b>", step_title_style),
            Paragraph("Resolución del vacío informativo aplicando estimadores robustos: mediana para dimensiones métricas y moda para categorías anatómicas.", table_cell_style),
            Paragraph("Matriz 100% densa (0 valores faltantes) preservando el 99.76% del volumen muestral sin distorsión de outliers.", table_cell_style)
        ],
        [
            Paragraph("<b>Paso 4: Estandarización y Codificación Vectorial</b>", step_title_style),
            Paragraph("Construcción de un espacio geométrico apto para distancias euclídeas mediante <code>StandardScaler</code> en numéricas y <code>OneHotEncoder</code> en nominales.", table_cell_style),
            Paragraph("Espacio euclídeo ortogonal continuo donde cada dimensión aporta de forma equitativa sin sesgo de escalas métricas.", table_cell_style)
        ],
        [
            Paragraph("<b>Paso 5: Modelado No Supervisado y Validación (K-Means)</b>", step_title_style),
            Paragraph("Entrenamiento de modelos con inicialización <code>k-means++</code> comparando K=5 y K=6. Proyección PCA 2D y evaluación con Silhouette y Davies-Bouldin.", table_cell_style),
            Paragraph("Elección de K=6 por mejor separación de grupos (Davies-Bouldin = 0.8425) y mayor resolución anatómica.", table_cell_style)
        ],
        [
            Paragraph("<b>Paso 6: Caracterización y Perfilado Biológico</b>", step_title_style),
            Paragraph("Extracción de centroides, perfiles modales y frecuencias relativas de cada cluster para asignarles nombres descriptivos y diagnósticos morfológicos.", table_cell_style),
            Paragraph("Identificación de 6 morfotipos distintivos (anillados, boletales gruesos, gráciles pequeños, singulares gigantes, etc.).", table_cell_style)
        ]
    ]

    t_pasos = Table(pasos_data, colWidths=[120, 255, 173])
    t_pasos.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), C_PRIMARY),
        ('ALIGN', (0,0), (-1,0), 'CENTER'),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('GRID', (0,0), (-1,-1), 0.5, C_BORDER),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, C_BG_CARD]),
        ('TOPPADDING', (0,0), (-1,-1), 2),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2),
        ('LEFTPADDING', (0,0), (-1,-1), 5),
        ('RIGHTPADDING', (0,0), (-1,-1), 5),
    ]))
    story.append(t_pasos)
    story.append(Spacer(1, 6))

    box_intro = [
        [Paragraph("<b>Hoja de Ruta del Informe:</b> A continuación se detallan exhaustivamente los 4 ejes requeridos para esta entrega: "
                   "<b>(1)</b> Cambios entre datasets, <b>(2)</b> Tratamiento de nulos, <b>(3)</b> Funcionamiento de K-Means y selección de K, y <b>(4)</b> Caracterización y denominación de los clusters resultantes.", callout_style)]
    ]
    t_box_intro = Table(box_intro, colWidths=[USABLE_WIDTH])
    t_box_intro.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor("#EFF6FF")),
        ('BOX', (0,0), (-1,-1), 0.5, colors.HexColor("#3B82F6")),
        ('TOPPADDING', (0,0), (-1,-1), 3),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3),
        ('LEFTPADDING', (0,0), (-1,-1), 8),
        ('RIGHTPADDING', (0,0), (-1,-1), 8),
    ]))
    story.append(t_box_intro)

    # =========================================================================
    # PÁGINA 2: SECCIÓN 1: CAMBIOS EN EL DATASET
    # =========================================================================
    story.append(PageBreak())
    story.append(Paragraph("1. Cambios entre el Dataset Original y el Actual", h1_style))
    story.append(Paragraph(
        "Para lograr una clusterización fenotípica interpretable y robusta, el dataset <b>Secondary Mushroom</b> fue sometido "
        "a un proceso de curación enfocado en la anatomía estructural del hongo, eliminando sesgos supervisados, redundancias y dimensiones sin soporte informacional.",
        body_style
    ))

    t_cambios_data = [
        [Paragraph("Aspecto", table_header_style), Paragraph("Dataset Original", table_header_style), Paragraph("Dataset Actual (Modelado)", table_header_style), Paragraph("Impacto y Justificación Técnica", table_header_style)],
        [
            Paragraph("<b>Registros (Filas)</b>", table_cell_bold),
            Paragraph(f"{meta['n_orig_rows']:,} filas", table_cell_style),
            Paragraph(f"<b>{meta['n_final_rows']:,} filas limpias</b>", table_cell_bold),
            Paragraph(f"Se identificaron y eliminaron {meta['n_dup']} registros duplicados exactos. Esto previene un sobrepeso espurio en el cálculo de centroides euclídeos.", table_cell_style)
        ],
        [
            Paragraph("<b>Dimensiones (Columnas)</b>", table_cell_bold),
            Paragraph(f"{meta['n_orig_cols']} variables mixtas", table_cell_style),
            Paragraph(f"<b>{meta['n_final_cols']} variables morfológicas</b>", table_cell_bold),
            Paragraph("Se acotó el análisis a los atributos físicos medibles del espécimen (sombrero, estípite, láminas y anillo), garantizando homogeneidad semántica.", table_cell_style)
        ],
        [
            Paragraph("<b>Variable Objetivo (class)</b>", table_cell_bold),
            Paragraph("Presente (e: edible / p: poisonous)", table_cell_style),
            Paragraph("<b>Excluida del pipeline</b>", table_cell_bold),
            Paragraph("El objetivo de esta entrega es la <b>clusterización no supervisada</b>. Mantener la etiqueta de toxicidad sesgaría la formación natural de grupos anatómicos.", table_cell_style)
        ],
        [
            Paragraph("<b>Atributos con >70% Nulos</b>", table_cell_bold),
            Paragraph("4 columnas casi vacías (72-84% NaN)", table_cell_style),
            Paragraph("<b>Eliminadas por completo</b>", table_cell_bold),
            Paragraph("Las columnas <i>stem-root, veil-type, veil-color</i> y <i>spore-print-color</i> carecían de masa crítica de datos, haciendo su imputación contraproducente.", table_cell_style)
        ],
        [
            Paragraph("<b>Variables de Contexto</b>", table_cell_bold),
            Paragraph("habitat, season (ecológicas)", table_cell_style),
            Paragraph("<b>Removidas</b>", table_cell_bold),
            Paragraph("Variables estacionales y ecológicas externas fueron descartadas para aislar exclusivamente la morfología corporal intrínseca de los hongos.", table_cell_style)
        ]
    ]

    t_cambios = Table(t_cambios_data, colWidths=[105, 95, 125, 223])
    t_cambios.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), C_PRIMARY),
        ('ALIGN', (0,0), (-1,0), 'CENTER'),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('GRID', (0,0), (-1,-1), 0.5, C_BORDER),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, C_BG_CARD]),
        ('TOPPADDING', (0,0), (-1,-1), 2.5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2.5),
        ('LEFTPADDING', (0,0), (-1,-1), 5),
        ('RIGHTPADDING', (0,0), (-1,-1), 5),
    ]))
    story.append(t_cambios)
    story.append(Spacer(1, 6))

    story.append(Paragraph("Estructura Anatómica de las 13 Variables Morfológicas Conservadas:", h2_style))
    story.append(Paragraph(
        "• <b>Sombrero (Pileus):</b> <code>cap-diameter</code> (numérico continuo en cm, media: 6.7 cm), <code>cap-shape</code> (forma: cónica, convexa, plana, etc.), <code>cap-surface</code> (textura: lisa, fibrosa, viscosa), <code>cap-color</code> (tonalidad cromática dominante).<br/>"
        "• <b>Pie / Estípite (Stipe):</b> <code>stem-height</code> (longitud en cm), <code>stem-width</code> (grosor basal en mm), <code>stem-color</code> (color), <code>stem-surface</code> (textura superficial).<br/>"
        "• <b>Láminas / Himenio (Gills):</b> <code>gill-color</code> (coloración del himenio), <code>gill-attachment</code> (tipo de inserción al pie: adnatas, libres, poroides, decurrentes), <code>gill-spacing</code> (densidad: cerrado vs distante).<br/>"
        "• <b>Anillo / Velo (Annulus):</b> <code>has-ring</code> (indicador binario t/f de presencia de anillo), <code>ring-type</code> (tipología estructural del anillo: colgante, evanescente, membranoso, etc.).",
        body_style
    ))
    story.append(Spacer(1, 6))

    meta_diff_box = [
        [Paragraph("<b>Resumen Cuantitativo:</b> El dataset pasó de una matriz cruda de <b>61.069 filas × 21 columnas</b> con 33% de valores faltantes agregados y variable supervisada, a una matriz morfológica optimizada de <b>60.923 filas × 13 columnas</b> 100% completas y estandarizadas.", callout_style)]
    ]
    t_box1 = Table(meta_diff_box, colWidths=[USABLE_WIDTH])
    t_box1.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor("#EFF6FF")),
        ('BOX', (0,0), (-1,-1), 0.5, colors.HexColor("#3B82F6")),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
        ('LEFTPADDING', (0,0), (-1,-1), 8),
        ('RIGHTPADDING', (0,0), (-1,-1), 8),
    ]))
    story.append(t_box1)

    # =========================================================================
    # PÁGINA 3: SECCIÓN 2: TRATAMIENTO DE DATOS NULOS
    # =========================================================================
    story.append(PageBreak())
    story.append(Paragraph("2. Tratamiento de Datos Nulos", h1_style))
    story.append(Paragraph(
        "Los valores faltantes en el Secondary Mushroom Dataset no ocurren de forma aleatoria, sino que siguen patrones estructurales "
        "ligados a familias micológicas (por ejemplo, especies que carecen por completo de velo o pie). "
        "Se aplicó una metodología sistemática de dos etapas: <b>descarte dimensional con umbral técnico del 70%</b> e <b>imputación estadística diferenciada por escala métrica</b>.",
        body_style
    ))

    if os.path.exists(meta['img_nulos']):
        story.append(Image(meta['img_nulos'], width=USABLE_WIDTH, height=135))
        story.append(Spacer(1, 4))

    t_nulos_data = [
        [Paragraph("Categoría de Atributo", table_header_style), Paragraph("Variables Afectadas", table_header_style), Paragraph("% Nulos", table_header_style), Paragraph("Tratamiento Aplicado", table_header_style), Paragraph("Fundamento Estadístico y Micológico", table_header_style)],
        [
            Paragraph("<b>Nulos Críticos (>70%)</b>", table_cell_bold),
            Paragraph("<i>stem-root</i> (84.8%)<br/><i>veil-type</i> (94.8%)<br/><i>veil-color</i> (87.9%)<br/><i>spore-print-color</i> (73.0%)", table_cell_style),
            Paragraph("<b>73% a 95%</b>", table_cell_bold),
            Paragraph("<b>Eliminación Completa de la Columna</b>", table_cell_bold),
            Paragraph("Imputar más del 70% de las observaciones implicaría inventar artificialmente la mayor parte de la distribución, generando artefactos y distorsión en la métrica euclídea.", table_cell_style)
        ],
        [
            Paragraph("<b>Variables Numéricas (<2%)</b>", table_cell_bold),
            Paragraph("<i>cap-diameter</i> (0%)<br/><i>stem-height</i> (0%)<br/><i>stem-width</i> (1.7%)", table_cell_style),
            Paragraph("<b>0% a 1.7%</b>", table_cell_bold),
            Paragraph("<b>Imputación por Mediana</b>", table_cell_bold),
            Paragraph("La mediana es un estimador de posición no paramétrico insensible a la asimetría de la muestra y valores extremos (hongos gigantes atípicos), preservando el centroide biológico real.", table_cell_style)
        ],
        [
            Paragraph("<b>Variables Categóricas (<20%)</b>", table_cell_bold),
            Paragraph("<i>cap-surface</i> (18.3%)<br/><i>stem-surface</i> (15.8%)<br/><i>gill-attachment</i> (16.2%)<br/><i>gill-spacing</i> (1.4%)", table_cell_style),
            Paragraph("<b>1% a 19%</b>", table_cell_bold),
            Paragraph("<b>Imputación por Moda (Categoría Frecuente)</b>", table_cell_bold),
            Paragraph("Reemplaza la ausencia por el fenotipo dominante de la población sin introducir categorías espurias ni alterar la cardinalidad del espacio categórico one-hot.", table_cell_style)
        ]
    ]

    t_nulos = Table(t_nulos_data, colWidths=[95, 115, 60, 115, 163])
    t_nulos.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), C_PRIMARY),
        ('ALIGN', (0,0), (-1,0), 'CENTER'),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('GRID', (0,0), (-1,-1), 0.5, C_BORDER),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, C_BG_CARD]),
        ('TOPPADDING', (0,0), (-1,-1), 3),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3),
        ('LEFTPADDING', (0,0), (-1,-1), 5),
        ('RIGHTPADDING', (0,0), (-1,-1), 5),
    ]))
    story.append(t_nulos)
    story.append(Spacer(1, 6))

    story.append(Paragraph("Evaluación de Alternativas de Limpieza Descartadas:", h2_style))
    story.append(Paragraph(
        "1. <b>Eliminación de Filas con Algún Nulo (Dropna):</b> Si se hubiesen eliminado todas las filas que contenían al menos un valor faltante, "
        "se hubiera descartado más del <b>82% de las muestras</b>, reduciendo la base de 61.069 a menos de 11.000 hongos y eliminando géneros enteros.<br/>"
        "2. <b>Imputación por un Valor Fijo '0' o 'Desconocido' en Categóricas:</b> Introducir un valor neutro crea un 'cluster artificial de ceros' "
        "donde el algoritmo agrupa ejemplares simplemente porque compartían datos faltantes, y no por su afinidad morfológica real.<br/>"
        "3. <b>Imputación por Media en Numéricas:</b> Descartada debido a que variables como <code>stem-width</code> presentan sesgo a la derecha con máximos extremos "
        "que inflarían erróneamente el valor representativo.",
        body_style
    ))
    story.append(Spacer(1, 4))

    box2_content = [
        [Paragraph("<b>Resultado del Tratamiento de Nulos:</b> Matriz 100% densa (cero valores nulos residuales) que retiene el <b>99.76% del volumen original</b> de hongos, apta para cálculo vectorial estricto.", callout_style)]
    ]
    t_box2 = Table(box2_content, colWidths=[USABLE_WIDTH])
    t_box2.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor("#F0FDF4")),
        ('BOX', (0,0), (-1,-1), 0.5, colors.HexColor("#22C55E")),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
        ('LEFTPADDING', (0,0), (-1,-1), 8),
        ('RIGHTPADDING', (0,0), (-1,-1), 8),
    ]))
    story.append(t_box2)

    # =========================================================================
    # PÁGINA 4: SECCIÓN 3: EXPLICACIÓN DE K-MEANS Y FUNCIONAMIENTO
    # =========================================================================
    story.append(PageBreak())
    story.append(Paragraph("3. Algoritmo K-Means: Concepto, Funcionamiento y Validación", h1_style))
    story.append(Paragraph(
        "<b>K-Means</b> es un algoritmo de aprendizaje no supervisado de particionamiento espacial. "
        "Busca particionar <i>N</i> observaciones en <i>K</i> clusters, asignando cada hongo al cluster con el <b>centroide (vector medio)</b> más próximo, "
        "optimizando la función de coste de inercia intra-cluster (<i>Within-Cluster Sum of Squares, WCSS</i>):",
        body_style
    ))

    if os.path.exists(meta['img_kmeans_diag']):
        story.append(Image(meta['img_kmeans_diag'], width=USABLE_WIDTH, height=105))
        story.append(Spacer(1, 4))

    story.append(Paragraph("Ciclo Algorítmico Paso a Paso:", h2_style))
    story.append(Paragraph(
        "• <b>Paso 1: Inicialización Inteligente (k-means++):</b> Se seleccionan <i>K</i> semillas iniciales de forma probabilística ponderada por distancia, "
        "garantizando que los centros iniciales queden bien separados y minimizando el riesgo de estancamiento en mínimos locales subóptimos.<br/>"
        "• <b>Paso 2: Asignación a Centroides Cercanos:</b> Cada hongo <i>x<sub>i</sub></i> calcula su distancia euclídea a los <i>K</i> centros actuales y se asigna al más cercano: "
        "<i>C(i) = argmin<sub>k</sub> ||x<sub>i</sub> - μ<sub>k</sub>||<sup>2</sup></i>.<br/>"
        "• <b>Paso 3: Actualización y Recálculo:</b> Cada centroide <i>μ<sub>k</sub></i> se reubica en la posición media exacta de todos los datos pertenecientes a dicho grupo: "
        "<i>μ<sub>k</sub> = (1/|S<sub>k</sub>|) ∑<sub>x ∈ S<sub>k</sub></sub> x</i>.<br/>"
        "• <b>Paso 4: Convergencia:</b> Se repiten los pasos 2 y 3 hasta que el desplazamiento de centroides sea inferior al umbral de convergencia (<i>tol=1e-4</i>) o se cumplan 500 iteraciones.",
        body_style
    ))

    story.append(Paragraph("Preprocesamiento y Reducción Dimensional PCA:", h2_style))
    story.append(Paragraph(
        "K-Means requiere un espacio métrico continuo euclídeo. Para procesar el dataset mixto se aplicó un pipeline de dos etapas:<br/>"
        "1. <b>StandardScaler:</b> Estandarizó las variables métricas continuas (media 0, desviación 1), evitando que variables en milímetros dominen sobre variables en centímetros.<br/>"
        "2. <b>OneHotEncoder:</b> Codificó las variables nominales en variables binarias ortogonales (0/1), permitiendo comparaciones de distancia sin introducir relaciones ordinales falsas.<br/>"
        f"3. <b>PCA (Componentes Principales):</b> Para la visualización e inspección de fronteras se proyectó a 2 componentes principales (<b>PC1: {meta['var_exp'][0]:.1f}%</b>, <b>PC2: {meta['var_exp'][1]:.1f}%</b>, acumulando <b>{meta['var_exp'][0]+meta['var_exp'][1]:.1f}%</b> de varianza total).",
        body_style
    ))
    story.append(Spacer(1, 4))

    story.append(Paragraph("Selección Experimental del Número de Clusters: K=5 vs K=6:", h2_style))

    t_metricas_data = [
        [Paragraph("Métrica Intrínseca de Evaluación", table_header_style), Paragraph("Modelo K=5", table_header_style), Paragraph("Modelo K=6 (Seleccionado)", table_header_style), Paragraph("Análisis Comparativo y Decisión", table_header_style)],
        [
            Paragraph("<b>Silhouette Score</b><br/>[-1 a +1, mayor = mejor]", table_cell_bold),
            Paragraph(f"<b>{meta['results_5_sil']:.4f}</b>", table_cell_style),
            Paragraph(f"<b>{meta['results_6_sil']:.4f}</b>", table_cell_style),
            Paragraph("Evalúa qué tan cohesionado está un punto con su cluster versus los vecinos. Ambos modelos muestran una excelente separación estructural (>0.32).", table_cell_style)
        ],
        [
            Paragraph("<b>Davies-Bouldin Index</b><br/>[≥0, menor = mejor]", table_cell_bold),
            Paragraph(f"<b>{meta['results_5_db']:.4f}</b>", table_cell_style),
            Paragraph(f"<b>{meta['results_6_db']:.4f}</b> (Óptimo)", table_cell_bold),
            Paragraph("Mide la similitud entre cada cluster y su vecino más parecido. <b>K=6 reduce el índice a 0.8425</b>, lo que demuestra clusters con menor dispersión y mayor nitidez.", table_cell_style)
        ],
        [
            Paragraph("<b>Resolución Morfológica</b>", table_cell_bold),
            Paragraph("Mezcla hongos de gran porte con boletos", table_cell_style),
            Paragraph("Aísla morfotipos puros y variantes raras", table_cell_bold),
            Paragraph("K=6 logra separar con éxito los hongos esféricos gigantes (Cluster 4) y diferencia los hongos de pie alto (Cluster 5) de los hongos robustos porosos (Cluster 1).", table_cell_style)
        ]
    ]

    t_met = Table(t_metricas_data, colWidths=[120, 75, 110, 243])
    t_met.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), C_PRIMARY),
        ('ALIGN', (0,0), (-1,0), 'CENTER'),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('GRID', (0,0), (-1,-1), 0.5, C_BORDER),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, C_BG_CARD]),
        ('TOPPADDING', (0,0), (-1,-1), 2.5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2.5),
        ('LEFTPADDING', (0,0), (-1,-1), 5),
        ('RIGHTPADDING', (0,0), (-1,-1), 5),
    ]))
    story.append(t_met)
    story.append(Spacer(1, 4))

    if os.path.exists(meta['img_metricas']) and os.path.exists(meta['img_scatter_comp']):
        t_img_comp = Table([
            [
                Image(meta['img_metricas'], width=225, height=92),
                Image(meta['img_scatter_comp'], width=315, height=92)
            ]
        ], colWidths=[230, 318])
        t_img_comp.setStyle(TableStyle([
            ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
            ('ALIGN', (0,0), (-1,-1), 'CENTER'),
            ('TOPPADDING', (0,0), (-1,-1), 0),
            ('BOTTOMPADDING', (0,0), (-1,-1), 0),
            ('LEFTPADDING', (0,0), (-1,-1), 0),
            ('RIGHTPADDING', (0,0), (-1,-1), 0),
        ]))
        story.append(t_img_comp)

    # =========================================================================
    # PÁGINA 5: SECCIÓN 4: EXPLICACIÓN DE CLUSTERS USADOS (K=6)
    # =========================================================================
    story.append(PageBreak())
    story.append(Paragraph("4. Caracterización Detallada de los Clusters (Modelo K=6)", h1_style))
    story.append(Paragraph(
        "A partir de las 60.923 muestras analizadas, el modelo K=6 descubrió 6 grupos fenotípicos bien diferenciados. "
        "A cada conglomerado se le asignó un nombre taxonómico descriptivo basado en sus variables dominantes:",
        body_style
    ))

    if os.path.exists(meta['img_scatter']) and os.path.exists(meta['img_barras']):
        t_img_k6 = Table([
            [
                Image(meta['img_scatter'], width=270, height=125),
                Image(meta['img_barras'], width=270, height=125)
            ]
        ], colWidths=[274, 274])
        t_img_k6.setStyle(TableStyle([
            ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
            ('ALIGN', (0,0), (-1,-1), 'CENTER'),
            ('TOPPADDING', (0,0), (-1,-1), 0),
            ('BOTTOMPADDING', (0,0), (-1,-1), 0),
            ('LEFTPADDING', (0,0), (-1,-1), 0),
            ('RIGHTPADDING', (0,0), (-1,-1), 0),
        ]))
        story.append(t_img_k6)
        story.append(Spacer(1, 4))

    clusters_info = [
        {
            "id": "Cluster 0",
            "name": "Anillados convexos marrones",
            "color": "#6C63FF",
            "size": f"{meta['sizes_6']['0']:,} ({meta['pct_6']['0']}%)",
            "dim": "Sombrero: 6.0 cm | Pie alto: 6.8 cm | Pie ancho: 10.1 mm",
            "ring": "100.0% con anillo ('t')",
            "desc": "Espécimen arquetípico con anillo permanente. Sombrero convexo (forma 'x') de color marrón/castaño ('n') o amarillento ('y'). Láminas adnatas cerradas y pie cilíndrico blanquecino."
        },
        {
            "id": "Cluster 1",
            "name": "Grandes de poros (Morfología Boletoide)",
            "color": "#FF6584",
            "size": f"{meta['sizes_6']['1']:,} ({meta['pct_6']['1']}%)",
            "dim": "Sombrero: 13.6 cm | Pie alto: 9.4 cm | Pie ancho: 34.3 mm (Muy grueso)",
            "ring": "0.1% con anillo",
            "desc": "Hongos de contextura masiva y estípite sumamente engrosado (~34.3 mm). Himenio poroide o decurrente (gill-attachment='p'). Carecen de anillo, sombrero ancho marrón oscuro o blanco."
        },
        {
            "id": "Cluster 2",
            "name": "Pegajosos sin anillo (Morfología Media)",
            "color": "#43D9AD",
            "size": f"{meta['sizes_6']['2']:,} ({meta['pct_6']['2']}%)",
            "dim": "Sombrero: 7.7 cm | Pie alto: 6.2 cm | Pie ancho: 14.9 mm",
            "ring": "7.7% con anillo",
            "desc": "Segundo grupo en volumen (32.2%). Porte intermedio con cutícula lisa o pegajosa/viscosa (cap-surface='t'). Láminas decurrentes o adnatas, tonos castaños y pie desnudo sin estructuras anulares."
        },
        {
            "id": "Cluster 3",
            "name": "Pequeños sin anillo (Micenas y Gráciles)",
            "color": "#FFB347",
            "size": f"{meta['sizes_6']['3']:,} ({meta['pct_6']['3']}%)",
            "dim": "Sombrero: 3.0 cm | Pie alto: 4.7 cm | Pie ancho: 4.5 mm (Muy delgado)",
            "ring": "3.2% con anillo",
            "desc": "El cluster más numeroso (36.1%). Hongos pequeños y delicados de estípite delgado (~4.5 mm) y sombrero diminuto (~3 cm). Láminas adnatas y apretadas. Especímenes gregarios de hojarasca."
        },
        {
            "id": "Cluster 4",
            "name": "Esféricos gigantes amarillos (Singularidad / Raros)",
            "color": "#5EB8FF",
            "size": f"{meta['sizes_6']['4']:,} ({meta['pct_6']['4']}%)",
            "dim": "Sombrero: 50.3 cm (Gigante) | Pie alto: 6.5 cm | Pie ancho: 35.1 mm",
            "ring": "0.0% con anillo",
            "desc": "Cluster altamente singular (0.6%). Sombrero esférico monumental (cap-shape='o', 100%) amarillo brillante ('y', 100%) de medio metro de diámetro, con poros. Compatible con bejines gigantes (Calvatia)."
        },
        {
            "id": "Cluster 5",
            "name": "Grandes blancos de pie alto (Porte Esbelto)",
            "color": "#FF6F61",
            "size": f"{meta['sizes_6']['5']:,} ({meta['pct_6']['5']}%)",
            "dim": "Sombrero: 10.7 cm | Pie alto: 13.9 cm (Muy alto) | Pie ancho: 15.8 mm",
            "ring": "78.0% con anillo",
            "desc": "Hongos estilizados de notable altura (estípite de casi 14 cm). Sombrero amplio predominantemente blanco o claro con escamas. Elevada frecuencia de anillo (78%) y láminas libres/emarginadas."
        }
    ]

    t_clusters_rows = [
        [
            Paragraph("Cluster / Nombre", table_header_style),
            Paragraph("Frecuencia", table_header_style),
            Paragraph("Dimensiones Promedio", table_header_style),
            Paragraph("Presencia Anillo", table_header_style),
            Paragraph("Morfología Diagnóstica", table_header_style)
        ]
    ]

    for c in clusters_info:
        badge = f"<font color='{c['color']}'><b>● {c['id']}</b></font><br/><b>{c['name']}</b>"
        t_clusters_rows.append([
            Paragraph(badge, table_cell_style),
            Paragraph(f"<b>{c['size']}</b>", table_cell_style),
            Paragraph(c['dim'], table_cell_style),
            Paragraph(f"<b>{c['ring']}</b>", table_cell_style),
            Paragraph(c['desc'], table_cell_style)
        ])

    t_clusters_table = Table(t_clusters_rows, colWidths=[105, 75, 110, 72, 186])
    t_clusters_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), C_PRIMARY),
        ('ALIGN', (0,0), (-1,0), 'CENTER'),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('GRID', (0,0), (-1,-1), 0.5, C_BORDER),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, C_BG_CARD]),
        ('TOPPADDING', (0,0), (-1,-1), 2.5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2.5),
        ('LEFTPADDING', (0,0), (-1,-1), 4),
        ('RIGHTPADDING', (0,0), (-1,-1), 4),
    ]))
    story.append(t_clusters_table)
    story.append(Spacer(1, 5))

    box_concl = [
        [Paragraph(
            "<b>Síntesis de Entrega:</b> La clusterización mediante K-Means particionó exitosamente la diversidad de las 60.923 muestras en 6 morfotipos "
            "consistentes con la literatura biológica. Las variables más determinantes para la separación fueron el <b>tamaño relativo (cap-diameter, stem-width)</b>, "
            "la <b>presencia/ausencia de anillo (has-ring)</b> y el <b>tipo de inserción himenial (gill-attachment)</b>, logrando un agrupamiento cohesivo y no supervisado.",
            callout_style
        )]
    ]
    t_box_concl = Table(box_concl, colWidths=[USABLE_WIDTH])
    t_box_concl.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor("#F8FAFC")),
        ('BOX', (0,0), (-1,-1), 0.5, colors.HexColor("#4F46E5")),
        ('TOPPADDING', (0,0), (-1,-1), 3),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3),
        ('LEFTPADDING', (0,0), (-1,-1), 8),
        ('RIGHTPADDING', (0,0), (-1,-1), 8),
    ]))
    story.append(t_box_concl)

    # Build Document
    doc.build(story, canvasmaker=NumberedCanvas)
    print(f"PDF generado exitosamente en: {PDF_PATH}", flush=True)

if __name__ == "__main__":
    build_pdf()
