# Caso 4 - Análisis del Rendimiento de las Empresas con Mayor Capitalización Bursátil (2018–2023) (Pendiente de implementar automatizacion del informe)

## Descripción

Este proyecto presenta un análisis exploratorio de datos (Exploratory Data Analysis - EDA) sobre el comportamiento histórico de las principales empresas con mayor capitalización bursátil del mercado estadounidense durante el período **2018–2023**.

El proyecto fue desarrollado utilizando **Python, MySQL, Bokeh y LaTeX**, implementando un flujo de trabajo que abarca desde la preparación de los datos hasta la generación automática de un informe técnico, permitiendo identificar patrones de crecimiento, volatilidad, liquidez y rendimiento acumulado que apoyen el análisis financiero y la toma de decisiones de inversión.

---

# Contexto del negocio

Una firma de inversión desea comprender el comportamiento histórico de las principales empresas que cotizan en el mercado bursátil estadounidense con el objetivo de identificar patrones de crecimiento, volatilidad y actividad de negociación que sirvan como apoyo para futuros análisis financieros y la toma de decisiones de inversión.

---

# Objetivo general

Analizar el comportamiento histórico del precio de las acciones, el volumen de negociación y el rendimiento acumulado de las principales empresas del mercado bursátil estadounidense durante el período **2018–2023** mediante técnicas de análisis exploratorio de datos para identificar tendencias, niveles de volatilidad y diferencias entre compañías.

---

# Preguntas de negocio

Durante el análisis se buscó responder las siguientes preguntas:

1. ¿Cuáles empresas obtuvieron el mayor rendimiento acumulado?
2. ¿Cómo evolucionó el precio de cierre de las empresas con mayor rendimiento acumulado?
3. ¿Cómo se distribuyen los rendimientos diarios de las empresas con mayor rendimiento acumulado?
4. ¿Qué empresas registran los mayores volúmenes de negociación?
5. ¿Cómo se relacionan el volumen negociado y el precio de cierre?
6. ¿Cuál fue el rendimiento mensual promedio de cada empresa?
7. ¿Qué tan consistentes fueron los rendimientos diarios de las empresas con mayor rendimiento acumulado?

---

# Metodología

El proyecto fue desarrollado siguiendo un flujo de trabajo orientado a garantizar la calidad de los datos y la reproducibilidad del análisis, compuesto por las siguientes etapas:

1. Obtención del conjunto de datos.
2. Evaluación inicial mediante un análisis exploratorio (EDA) para conocer el estado de la información.
3. Limpieza, transformación y preparación de los datos utilizando MySQL.
4. Exportación del conjunto de datos preparado.
5. Validación del conjunto de datos mediante un segundo análisis exploratorio.
6. Desarrollo del análisis para responder las preguntas de negocio.
7. Generación automática de tablas, figuras y textos utilizados en el informe.
8. Elaboración automática del informe técnico en LaTeX.

---

# Tecnologías utilizadas

- Python
- Pandas
- NumPy
- SciPy
- Scikit-Learn
- MySQL
- Bokeh
- LaTeX (XeLaTeX)
- Jupyter Notebook

---

# Estructura del proyecto

| Archivo / Carpeta | Descripción |
|-------------------|-------------|
| `notebooks/` | Contiene los notebooks del proyecto, incluyendo el desarrollo completo del caso de estudio y el EDA automático. |
| `data/` | Conjunto de datos utilizado durante el análisis. |
| `charts/` | Gráficas exportadas automáticamente para el informe. |
| `tables/` | Tablas exportadas automáticamente en formato LaTeX. |
| `text/` | Textos exportados automáticamente para el informe técnico. |
| `utils/` | Funciones reutilizables para exportación de recursos y generación automática del reporte. |
| `report/` | Reportes generados por el proyecto, incluyendo el EDA en HTML y el informe técnico en LaTeX/PDF. |
| `README.md` | Documentación general del proyecto. |
| `requirements.txt` | Dependencias necesarias para ejecutar el proyecto. |

---

# Automatización

El proyecto incorpora un proceso de automatización para la generación del informe técnico. Al finalizar la ejecución del análisis se realizan automáticamente las siguientes tareas:

- Exportación de tablas en formato LaTeX.
- Exportación de figuras utilizadas en el análisis.
- Exportación de los textos empleados en el informe.
- Verificación de la estructura del proyecto.
- Compilación automática del documento LaTeX.
- Generación del informe técnico final en formato PDF.

Esta arquitectura permite separar el análisis de datos de la documentación, facilitando la reutilización del flujo de trabajo en futuros casos de estudio.

---

# Informe generado

Como resultado del proceso automatizado se genera un informe técnico en formato PDF que documenta:

- El contexto y objetivo del caso de estudio.
- La metodología empleada.
- La preparación y transformación de los datos.
- El análisis desarrollado para cada pregunta de negocio.
- Las conclusiones y recomendaciones finales.

El informe se construye automáticamente utilizando una plantilla desarrollada en LaTeX.

---

# Principales resultados

El análisis permitió identificar los siguientes hallazgos:

- **NVIDIA** obtuvo el mayor rendimiento acumulado durante el período analizado, mientras que **Tesla** y **BioNTech** también registraron crecimientos sobresalientes, aunque acompañados de una mayor volatilidad.
- La evolución del precio de cierre mostró que un alto rendimiento no implica necesariamente un comportamiento altamente inestable. NVIDIA presentó un crecimiento más sostenido, mientras que BioNTech experimentó fuertes incrementos seguidos de importantes correcciones.
- Los análisis de volatilidad y rendimientos diarios evidenciaron que **BioNTech**, **Tesla** y **PDD Holdings** registraron la mayor dispersión en sus retornos, mientras que empresas como **Synopsys**, **KLA**, **Cadence Design Systems**, **Fair Isaac** y **ARES Management** mostraron un comportamiento considerablemente más estable.
- **Tesla**, **Apple** y **AMD** concentraron los mayores volúmenes de negociación del conjunto analizado, reflejando elevados niveles de liquidez en el mercado.
- No se identificó una relación lineal claramente definida entre el volumen negociado y el precio de cierre, lo que sugiere que ambas variables responden a factores diferentes del comportamiento bursátil.
- El análisis mensual permitió identificar patrones estacionales compartidos entre las empresas, aunque la magnitud de los rendimientos varía considerablemente entre compañías.

---

# Recomendaciones

Como resultado del análisis se proponen las siguientes acciones:

- Complementar el análisis exploratorio mediante indicadores financieros que permitan evaluar el rendimiento ajustado por riesgo.
- Incorporar variables fundamentales como ingresos, utilidades, capitalización bursátil, tasas de interés e indicadores macroeconómicos para comprender mejor el comportamiento de las acciones.
- Profundizar en el estudio de la relación entre precio y volumen mediante análisis de correlación y modelos de regresión.
- Realizar análisis por subperíodos o eventos relevantes, como la pandemia de COVID-19, cambios en política monetaria o publicación de resultados financieros.
- Utilizar los resultados obtenidos como base para desarrollar modelos predictivos y estrategias de inversión que integren rendimiento esperado, volatilidad y liquidez.

---

# Cómo ejecutar el proyecto

1. Clonar este repositorio.

2. Instalar las dependencias:

> **Nota:** Para generar automáticamente el informe técnico es necesario tener instalada una distribución de LaTeX compatible con XeLaTeX (por ejemplo, MiKTeX o TeX Live).

```bash
pip install -r requirements.txt
```

3. Abrir el archivo `caso4.ipynb` utilizando Jupyter Notebook o JupyterLab.

4. Ejecutar todas las celdas del notebook.

Al finalizar la ejecución se generarán automáticamente:

- El conjunto de tablas en formato LaTeX.
- Las figuras utilizadas en el análisis.
- Los textos del informe.
- El informe técnico final en formato PDF.

---

# Autor

**Javier Barillas**

Estudiante de Economía | Analista de Datos

Proyecto desarrollado con fines educativos y como parte de un portafolio profesional de análisis de datos.