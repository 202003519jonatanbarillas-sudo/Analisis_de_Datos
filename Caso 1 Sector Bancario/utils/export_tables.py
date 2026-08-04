import os
import pandas as pd

def guardar_tabla(df: pd.DataFrame, nombre: str, output_dir: str = "tables") -> None:
    """
    Toma un DataFrame de Pandas y exporta un archivo .tex optimizado
    para el estilo ejecutivo institucional (booktabs, alineación derecha).
    """
    os.makedirs(output_dir, exist_ok=True)
    total_filas, total_cols = df.shape
    limite_visualizacion = 10

    if total_filas > limite_visualizacion:
        puntos = pd.DataFrame([["..."] * total_cols], columns=df.columns, index=["..."])
        df_mostrar = pd.concat([df.head(5), puntos, df.tail(5)])
    else:
        df_mostrar = df.copy()

    # Formato de columnas: primera izquierda (l), resto derecha (r) para datos numéricos
    formato_cols = "l" + "r" * total_cols

    # Exportación usando el motor de estilo moderno de Pandas (compatible con booktabs)
    # Se convierte a string previamente para evitar errores con los "..."
    if total_filas > limite_visualizacion:
        for col in df.select_dtypes(include=['float', 'float64']).columns:
            df_mostrar[col] = df_mostrar[col].apply(
                lambda x: f"{x:.2f}" if pd.notnull(x) and isinstance(x, (int, float)) else x
            )

    latex_str = df_mostrar.style.to_latex(
        hrules=True,             # Activa \toprule, \midrule, \bottomrule (booktabs)
        column_format=formato_cols
    )

    # Limpieza del nombre para un título presentable (Ej: "ventas_mensuales" -> "Ventas Mensuales")
    nombre_limpio = nombre.replace("_", " ").title()

    # Pie de nota estilizado con la tipografía y color corporativo
    if total_filas > limite_visualizacion:
        pie_nota = (
            f"\\vspace{{0.15cm}}\n"
            f"\\raggedright{{\\sffamily\\footnotesize\\color{{CorporateGray}}\n"
            f"\\textit{{Nota: Se muestran las primeras y últimas 5 filas. "
            f"Conjunto completo: {total_filas:,} registros $\\times$ {total_cols} variables.}}}}"
        )
    else:
        pie_nota = (
            f"\\vspace{{0.15cm}}\n"
            f"\\raggedright{{\\sffamily\\footnotesize\\color{{CorporateGray}}\n"
            f"\\textit{{Nota: Conjunto completo de datos ({total_filas:,} registros "
            f"$\\times$ {total_cols} variables).}}}}"
        )

    # Ensamblaje del entorno LaTeX
    contenido_final = f"""% Archivo generado automáticamente. No editar a mano.
\\begin{{table}}[htbp]
\\centering
\\begin{{adjustbox}}{{max width=\\textwidth}}
{latex_str.strip()}
\\end{{adjustbox}}
\\caption{{Análisis de datos: {nombre_limpio}}}
\\label{{tab:{nombre}}}
{pie_nota}
\\end{{table}}
"""

    ruta_archivo = os.path.join(output_dir, f"{nombre}.tex")
    with open(ruta_archivo, "w", encoding="utf-8") as f:
        f.write(contenido_final)

    print(f"-> Tabla '{nombre}.tex' exportada con éxito en la carpeta '{output_dir}/'.")


def exportar_tablas(TABLES: dict, output_dir: str = "../tables") -> None:
    for nombre, df in TABLES.items():
        guardar_tabla(df=df, nombre=nombre, output_dir=output_dir)

    print("Todas las tablas fueron exportadas con el nuevo formato institucional.")