"""
Extrae todas las celdas de código del notebook y las ejecuta
guardando los gráficos en la carpeta 'resultado 1'.
"""
import json, os, sys

NOTEBOOK_PATH = r"d:\Cathy\Documentos\ciencia de datos\implementacion\clustering_hongos_entrega2.ipynb"
OUTPUT_DIR    = r"d:\Cathy\Documentos\ciencia de datos\implementacion\resultado 1"

os.makedirs(OUTPUT_DIR, exist_ok=True)

with open(NOTEBOOK_PATH, encoding="utf-8") as f:
    nb = json.load(f)

code_cells = [
    "".join(cell["source"])
    for cell in nb["cells"]
    if cell["cell_type"] == "code" and cell["source"]
]

# Unir todo el código y parchear la ruta de salida y de datos
full_code = "\n\n".join(code_cells)
full_code = full_code.replace(
    "DATA_PATH  = r'recursos/secondary_data.csv'",
    r"DATA_PATH  = r'd:\Cathy\Documentos\ciencia de datos\recursos\secondary_data.csv'"
)
full_code = full_code.replace(
    "OUTPUT_DIR = r'implementacion/graficos_notebook'",
    f"OUTPUT_DIR = r'{OUTPUT_DIR}'"
)
# Reemplazar plt.show() por nada (no hay GUI en modo script)
full_code = full_code.replace("plt.show()", "pass  # plt.show() desactivado en modo script")

# Guardar script generado para referencia
script_path = os.path.join(OUTPUT_DIR, "_notebook_ejecutado.py")
with open(script_path, "w", encoding="utf-8") as f:
    f.write(full_code)

print(f"Script generado: {script_path}")
print(f"Ejecutando {len(code_cells)} celdas de código...\n")

exec(compile(full_code, "<notebook>", "exec"))
print(f"\nTodos los resultados guardados en:\n  {OUTPUT_DIR}")
