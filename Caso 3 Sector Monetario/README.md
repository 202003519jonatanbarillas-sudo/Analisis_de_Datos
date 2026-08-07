# Caso 3 - Análisis de la Evolución de los Indicadores Monetarios y Financieros de Guatemala (2015–2025)

## Descripción

Este proyecto presenta un análisis exploratorio de datos (Exploratory Data Analysis - EDA) sobre la evolución de los principales indicadores monetarios y financieros de Guatemala durante el período **2015–2025**.

El proyecto fue desarrollado utilizando **Python, MySQL, Bokeh y LaTeX**, implementando un flujo de trabajo que abarca desde la preparación de los datos hasta la generación automática de un informe técnico, permitiendo identificar tendencias, relaciones entre variables y patrones relevantes para apoyar el análisis macroeconómico y la toma de decisiones.

El estudio se centra en indicadores como el **Producto Interno Bruto (PIB)**, **remesas familiares**, **numerario en circulación**, **medios de pago (M2)**, **crédito bancario al sector privado** y **spreads bancarios**, con el propósito de comprender su comportamiento y evolución a lo largo del tiempo.

---

# Contexto del negocio

El **Banco de Guatemala** requiere monitorear la evolución de los principales indicadores monetarios y financieros del país con el fin de comprender el comportamiento de la liquidez, el crédito al sector privado, las remesas familiares y la actividad económica nacional. La información obtenida permite apoyar el análisis macroeconómico, el seguimiento de la estabilidad financiera y la formulación de políticas económicas y monetarias.

---

# Objetivo general

Analizar la evolución de los principales indicadores monetarios y financieros de Guatemala durante el período **2015–2025** mediante técnicas de análisis exploratorio de datos para identificar tendencias, relaciones entre variables y patrones que contribuyan a la comprensión del crecimiento económico, la liquidez del sistema financiero y el comportamiento de la economía nacional.

---

# Preguntas de negocio

Durante el análisis se buscó responder las siguientes preguntas:

1. ¿Cómo evolucionaron los principales agregados monetarios durante el período 2015–2025?
2. ¿Existe una relación entre el crecimiento del PIB y el crédito bancario al sector privado?
3. ¿Las remesas familiares presentan relación con el crecimiento de los medios de pago (M2)?
4. ¿Cómo evolucionó el spread bancario en moneda nacional y moneda extranjera?
5. ¿Qué indicador presentó el mayor crecimiento durante el período?
6. ¿Cuál ha sido la variación trimestral del PIB?
7. ¿Existe una relación entre el crecimiento de las remesas familiares y el PIB?

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

> ⚠️ **Nota sobre el informe PDF:** Este proyecto fue desarrollado con fines educativos y el motor de automatización de textos en LaTeX se encuentra en fase de mejora continua. Por tal motivo, el documento generado podría presentar algunos errores de redacción, textos repetidos o detalles de formato (espaciados, estructuración de títulos) que aún están siendo optimizados para alcanzar un estándar completamente profesional.

---

# Principales resultados

El análisis permitió identificar los siguientes hallazgos:

- Las **remesas familiares** y el **numerario en circulación** fueron los indicadores que registraron el mayor crecimiento acumulado durante el período analizado, reflejando su importancia dentro de la economía nacional.
- El **Producto Interno Bruto (PIB)** presentó una tendencia de crecimiento sostenido, con una interrupción significativa durante la pandemia de COVID-19 y una posterior recuperación.
- Se identificó una relación positiva entre el **PIB**, el **crédito bancario al sector privado**, los **medios de pago (M2)** y las **remesas familiares**, evidenciando la interacción existente entre la actividad económica, la liquidez y el financiamiento del sector privado.
- El **spread bancario en moneda nacional** mostró un comportamiento más estable que el correspondiente a moneda extranjera, sugiriendo una menor exposición a los efectos de choques internacionales.
- El crecimiento observado en las remesas familiares evidencia su relevancia como fuente de liquidez para la economía guatemalteca, aunque también refleja una importante dependencia de ingresos provenientes del exterior.

---

# Recomendaciones

Como resultado del análisis se proponen las siguientes acciones:

- Mantener un monitoreo continuo de indicadores como las remesas familiares, el numerario en circulación, el crédito bancario y los medios de pago debido a su estrecha relación con el desempeño de la economía.
- Complementar el análisis exploratorio mediante técnicas econométricas y modelos de series de tiempo que permitan cuantificar relaciones de causalidad y realizar proyecciones.
- Utilizar información estadística actualizada del Banco de Guatemala, considerando que las series más recientes pueden estar sujetas a revisiones.
- Promover estudios orientados a fortalecer la inclusión financiera y evaluar mecanismos que reduzcan la dependencia del crecimiento económico respecto a factores externos como las remesas familiares.

---

# Cómo ejecutar el proyecto

1. Clonar este repositorio.

2. Instalar las dependencias:

> **Nota:** Para generar automáticamente el informe técnico es necesario tener instalada una distribución de LaTeX compatible con XeLaTeX (por ejemplo, MiKTeX o TeX Live).

```bash
pip install -r requirements.txt
```

3. Abrir el archivo `caso3.ipynb` utilizando Jupyter Notebook o JupyterLab.

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