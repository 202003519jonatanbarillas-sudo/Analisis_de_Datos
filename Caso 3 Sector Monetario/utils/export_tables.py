import os
import pandas as pd

# Function Dataframes 

def guardar_tabla(df: pd.DataFrame, nombre: str, output_dir: str = "tables") -> None:
  """Toma un DataFrame de Pandas, aplica el formato de vista previa tipo Jupyter

  (si es muy grande) o completo (si es pequeño), y exporta un archivo .tex
  con formato profesional usando booktabs.
  """
  os.makedirs(output_dir, exist_ok=True)
  total_filas, total_cols = df.shape
  limite_visualizacion = 10 

  if total_filas > limite_visualizacion:
    puntos = pd.DataFrame([["..."] * total_cols], columns=df.columns, index=["..."])
    df_mostrar = pd.concat([df.head(5), puntos, df.tail(5)])
  else:
    df_mostrar = df.copy()

  latex_str = df_mostrar.to_latex(index=True, escape=True, column_format="l" + "c" * total_cols, float_format="%.2f")

  if total_filas > limite_visualizacion:
    pie_nota = (
        f"\\smallskip\\textit{{Mostrando las primeras 5 y últimas 5 filas"
        f" de un total de {total_filas:,} registros $\\times$ {total_cols}"
        " variables.}}"
    )
  else:
    pie_nota = (
        f"\\smallskip\\textit{{Conjunto completo de datos: {total_filas:,}"
        f" registros $\\times$ {total_cols} variables.}}"
    )

  contenido_final = f"""% Archivo generado automáticamente. No editar a mano.
\\begin{{table}}[htbp]
\\centering
\\begin{{adjustbox}}{{max width=\\textwidth}}
{latex_str}
\\end{{adjustbox}}
\\caption{{Resultado de la variable: \\texttt{{{nombre}}}}}
\\label{{tab:{nombre}}}
{pie_nota}
\\end{{table}}
"""
  ruta_archivo = os.path.join(output_dir, f"{nombre}.tex")
  with open(ruta_archivo, "w", encoding="utf-8") as f:
    f.write(contenido_final)

  print(
      f"-> Tabla '{nombre}.tex' exportada con éxito en la carpeta"
      f" '{output_dir}/'."
  )

def exportar_tablas(TABLES: dict, output_dir: str = "../tables") -> None:
    """
    Exporta todos los DataFrames almacenados en un diccionario.
    """

    for nombre, df in TABLES.items():

        guardar_tabla(
            df=df,
            nombre=nombre,
            output_dir=output_dir
        )

    print("Todas las tablas fueron exportadas correctamente.")