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

    formato_cols = "l" * total_cols

    latex_str = df_mostrar.to_latex(
        index=False,
        escape=True,
        float_format="%.2f",
        column_format=formato_cols,
        longtable=False
    )

    nombre_limpio = nombre.replace("_", " ").title()

    if total_filas > limite_visualizacion:
        pie_nota = (
            f"\\vspace{{0.15cm}}\n"
            f"\\raggedright{{\\sffamily\\footnotesize\\color{{ThemeMuted}}\n"
            f"\\textit{{Nota: Se muestran las primeras y últimas 5 filas. "
            f"Conjunto completo: {total_filas:,} registros $\\times$ {total_cols} variables.}}}}"
        )
    else:
        pie_nota = (
            f"\\vspace{{0.15cm}}\n"
            f"\\raggedright{{\\sffamily\\footnotesize\\color{{ThemeMuted}}\n"
            f"\\textit{{Nota: Conjunto completo de datos ({total_filas:,} registros "
            f"$\\times$ {total_cols} variables).}}}}"
        )


    contenido_final = f"""% Archivo generado automáticamente. No editar a mano.
\\begin{{table}}[htbp]
\\centering
\\begin{{adjustbox}}{{max width=\\textwidth}}
{latex_str.strip()}
\\end{{adjustbox}}
\\caption{{{nombre_limpio}}}
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