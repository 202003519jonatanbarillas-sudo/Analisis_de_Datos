import os
from bokeh.io.export import export_png
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Function Charts

def guardar_grafica(figura, nombre: str, output_dir: str = "../charts") -> None:

    os.makedirs(output_dir, exist_ok=True)
    ruta_archivo = os.path.join(output_dir, f"{nombre}.png")
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1200,800")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options)

    try:
        export_png(figura, filename=ruta_archivo, webdriver=driver)
        print(f"-> Gráfica '{nombre}.png' exportada con éxito en la carpeta"
      f" '{output_dir}/'.")

    except Exception as e:
        print(f"Error exportando '{nombre}': {e}")

    finally:
        driver.quit()
        
def exportar_graficas(CHARTS, output_dir="../charts") -> None:

    os.makedirs(output_dir, exist_ok=True)

    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1200,800")

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options)

    try:
        for nombre, figura in CHARTS.items():
            ruta_archivo = os.path.join( output_dir, f"{nombre}.png")
            export_png(figura, filename=ruta_archivo, webdriver=driver)
            print(f"-> {nombre}.png exportada")

    finally:
        driver.quit()
    print("Todas las gráficas fueron exportadas correctamente.")