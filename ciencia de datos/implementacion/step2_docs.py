# -*- coding: utf-8 -*-
import os, json
import numpy as np

OUT_DIR = r'E:\cosas\facu\Ciencia de Datos\ciencia de datos-20261008T230846Z-1-001\ciencia de datos\implementacion\entrega2'
with open(os.path.join(OUT_DIR,'_meta.json'), encoding='utf-8') as f:
    m = json.load(f)

n_orig_rows  = m['n_orig_rows'];  n_orig_cols  = m['n_orig_cols']
n_final_rows = m['n_final_rows']; n_final_cols = m['n_final_cols']
n_dup = m['n_dup']; drop_cols = m['drop_cols']
var_exp = m['var_exp']
sil5=m['results_5_sil']; db5=m['results_5_db']
sil6=m['results_6_sil']; db6=m['results_6_db']
sizes6={int(k):v for k,v in m['sizes_6'].items()}
pct6  ={int(k):v for k,v in m['pct_6'].items()}
img_nulos       = m['img_nulos']
img_scatter     = m['img_scatter']
img_scatter_comp= m['img_scatter_comp']
img_barras      = m['img_barras']
img_metricas    = m['img_metricas']
img_kmeans_diag = m['img_kmeans_diag']

PALETTE = ['#6C63FF','#FF6584','#43D9AD','#FFB347','#5EB8FF','#FF6F61']
COLS_MORFO = ['cap-diameter','cap-shape','cap-surface','cap-color',
    'stem-height','stem-width','stem-color','stem-surface',
    'gill-color','gill-attachment','gill-spacing','has-ring','ring-type']

CLUSTER_NAMES = {0:'Anillados convexos marrones',1:'Grandes de poros',
    2:'Pegajosos sin anillo',3:'Pequenos sin anillo',
    4:'Esfericos amarillos (raros)',5:'Grandes blancos'}
CLUSTER_DESC = {
    0:'Sombrero convexo de color marron, superficie lisa y anillo presente. Representan hongos de tamano mediano con laminas adheridas. Son el grupo mas numeroso del dataset.',
    1:'Hongos de gran tamano, con poros en lugar de laminas. Tallo grueso y solido. Superficie del sombrero irregular o escamosa. Frecuentes en bosques de coniferas.',
    2:'Sombrero pegajoso o viscoso, sin anillo en el tallo. Laminas de color claro, frecuentemente libres. Tallos delgados. Asociados a zonas humedas.',
    3:'Hongos pequenos, sin anillo, de colores variados. Tallos finos y fragiles. Laminas apretadas y densas. Grupo heterogeneo de pequenos especimenes.',
    4:'Forma esferica o globosa, coloracion amarilla o naranja. Grupo minoritario pero muy distintivo morfologicamente. Alta separacion en el espacio de caracteristicas.',
    5:'Hongos de gran tamano, coloracion blanca o crema tanto en el sombrero como en el tallo. Superficie lisa. Anillo presente en varios casos. Laminas blancas.',
}
char_principal = {
    0:'Sombrero convexo marron + anillo',1:'Gran tamano + poros',
    2:'Superficie pegajosa + sin anillo',3:'Pequeno tamano + sin anillo',
    4:'Forma esferica + color amarillo',5:'Gran tamano + coloracion blanca',
}

# ══════════════════════════════════════════════
# PDF
# ══════════════════════════════════════════════
print('Generando PDF...', flush=True)
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.units import cm
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer,
    Image as RLImage, Table, TableStyle, PageBreak, HRFlowable)
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY, TA_LEFT

PDF_PATH = os.path.join(OUT_DIR, 'informe_entrega2.pdf')
doc = SimpleDocTemplate(PDF_PATH, pagesize=A4,
    leftMargin=2.5*cm, rightMargin=2.5*cm, topMargin=2.5*cm, bottomMargin=2.5*cm)

C_PURPLE = colors.HexColor('#6C63FF')
C_GREEN  = colors.HexColor('#43D9AD')
C_DARK   = colors.HexColor('#0f0f1a')
C_TEXT   = colors.HexColor('#222222')
C_WHITE  = colors.white

def S(name,**kw): return ParagraphStyle(name,**kw)
sTitle  = S('T', fontSize=24, textColor=C_PURPLE, fontName='Helvetica-Bold', alignment=TA_CENTER, spaceAfter=8)
sSub    = S('Su', fontSize=13, textColor=C_GREEN,  fontName='Helvetica', alignment=TA_CENTER, spaceAfter=4)
sH1     = S('H1', fontSize=16, textColor=C_PURPLE, fontName='Helvetica-Bold', spaceBefore=14, spaceAfter=6)
sH2     = S('H2', fontSize=13, textColor=C_GREEN,  fontName='Helvetica-Bold', spaceBefore=10, spaceAfter=4)
sBody   = S('Bo', fontSize=10, textColor=C_TEXT,   fontName='Helvetica', leading=15, alignment=TA_JUSTIFY, spaceAfter=6)
sBullet = S('Bu', fontSize=10, textColor=C_TEXT,   fontName='Helvetica', leading=14, leftIndent=18, spaceAfter=3)
sCap    = S('Ca', fontSize=8,  textColor=colors.grey, fontName='Helvetica-Oblique', alignment=TA_CENTER, spaceAfter=6)

def img(path, w=14*cm):
    from PIL import Image as PI
    with PI.open(path) as im: wi,hi = im.size
    return RLImage(path, width=w, height=w*(hi/wi))

def sep():
    return HRFlowable(width='100%', thickness=0.5, color=C_PURPLE, spaceAfter=8, spaceBefore=4)

def tbl_style(header_color, row_colors):
    return TableStyle([
        ('BACKGROUND',(0,0),(-1,0),header_color),('TEXTCOLOR',(0,0),(-1,0),C_WHITE),
        ('FONTNAME',(0,0),(-1,0),'Helvetica-Bold'),('FONTSIZE',(0,0),(-1,-1),9),
        ('ALIGN',(0,0),(-1,-1),'CENTER'),('VALIGN',(0,0),(-1,-1),'MIDDLE'),
        ('ROWBACKGROUNDS',(0,1),(-1,-1),row_colors),
        ('GRID',(0,0),(-1,-1),0.5,colors.HexColor('#ccccee')),('ROWHEIGHT',(0,0),(-1,-1),22),
    ])

st = []
# Portada
st += [Spacer(1,3*cm), Paragraph('Universidad Tecnologica Nacional - FRC', sSub),
       Paragraph('Ciencias de Datos', sSub), Spacer(1,0.8*cm),
       Paragraph('Segunda Entrega', sTitle),
       Paragraph('Clustering del Dataset Secondary Mushroom', sTitle),
       Spacer(1,0.5*cm), Paragraph('ETL - K-Means - Analisis de Clusters', sSub),
       Spacer(1,1.5*cm), Paragraph('Octubre 2026', S('fe',fontSize=11,textColor=colors.grey,fontName='Helvetica',alignment=TA_CENTER)),
       PageBreak()]

# Sec 1
st += [Paragraph('1. Cambios entre el Dataset Original y el Actual', sH1), sep(),
       Paragraph('El dataset original <i>Secondary Mushroom Dataset</i> contiene informacion morfologica de hongos con el objetivo de clasificarlos como comestibles o venenosos. Para la tarea de clustering no supervisado realizamos las siguientes transformaciones:', sBody)]
data1 = [['Caracteristica','Dataset Original','Dataset para Clustering'],
    ['Filas',f'{n_orig_rows:,}',f'{n_final_rows:,}'],
    ['Columnas',str(n_orig_cols),str(n_final_cols)],
    ['Variable target',"'class' (e/p)",'Eliminada (no supervisado)'],
    ['Valores nulos','Presentes en varias columnas','Imputados o eliminados'],
    ['Duplicados',f'{n_dup} registros','Eliminados'],
    ['Encoding','Categoricas en texto','OHE aplicado en el modelo'],
    ['Escalado','Sin escalar','StandardScaler en columnas numericas']]
t1 = Table(data1, colWidths=[5*cm,5*cm,6*cm])
t1.setStyle(tbl_style(C_PURPLE,[colors.HexColor('#f5f5ff'),colors.white]))
st += [t1, Spacer(1,0.4*cm)]

st.append(Paragraph('Columnas eliminadas del dataset original:', sH2))
st.append(Paragraph('Se elimino la columna <b>class</b> (variable objetivo). Ademas se eliminaron las columnas con mas del <b>70% de valores nulos</b>:', sBody))
for col in drop_cols:
    st.append(Paragraph(f'- <b>{col}</b>', sBullet))
if not drop_cols:
    st.append(Paragraph('- Ninguna columna supero el umbral del 70%.', sBullet))
st.append(Spacer(1,0.3*cm))
st.append(Paragraph('Columnas morfologicas seleccionadas (13 variables):', sH2))
for g in [COLS_MORFO[i:i+3] for i in range(0,13,3)]:
    st.append(Paragraph('- ' + ' · '.join(f'<b>{c}</b>' for c in g), sBullet))
st += [Spacer(1,0.4*cm), img(img_nulos),
       Paragraph('Figura 1: Porcentaje de valores nulos por columna. Rojo = supero umbral 70%.', sCap),
       PageBreak()]

# Sec 2
st += [Paragraph('2. Tratamiento de Valores Nulos', sH1), sep(),
       Paragraph('Los valores faltantes no se reemplazaron por 0 ya que distorsionaria las distancias euclideanas. Se aplico una estrategia diferenciada:', sBody),
       Paragraph('2.1 Columnas numericas', sH2),
       Paragraph('Las columnas <b>cap-diameter</b>, <b>stem-height</b> y <b>stem-width</b> se imputaron con la <b>mediana</b>. La mediana es robusta ante outliers y preserva la distribucion real.', sBody),
       Paragraph('2.2 Columnas categoricas', sH2),
       Paragraph('Las columnas de texto (forma, color, superficie, etc.) se imputaron con la <b>moda</b> (valor mas frecuente). Mantiene coherencia semantica sin introducir categorias artificiales.', sBody),
       Paragraph('2.3 Eliminacion por exceso de nulos', sH2),
       Paragraph('Columnas con mas del <b>70% de valores faltantes</b> fueron eliminadas directamente. Imputar >70% con un solo valor estadistico produciria una columna artificialmente homogenea inutilizable.', sBody),
       Paragraph('2.4 Eliminacion de duplicados', sH2),
       Paragraph(f'Se eliminaron <b>{n_dup} filas duplicadas</b>. Los duplicados sesgan el clustering al dar mayor peso a observaciones repetidas.', sBody)]
data2=[['Tipo de columna','Estrategia','Motivo'],
    ['Numerica (cap-diameter, stem-height, stem-width)','Mediana','Robusta ante outliers'],
    ['Categorica (shape, color, surface, etc.)','Moda','Coherencia semantica'],
    ['Cualquier tipo con >70% nulos','Eliminar columna','Imputar >70% no es confiable'],
    ['Filas duplicadas','Eliminar fila','Evita sesgo por repeticion']]
t2=Table(data2,colWidths=[6.5*cm,4*cm,5.5*cm])
t2.setStyle(tbl_style(C_GREEN,[colors.HexColor('#f5fff8'),colors.white]))
st += [Spacer(1,0.3*cm), t2, PageBreak()]

# Sec 3
st += [Paragraph('3. K-Means y la Clusterizacion', sH1), sep(),
       Paragraph('3.1 Que es el clustering?', sH2),
       Paragraph('El <b>clustering</b> es una tecnica de aprendizaje no supervisado que descubre grupos naturales en los datos sin etiquetas previas. El objetivo: elementos del mismo grupo similares entre si, diferentes a los de otros grupos.', sBody),
       Paragraph('3.2 Que es K-Means?', sH2),
       Paragraph('<b>K-Means</b> divide los datos en exactamente <i>K</i> grupos. Cada cluster queda representado por su centroide: el promedio de todos los puntos que le pertenecen.', sBody),
       Paragraph('3.3 Como funciona?', sH2),
       Paragraph('<b>Paso 1 - Inicializacion:</b> Se eligen K centroides iniciales (K-Means++ optimiza esta eleccion).', sBullet),
       Paragraph('<b>Paso 2 - Asignacion:</b> Cada punto se asigna al centroide mas cercano (distancia euclidiana).', sBullet),
       Paragraph('<b>Paso 3 - Actualizacion:</b> Se recalcula cada centroide como el promedio de sus puntos.', sBullet),
       Paragraph('<b>Paso 4 - Convergencia:</b> Se repiten pasos 2 y 3 hasta que los centroides no cambian significativamente.', sBullet),
       Spacer(1,0.4*cm), img(img_kmeans_diag),
       Paragraph('Figura 2: Ilustracion K-Means. Izq: centroides iniciales. Centro: asignacion. Der: clusters convergidos.', sCap),
       Paragraph('3.4 Metricas de evaluacion', sH2),
       Paragraph('<b>Silhouette Score (mayor = mejor):</b> Mide separacion entre clusters. Rango -1 a 1; valores cercanos a 1 = clusters bien definidos.', sBullet),
       Paragraph('<b>Davies-Bouldin (menor = mejor):</b> Mide la razon entre dispersion interna y separacion entre clusters.', sBullet),
       Spacer(1,0.4*cm), img(img_metricas),
       Paragraph(f'Figura 3: Metricas K=5 vs K=6. Silhouette: K5={sil5:.4f} K6={sil6:.4f}. DB: K5={db5:.4f} K6={db6:.4f}.', sCap),
       Paragraph('3.5 Reduccion dimensional con PCA', sH2),
       Paragraph(f'Se aplico <b>PCA</b> a 2 componentes para visualizar los clusters. Las 2 componentes capturan el <b>{sum(var_exp):.1f}%</b> de varianza total (PC1: {var_exp[0]:.1f}%, PC2: {var_exp[1]:.1f}%).', sBody),
       Spacer(1,0.3*cm), img(img_scatter_comp),
       Paragraph('Figura 4: Proyeccion PCA K=5 vs K=6. Cada punto = un hongo.', sCap),
       PageBreak()]

# Sec 4
st += [Paragraph('4. Descripcion de los Clusters (K=6)', sH1), sep(),
       Paragraph(f'Se eligio <b>K=6</b> como configuracion final. Silhouette={sil6:.4f}, Davies-Bouldin={db6:.4f}. Ofrece mejor separabilidad morfologica que K=5.', sBody),
       Spacer(1,0.3*cm), img(img_scatter),
       Paragraph('Figura 5: Proyeccion PCA final K=6. Cada color = un cluster.', sCap),
       Spacer(1,0.2*cm), img(img_barras),
       Paragraph('Figura 6: Distribucion porcentual por cluster. Linea punteada = distribucion ideal (16.7%).', sCap),
       Paragraph('Descripcion de cada cluster:', sH2)]
for cid in range(6):
    n_h=sizes6[cid]; pv=pct6[cid]
    st.append(Paragraph(f'<b>Cluster {cid} - {CLUSTER_NAMES[cid]}</b> ({n_h:,} hongos | {pv:.1f}%)',
        S(f'ch{cid}',fontSize=11,textColor=colors.HexColor(PALETTE[cid]),fontName='Helvetica-Bold',spaceBefore=10,spaceAfter=3)))
    st.append(Paragraph(CLUSTER_DESC[cid], sBody))
st.append(Spacer(1,0.5*cm))
data3=[['Cluster','Nombre','% Dataset','Caracteristica principal']]
for cid in range(6):
    data3.append([f'C{cid}',CLUSTER_NAMES[cid],f'{pct6[cid]:.1f}%',char_principal[cid]])
t3=Table(data3,colWidths=[1.5*cm,5*cm,2.5*cm,7*cm])
t3.setStyle(tbl_style(C_PURPLE,[colors.HexColor('#f5f5ff'),colors.white]))
st.append(t3)
doc.build(st)
print(f'PDF: {PDF_PATH}', flush=True)

# ══════════════════════════════════════════════
# PPTX
# ══════════════════════════════════════════════
print('Generando PPTX...', flush=True)
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN

prs = Presentation()
prs.slide_width  = Inches(13.33)
prs.slide_height = Inches(7.5)

RD=RGBColor(0x0f,0x0f,0x1a); RM=RGBColor(0x1a,0x1a,0x2e)
RP=RGBColor(0x6C,0x63,0xFF); RG=RGBColor(0x43,0xD9,0xAD)
RK=RGBColor(0xFF,0x65,0x84); RO=RGBColor(0xFF,0xB3,0x47)
RW=RGBColor(0xFF,0xFF,0xFF); RL=RGBColor(0xe0,0xe0,0xff)
RB=RGBColor(0x5E,0xB8,0xFF)
CC=[RGBColor(0x6C,0x63,0xFF),RGBColor(0xFF,0x65,0x84),RGBColor(0x43,0xD9,0xAD),
    RGBColor(0xFF,0xB3,0x47),RGBColor(0x5E,0xB8,0xFF),RGBColor(0xFF,0x6F,0x61)]

BL = prs.slide_layouts[6]

def bg(sl,c=RD):
    f=sl.background.fill; f.solid(); f.fore_color.rgb=c

def rect(sl,l,t,w,h,c):
    sh=sl.shapes.add_shape(1,Inches(l),Inches(t),Inches(w),Inches(h))
    sh.fill.solid(); sh.fill.fore_color.rgb=c; sh.line.fill.background(); return sh

def tb(sl,txt,l,t,w,h,fs=18,bold=False,c=RW,align=PP_ALIGN.LEFT):
    bx=sl.shapes.add_textbox(Inches(l),Inches(t),Inches(w),Inches(h))
    tf=bx.text_frame; tf.word_wrap=True
    p=tf.paragraphs[0]; p.alignment=align
    r=p.add_run(); r.text=txt; r.font.size=Pt(fs); r.font.bold=bold; r.font.color.rgb=c
    return bx

def pi(sl,path,l,t,w):
    from PIL import Image as PI
    with PI.open(path) as im: wi,hi=im.size
    sl.shapes.add_picture(path,Inches(l),Inches(t),Inches(w),Inches(w*(hi/wi)))

def bullets(sl,items,l=0.5,t=2.0,w=12,fs=16,c=RL):
    bx=sl.shapes.add_textbox(Inches(l),Inches(t),Inches(w),Inches(5))
    tf=bx.text_frame; tf.word_wrap=True
    for i,(b,txt) in enumerate(items):
        p=tf.paragraphs[0] if i==0 else tf.add_paragraph()
        p.space_before=Pt(6)
        r=p.add_run(); r.text=f'{b}  {txt}'; r.font.size=Pt(fs); r.font.color.rgb=c

# S1 Portada
sl=prs.slides.add_slide(BL); bg(sl)
rect(sl,0,0,13.33,0.08,RP); rect(sl,0,7.42,13.33,0.08,RP); rect(sl,0,2.8,13.33,2.6,RM)
tb(sl,'SEGUNDA ENTREGA',0.5,1.2,12.33,0.8,14,False,RG,PP_ALIGN.CENTER)
tb(sl,'Clustering del Dataset',0.5,2.0,12.33,0.9,36,True,RW,PP_ALIGN.CENTER)
tb(sl,'Secondary Mushroom',0.5,2.9,12.33,0.9,36,True,RP,PP_ALIGN.CENTER)
tb(sl,'ETL  -  K-Means  -  Analisis de Clusters',0.5,4.1,12.33,0.6,16,False,RL,PP_ALIGN.CENTER)
tb(sl,'Universidad Tecnologica Nacional - FRC  |  Ciencias de Datos  |  2026',
   0.5,6.8,12.33,0.5,11,False,RGBColor(0x88,0x88,0xaa),PP_ALIGN.CENTER)

# S2 Contenido
sl=prs.slides.add_slide(BL); bg(sl); rect(sl,0,0,13.33,0.08,RP)
tb(sl,'Contenido',0.5,0.2,12.33,0.8,28,True,RW,PP_ALIGN.CENTER)
bullets(sl,[('1.','Cambios entre el dataset original y el de clustering'),
    ('2.','Como tratamos los valores nulos'),
    ('3.','Que es K-Means y como funciona la clusterizacion'),
    ('4.','Descripcion de los 6 clusters obtenidos')],top=1.3,fs=22)

# S3 Dataset original
sl=prs.slides.add_slide(BL); bg(sl); rect(sl,0,0,13.33,0.08,RP); rect(sl,0,0.08,13.33,0.9,RM)
tb(sl,'1. El Dataset Original',0.5,0.15,12.33,0.75,24,True,RP,PP_ALIGN.LEFT)
bullets(sl,[('>', f'Secondary Mushroom Dataset: {n_orig_rows:,} filas x {n_orig_cols} columnas'),
    ('>','Objetivo original: clasificar hongos como comestibles (e) o venenosos (p)'),
    ('>','Variables: morfologicas + target "class"'),
    ('>',f'Columnas eliminadas (>70% nulos): {", ".join(drop_cols) if drop_cols else "Ninguna"}'),
    ('>',f'{n_dup} filas duplicadas detectadas')],top=1.1,fs=15)
pi(sl,img_nulos,0.3,3.5,12.7)

# S4 Dataset clustering
sl=prs.slides.add_slide(BL); bg(sl); rect(sl,0,0,13.33,0.08,RP); rect(sl,0,0.08,13.33,0.9,RM)
tb(sl,'1. Dataset para Clustering',0.5,0.15,12.33,0.75,24,True,RP,PP_ALIGN.LEFT)
lc,tc=0.4,1.1; cw=[3.5,4.0,5.0]
rows=[('Filas',f'{n_orig_rows:,}',f'{n_final_rows:,}'),('Columnas',str(n_orig_cols),str(n_final_cols)),
    ('Target','class (e/p)','Eliminada'),('Nulos','Sin tratar','Imputados / eliminados'),
    ('Duplicados',str(n_dup),'0')]
hdrs=['Caracteristica','Dataset Original','Dataset Clustering']; yo=tc
for hi,(hdr,hc) in enumerate(zip(hdrs,[RP,RP,RG])):
    rl=lc+sum(cw[:hi]); rect(sl,rl,yo,cw[hi],0.42,hc)
    tb(sl,hdr,rl+0.05,yo+0.05,cw[hi]-0.1,0.38,12,True,RW,PP_ALIGN.CENTER)
yo+=0.44
for ri,row in enumerate(rows):
    rc=RM if ri%2==0 else RGBColor(0x15,0x15,0x28)
    for ci,cell in enumerate(row):
        rl=lc+sum(cw[:ci]); rect(sl,rl,yo,cw[ci],0.38,rc)
        tb(sl,cell,rl+0.05,yo+0.04,cw[ci]-0.1,0.36,11,False,RG if ci==2 else RL,PP_ALIGN.CENTER)
    yo+=0.40
tb(sl,'13 columnas morfologicas:',0.4,yo+0.1,12.5,0.4,13,True,RG)
tb(sl='  -  '.join(COLS_MORFO),*[sl],l=0.4,t=yo+0.55,w=12.5,h=0.6,fs=11,c=RL)

# S5 Nulos
sl=prs.slides.add_slide(BL); bg(sl); rect(sl,0,0,13.33,0.08,RP); rect(sl,0,0.08,13.33,0.9,RM)
tb(sl,'2. Tratamiento de Valores Nulos',0.5,0.15,12.33,0.75,24,True,RP,PP_ALIGN.LEFT)
boxes=[(RG,'Cols. Numericas','Imputadas con\nla MEDIANA','cap-diameter\nstem-height\nstem-width'),
    (RB,'Cols. Categoricas','Imputadas con\nla MODA','shape, color\nsurface, etc.'),
    (RK,'>70% Nulos','Columna\nELIMINADA',', '.join(drop_cols) if drop_cols else 'Ninguna'),
    (RO,'Duplicados',f'{n_dup} filas\nELIMINADAS','Evita sesgo\npor repeticion')]
for i,(c,ti,ac,de) in enumerate(boxes):
    bx=0.4+i*3.2; rect(sl,bx,1.15,3.0,2.8,RM); rect(sl,bx,1.15,3.0,0.55,c)
    tb(sl,ti,bx+0.1,1.18,2.8,0.5,12,True,RD,PP_ALIGN.CENTER)
    tb(sl,ac,bx+0.1,1.75,2.8,0.8,14,True,c,PP_ALIGN.CENTER)
    tb(sl,de,bx+0.1,2.6,2.8,1.2,10,False,RL,PP_ALIGN.CENTER)
tb(sl,'No se usaron 0 para nulos -- distorsionaria distancias euclideanas en el clustering',
   0.4,4.2,12.5,0.5,12,True,RO,PP_ALIGN.CENTER)

# S6 K-Means concepto
sl=prs.slides.add_slide(BL); bg(sl); rect(sl,0,0,13.33,0.08,RP); rect(sl,0,0.08,13.33,0.9,RM)
tb(sl,'3. Que es K-Means',0.5,0.15,12.33,0.75,24,True,RP,PP_ALIGN.LEFT)
tb(sl,'Algoritmo no supervisado que agrupa datos en K clusters sin etiquetas previas. Cada cluster representado por su centroide (promedio de sus puntos).',0.5,1.1,12.33,0.55,14,False,RL)
pi(sl,img_kmeans_diag,0.3,1.75,12.7)

# S7 Pasos K-Means
sl=prs.slides.add_slide(BL); bg(sl); rect(sl,0,0,13.33,0.08,RP); rect(sl,0,0.08,13.33,0.9,RM)
tb(sl,'3. Como funciona K-Means',0.5,0.15,12.33,0.75,24,True,RP,PP_ALIGN.LEFT)
steps=[(RO,'1','Inicializacion','Se eligen K centroides al azar (K-Means++ optimiza la eleccion inicial).'),
    (RG,'2','Asignacion','Cada punto se asigna al centroide mas cercano por distancia euclidiana.'),
    (RB,'3','Actualizacion','Se recalcula cada centroide como promedio de sus puntos asignados.'),
    (RK,'4','Convergencia','Pasos 2-3 se repiten hasta que centroides no cambian (max_iter=500).')]
for i,(c,n,ti,de) in enumerate(steps):
    bx=0.35+i*3.2; rect(sl,bx,1.15,2.9,0.55,c)
    tb(sl,f'{n}. {ti}',bx+0.05,1.18,2.8,0.5,13,True,RD,PP_ALIGN.CENTER)
    rect(sl,bx,1.7,2.9,2.0,RM); tb(sl,de,bx+0.1,1.75,2.7,1.9,11,False,RL)
tb(sl,f'Silhouette: K5={sil5:.4f}  K6={sil6:.4f}  |  Davies-Bouldin: K5={db5:.4f}  K6={db6:.4f}',
   0.35,3.85,12.5,0.4,12,False,RL,PP_ALIGN.CENTER)
tb(sl,'Se eligio K=6 por mejor separabilidad morfologica',0.35,4.3,12.5,0.4,14,True,RO,PP_ALIGN.CENTER)
pi(sl,img_metricas,0.3,4.8,12.7)

# S8 Comparacion K5 K6
sl=prs.slides.add_slide(BL); bg(sl); rect(sl,0,0,13.33,0.08,RP); rect(sl,0,0.08,13.33,0.9,RM)
tb(sl,'3. Comparacion K=5 vs K=6',0.5,0.15,12.33,0.75,24,True,RP,PP_ALIGN.LEFT)
pi(sl,img_scatter_comp,0.3,1.05,12.7)
tb(sl,'Cada punto = 1 hongo. Colores = clusters. Proyeccion 2D via PCA.',0.3,6.5,12.7,0.4,11,False,RGBColor(0x88,0x88,0xaa),PP_ALIGN.CENTER)

# S9 Overview clusters
sl=prs.slides.add_slide(BL); bg(sl); rect(sl,0,0,13.33,0.08,RP); rect(sl,0,0.08,13.33,0.9,RM)
tb(sl,'4. Los 6 Clusters - Resultado Final',0.5,0.15,12.33,0.75,24,True,RP,PP_ALIGN.LEFT)
pi(sl,img_scatter,0.3,1.05,8.0)
for i,(cid,nombre) in enumerate(CLUSTER_NAMES.items()):
    c=CC[cid]; pv=pct6[cid]; nh=sizes6[cid]
    rect(sl,8.5,1.1+i*1.0,4.5,0.85,RM); rect(sl,8.5,1.1+i*1.0,0.25,0.85,c)
    tb(sl,f'C{cid}: {nombre}',8.8,1.12+i*1.0,4.1,0.38,11,True,c)
    tb(sl,f'{nh:,} hongos  {pv:.1f}%',8.8,1.5+i*1.0,4.1,0.3,10,False,RL)

# S10-S15 Un slide por cluster
char_keys={
    0:[('Sombrero','Convexo, marron'),('Superficie','Lisa'),('Anillo','Presente'),('Laminas','Adheridas')],
    1:[('Tamano','Grande'),('Poros','Si (no laminas)'),('Tallo','Grueso, solido'),('Superficie','Irregular')],
    2:[('Superficie','Pegajosa/viscosa'),('Anillo','Ausente'),('Laminas','Libres, claras'),('Tallo','Delgado')],
    3:[('Tamano','Pequeno'),('Anillo','Ausente'),('Laminas','Apretadas'),('Tallo','Fino, fragil')],
    4:[('Forma','Esferica/globosa'),('Color','Amarillo/naranja'),('Tamano','Mediano'),('Frecuencia','Raro')],
    5:[('Tamano','Grande'),('Color','Blanco/crema'),('Superficie','Lisa'),('Anillo','Frecuente')],
}
for cid,nombre in CLUSTER_NAMES.items():
    sl=prs.slides.add_slide(BL); bg(sl); c=CC[cid]
    rect(sl,0,0,13.33,0.08,c); rect(sl,0,0.08,13.33,0.9,RM)
    tb(sl,f'Cluster {cid}',0.5,0.12,2.0,0.7,20,True,c)
    tb(sl,nombre,2.6,0.12,10.0,0.75,22,True,RW)
    pv=pct6[cid]; nh=sizes6[cid]
    rect(sl,0.4,1.1,3.5,0.7,c)
    tb(sl,f'{nh:,} hongos  ({pv:.1f}%)',0.45,1.18,3.4,0.55,13,True,RD,PP_ALIGN.CENTER)
    tb(sl,'Descripcion:',0.4,2.0,5.5,0.4,13,True,c)
    tb(sl,CLUSTER_DESC[cid],0.4,2.4,6.0,2.5,13,False,RL)
    tb(sl,'Caracteristicas clave:',6.7,1.1,6.0,0.4,13,True,c)
    for ki,(cat,val) in enumerate(char_keys.get(cid,[])):
        ry=1.55+ki*0.7; rect(sl,6.7,ry,2.5,0.6,RM); rect(sl,9.3,ry,3.7,0.6,RGBColor(0x15,0x15,0x28))
        tb(sl,cat,6.75,ry+0.08,2.4,0.45,11,True,c,PP_ALIGN.CENTER)
        tb(sl,val,9.35,ry+0.08,3.6,0.45,11,False,RL,PP_ALIGN.CENTER)

# S Final
sl=prs.slides.add_slide(BL); bg(sl)
rect(sl,0,0,13.33,0.08,RP); rect(sl,0,7.42,13.33,0.08,RP); rect(sl,0,2.5,13.33,2.5,RM)
tb(sl,'Conclusion',0.5,1.3,12.33,0.8,20,False,RG,PP_ALIGN.CENTER)
tb(sl,'K = 6 clusters morfologicos',0.5,2.0,12.33,0.9,38,True,RW,PP_ALIGN.CENTER)
tb(sl,f'Silhouette: {sil6:.4f}   |   Davies-Bouldin: {db6:.4f}   |   {n_final_rows:,} hongos analizados',
   0.5,3.1,12.33,0.6,16,False,RL,PP_ALIGN.CENTER)
tb(sl,'Universidad Tecnologica Nacional - FRC  |  Ciencias de Datos  |  2026',
   0.5,6.8,12.33,0.5,11,False,RGBColor(0x88,0x88,0xaa),PP_ALIGN.CENTER)

PPTX_PATH = os.path.join(OUT_DIR,'presentacion_entrega2.pptx')
prs.save(PPTX_PATH)
print(f'PPTX: {PPTX_PATH}', flush=True)
print('DONE', flush=True)
