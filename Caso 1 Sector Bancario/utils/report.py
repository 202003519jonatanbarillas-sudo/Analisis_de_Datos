from pathlib import Path
import re
import subprocess
import shutil

def verificar_existe(ruta: Path, errores: list, tipo: str):
    """
    Verifica la existencia de un archivo o directorio.
    """
    if not ruta.exists():
        errores.append(f"[ERROR] No se encontró el {tipo}: {ruta}")

def obtener_indices(carpeta: Path, patron: str) -> set:
    """
    Busca archivos en la carpeta que coincidan con el patrón regex
    y devuelve un conjunto con los índices encontrados.
    """
    indices = set()
    regex = re.compile(patron)

    if carpeta.exists():
        for archivo in carpeta.iterdir():
            match = regex.match(archivo.name)
            if match:
                indices.add(int(match.group(1)))
    return indices


def verificar_archivos(ROOT=None):
    """
    Verifica que la estructura mínima del proyecto exista antes de
    generar el reporte.
    """
    if ROOT is None:
        try:
            ROOT = Path(__file__).resolve().parent.parent
        except NameError:
            ROOT = Path.cwd()
            if ROOT.name == "notebooks":
                ROOT = ROOT.parent
    errores = []
    advertencias = []

    carpetas = [
        ROOT / "data",
        ROOT / "charts",
        ROOT / "tables",
        ROOT / "text",
        ROOT / "report",
        ROOT / "report" / "latex",
        ROOT / "report" / "latex" / "templates",
        ROOT / "report" / "latex" / "templates" / "sections"
    ]

    for carpeta in carpetas:
        verificar_existe(carpeta, errores, "directorio")

    template = ROOT / "report" / "latex" / "templates"

    archivos_template = [
        "main.tex",
        "variables.tex",
        "comandos.tex",
        "encabezado.tex",
        "estilos.sty"
    ]

    for archivo in archivos_template:
        verificar_existe(template / archivo, errores, "archivo")

    sections = template / "sections"
    archivos_sections = [
        "portada.tex",
        "resumen.tex",
        "introduccion.tex",
        "objetivos.tex",
        "dataset.tex",
        "metodologia.tex",
        "preparacion.tex",
        "resultados.tex",
        "conclusiones.tex",
        "recomendaciones.tex",
        "anexos.tex"
    ]

    for archivo in archivos_sections:
        verificar_existe(sections / archivo, errores, "archivo")

    text = ROOT / "text"
    textos = [
        "titulo.tex",
        "contexto.tex",
        "objetivo.tex",
        "conclusiones.tex",
        "recomendaciones.tex"
    ]

    for archivo in textos:
        verificar_existe(text / archivo, errores, "archivo")

    tables = ROOT / "tables"
    charts = ROOT / "charts"
    verificar_existe(tables / "table.tex", errores, "archivo")
    preguntas = obtener_indices(text, r"pregunta_(\d+)\.tex")
    analisis = obtener_indices(text, r"analisis_(\d+)\.tex")
    tablas = obtener_indices(tables, r"table_ques(\d+)\.tex")
    graficas = obtener_indices(charts, r"chart_ques(\d+)\.png")

    todos = preguntas | analisis | tablas | graficas

    for i in sorted(todos):
        if i not in preguntas:
            errores.append(f"[ERROR] Falta: text/pregunta_{i}.tex")
        if i not in analisis:
            errores.append(f"[ERROR] Falta: text/analisis_{i}.tex")
        if i not in tablas:
            errores.append(f"[ERROR] Falta: tables/table_ques{i}.tex")
        if i not in graficas:
            errores.append(f"[ERROR] Falta: charts/chart_ques{i}.png")

    if errores:
        print("\n" + "=" * 75)
        print("VERIFICACIÓN DE ARCHIVOS")
        print("=" * 75 + "\n")

        for error in errores:
            print(error)

        print("\nNo es posible generar el reporte.\n")
        return False

    print("\n" + "=" * 75)
    print("VERIFICACIÓN DE ARCHIVOS")
    print("=" * 75)
    print("✓ Todos los archivos fueron encontrados.")
    print(f"✓ Preguntas : {len(preguntas)}")
    print(f"✓ Análisis  : {len(analisis)}")
    print(f"✓ Tablas    : {len(tablas)}")
    print(f"✓ Gráficas  : {len(graficas)}")
    print("\nProyecto listo para generar el reporte.\n")
    return True
    
def limpiar_build(ROOT=None):
    """
    Crea la carpeta build si no existe y elimina
    los archivos temporales de compilaciones anteriores.
    """

    if ROOT is None:
        try:
            ROOT = Path(__file__).resolve().parent.parent
        except NameError:
            ROOT = Path.cwd()
            if ROOT.name == "notebooks":
                ROOT = ROOT.parent

    BUILD = ROOT / "report" / "latex" / "build"
    BUILD.mkdir(parents=True, exist_ok=True)

    extensiones = [
        ".aux",
        ".log",
        ".out",
        ".toc",
        ".lof",
        ".lot",
        ".fls",
        ".fdb_latexmk",
        ".synctex.gz",
        ".xdv",
        ".pdf"
    ]

    eliminados = 0

    for archivo in BUILD.iterdir():
        if archivo.is_file():
            if any(archivo.name.endswith(ext) for ext in extensiones):
                archivo.unlink()
                eliminados += 1

    print("\n" + "=" * 75)
    print("LIMPIEZA DE BUILD")
    print("=" * 75)
    print(f"✓ Carpeta: {BUILD}")
    print(f"✓ Archivos eliminados: {eliminados}\n")
    
def compilar_latex(ROOT=None):
    """
    Compila el documento LaTeX utilizando XeLaTeX.
    """

    if ROOT is None:
        try:
            ROOT = Path(__file__).resolve().parent.parent
        except NameError:
            ROOT = Path.cwd()
            if ROOT.name == "notebooks":
                ROOT = ROOT.parent

    TEMPLATE = ROOT / "report" / "latex" / "templates"
    BUILD = ROOT / "report" / "latex" / "build"

    comando = [
        "xelatex",
        "-interaction=nonstopmode",
        "-output-directory",
        str(BUILD),
        "main.tex"
    ]

    print("\n" + "=" * 75)
    print("COMPILANDO REPORTE")
    print("=" * 75)

    for i in range(2):
        resultado = subprocess.run(comando, cwd=TEMPLATE, capture_output=True, text=True)

        if resultado.returncode != 0:
            print("\nERROR DURANTE LA COMPILACIÓN\n")
            print(resultado.stdout)
            print(resultado.stderr)
            return False

    print("✓ Compilación finalizada correctamente.\n")
    return True

def mover_pdf(ROOT=None):
    from pathlib import Path
    import shutil

    if ROOT is None:
        try:
            ROOT = Path(__file__).resolve().parent.parent
        except NameError:
            ROOT = Path.cwd()
            if ROOT.name == "notebooks":
                ROOT = ROOT.parent

    origen = ROOT / "report" / "latex" / "build" / "main.pdf"
    destino = ROOT / "report" / "reporte_final.pdf"

    print("Origen:", origen)
    print("Destino:", destino)

    if not origen.exists():
        print("\nERROR")
        print("No se encontró el PDF generado.\n")
        return False

    shutil.copy2(origen, destino)
    print("=" * 75)
    print("PDF")
    print("=" * 75)
    print(f"✓ PDF copiado a:\n{destino}\n")
    return True

def mostrar_resumen(ROOT=None):
    """
    Muestra un resumen del proceso de generación del reporte.
    """
    if ROOT is None:
        try:
            ROOT = Path(__file__).resolve().parent.parent
        except NameError:
            ROOT = Path.cwd()
            if ROOT.name == "notebooks":
                ROOT = ROOT.parent

    pdf = ROOT / "report" / "reporte_final.pdf"
    print("\n" + "=" * 75)
    print("           REPORTE GENERADO CORRECTAMENTE")
    print("=" * 75)
    print("✓ Verificación de archivos")
    print("✓ Limpieza del directorio build")
    print("✓ Compilación LaTeX")
    print("✓ Copia del PDF")
    print("\nArchivo generado:")
    print(f"   {pdf}")
    print("\nProceso finalizado correctamente.\n") 

def generar_reporte():
    """
    Ejecuta todo el proceso de generación del reporte.
    """
    if not verificar_archivos():
        return

    limpiar_build()

    compilar_latex()
    compilar_latex()

    if not mover_pdf():
        return

    mostrar_resumen()
    
if __name__ == "__main__":
    generar_reporte()
