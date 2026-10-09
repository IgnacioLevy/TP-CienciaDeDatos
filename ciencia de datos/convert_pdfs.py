import os
import pymupdf

recursos_dir = r"d:\Cathy\Documentos\ciencia de datos\recursos"
output_dir = r"d:\Cathy\Documentos\ciencia de datos\docs"

os.makedirs(output_dir, exist_ok=True)

pdf_files = [f for f in os.listdir(recursos_dir) if f.lower().endswith(".pdf")]

print(f"Found {len(pdf_files)} PDF files to convert.")

for pdf_file in pdf_files:
    pdf_path = os.path.join(recursos_dir, pdf_file)
    md_name = os.path.splitext(pdf_file)[0] + ".md"
    md_path = os.path.join(output_dir, md_name)
    
    print(f"Converting {pdf_file} -> {md_name}...")
    doc = pymupdf.open(pdf_path)
    
    md_content = [f"# {os.path.splitext(pdf_file)[0]}\n"]
    
    for page_num in range(len(doc)):
        page = doc[page_num]
        # try markdown format or fallback to text
        try:
            text = page.get_text("markdown")
        except Exception:
            text = page.get_text("text")
        
        md_content.append(f"## Página {page_num + 1}\n")
        md_content.append(text if text else "(Página sin texto reconocible)\n")
        md_content.append("\n---\n")
    
    doc.close()
    
    with open(md_path, "w", encoding="utf-8") as f:
        f.write("\n".join(md_content))

print("Conversion complete!")
