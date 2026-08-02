import os
import re
import nbformat
from bs4 import BeautifulSoup

# Function Text

def extraer_textos_notebook(ruta_notebook):
    """
    Extrae las secciones marcadas con:
    <!-- TIPO: XXXXX -->

    Retorna un diccionario con todo el contenido.
    """

    with open(ruta_notebook, "r", encoding="utf-8") as f:
        nb = nbformat.read(f, as_version=4)

    reporte = {}
    for celda in nb.cells:
        if celda.cell_type != "markdown":
            continue

        contenido = celda.source
        patron = r"<!--\s*EXPORT:\s*(.*?)\s*-->"
        encontrado = re.search(patron, contenido)

        if not encontrado:
            continue

        tipo = encontrado.group(1).strip().lower()
        soup = BeautifulSoup(contenido, "html.parser")
        texto = soup.get_text(separator="\n", strip=True)
        reporte.setdefault(tipo, []).append(texto)

    return reporte

def guardar_textos_tex(reporte, output_dir="../text"):
    """
    Guarda los textos extraídos del notebook en archivos .tex.
    """
    # Crear la carpeta si no existe
    os.makedirs(output_dir, exist_ok=True)
    for tipo, bloques in reporte.items():

        for i, texto in enumerate(bloques, start=1):
            nombre = tipo

            if len(bloques) > 1:
                nombre += f"_{i:02d}"   # 01, 02, 03...

            ruta_archivo = os.path.join(output_dir, f"{nombre}.tex")
            with open(ruta_archivo, "w", encoding="utf-8") as f:
                f.write(texto)

            print(f"-> '{nombre}.tex' guardado en '{output_dir}/'")

def exportar_reporte_textos(ruta_notebook):

    reporte = extraer_textos_notebook(ruta_notebook)
    guardar_textos_tex(reporte)

    print("Textos exportados correctamente.")