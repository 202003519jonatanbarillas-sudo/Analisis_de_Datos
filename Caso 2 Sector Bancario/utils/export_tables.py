import os
import pandas as pd


def guardar_tabla(df: pd.DataFrame, nombre: str, output_dir: str = "tables") -> None:
    """
    Exporta un DataFrame a LaTeX con estilo ejecutivo:
    - Cabecera negra con texto dorado.
    - Cuerpo limpio.
    - Nota metodológica inferior.
    """

    os.makedirs(output_dir, exist_ok=True)

    total_filas, total_cols = df.shape
    limite_visualizacion = 10


    #------------------------------------------
    # Reducir tabla si es demasiado grande
    #------------------------------------------

    if total_filas > limite_visualizacion:

        puntos = pd.DataFrame(
            [["..."] * total_cols],
            columns=df.columns,
            index=["..."]
        )

        df_mostrar = pd.concat(
            [
                df.head(5),
                puntos,
                df.tail(5)
            ]
        )

    else:

        df_mostrar = df.copy()



    #------------------------------------------
    # Formato columnas
    #------------------------------------------

    formato_cols = "l" * total_cols



    #------------------------------------------
    # Exportar LaTeX
    #------------------------------------------

    latex_str = df_mostrar.to_latex(
        index=False,
        escape=True,
        float_format="%.2f",
        column_format=formato_cols,
        longtable=False
    )



    #------------------------------------------
    # Estilo cabecera tabla
    #------------------------------------------

    lineas = latex_str.splitlines()
    
    for i, linea in enumerate(lineas):
    
        if "\\toprule" in linea:
    
            cabecera = lineas[i+1]
    
            columnas = cabecera.replace("\\\\", "").split("&")
    
            cabecera_formateada = (
                "\\rowcolor{ThemeBackground}\n"
                "\\rule{0pt}{0.45cm}\n"
                +
                " & ".join(
                    [
                        "\\textcolor{ThemeGold}{\\bfseries "
                        + col.strip()
                        + "}"
                        for col in columnas
                    ]
                )
                +
                " \\\\"
            )
    
            lineas[i] = ""

            lineas[i+1] = cabecera_formateada
    
            break
    
    
    latex_str = "\n".join(lineas)
    
    latex_str = latex_str.replace("\\midrule", "")
    nombre_limpio = nombre.replace("_", " ").title()



    #------------------------------------------
    # Nota inferior
    #------------------------------------------

    if total_filas > limite_visualizacion:

        pie_nota = (
            f"\\vspace{{0.15cm}}\n"
            f"{{\\raggedright\\sffamily\\footnotesize"
            f"\\color{{ThemeMuted}}\n"
            f"\\textit{{Nota: Se muestran las primeras y últimas 5 filas. "
            f"Conjunto completo: {total_filas:,} registros "
            f"$\\times$ {total_cols} variables.}}}}"
        )

    else:

        pie_nota = (
            f"\\vspace{{0.15cm}}\n"
            f"{{\\raggedright\\sffamily\\footnotesize"
            f"\\color{{ThemeMuted}}\n"
            f"\\textit{{Nota: Conjunto completo de datos "
            f"({total_filas:,} registros "
            f"$\\times$ {total_cols} variables).}}}}"
        )



    #------------------------------------------
    # Archivo TEX final
    #------------------------------------------

    contenido_final = f"""
% Archivo generado automáticamente. No editar manualmente.

\\begin{{table}}[htbp]

\\centering

\\begin{{adjustbox}}{{max width=\\textwidth}}

{latex_str.strip()}

\\end{{adjustbox}}

{pie_nota}

\\end{{table}}
"""



    ruta_archivo = os.path.join(
        output_dir,
        f"{nombre}.tex"
    )


    with open(
        ruta_archivo,
        "w",
        encoding="utf-8"
    ) as f:

        f.write(contenido_final)



    print(
        f"-> Tabla '{nombre}.tex' exportada correctamente en '{output_dir}/'."
    )


def exportar_tablas(TABLES: dict, output_dir: str = "../tables") -> None:

    for nombre, df in TABLES.items():

        guardar_tabla(
            df=df,
            nombre=nombre,
            output_dir=output_dir
        )


    print(
        "Todas las tablas fueron exportadas con el estilo institucional."
    )