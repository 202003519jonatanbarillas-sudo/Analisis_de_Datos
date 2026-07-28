# Caso 3 - Análisis de la Evolución de los Indicadores Monetarios y Financieros de Guatemala (2015–2025) 

## Descripción

Este proyecto presenta un **Análisis Exploratorio de Datos (EDA)** sobre la evolución de los principales indicadores monetarios y financieros de Guatemala durante el período **2015–2025**. El estudio fue desarrollado utilizando **Python**, **MySQL** y **Bokeh**, aplicando técnicas de limpieza, transformación, análisis y visualización de datos para identificar tendencias, relaciones entre variables y patrones relevantes para la toma de decisiones económicas.

El análisis se centra en indicadores como el **Producto Interno Bruto (PIB)**, **remesas familiares**, **numerario en circulación**, **medios de pago (M2)**, **crédito bancario al sector privado** y **spreads bancarios**, con el propósito de comprender su comportamiento y evolución a lo largo del tiempo.

---

# Contexto del negocio

El **Banco de Guatemala** requiere monitorear la evolución de los principales indicadores monetarios y financieros del país con el fin de comprender el comportamiento de la liquidez, el crédito al sector privado, las remesas familiares y la actividad económica nacional. La información obtenida permite apoyar el análisis macroeconómico, el seguimiento de la estabilidad financiera y la formulación de políticas económicas y monetarias.

---

# Objetivo general

Analizar la evolución de los principales indicadores monetarios y financieros de Guatemala durante el período **2015–2025** mediante técnicas de análisis exploratorio de datos, con el propósito de identificar tendencias, relaciones entre variables y patrones que contribuyan a la comprensión del crecimiento económico, la liquidez del sistema financiero y el comportamiento de la economía nacional.

---

# Preguntas de negocio

Durante el análisis se buscó responder las siguientes preguntas:

1. ¿Cómo evolucionó el saldo total administrado por el banco durante 2025?
2. ¿Qué sucursales concentran el mayor saldo de los clientes?
3. ¿Qué segmentos de clientes concentran los mayores saldos?
4. ¿Existe una relación entre el ingreso de los clientes y el saldo disponible en sus cuentas?
5. ¿Qué grupos de edad concentran el mayor saldo administrado por el banco durante 2025?

---

# Metodología

El proyecto fue desarrollado siguiendo un flujo de trabajo de análisis exploratorio de datos (EDA), compuesto por las siguientes etapas:

1. ¿Cómo evolucionaron los principales agregados monetarios durante el período?
2. ¿Existe relación entre el crecimiento del PIB y el crédito bancario al sector privado?
3. ¿Las remesas familiares presentan relación con el crecimiento de los medios de pago (M2)?
4. ¿Cómo evolucionó el spread bancario en moneda nacional y moneda extranjera?
5. ¿Qué indicador presentó el mayor crecimiento durante el período?
6. ¿Cuál ha sido la variación trimestral del PIB?
7. ¿Existe una relación entre el crecimiento de las remesas y el PIB?

---

# Tecnologías utilizadas

- Python
- Pandas
- NumPy
- Bokeh
- Jupyter Lab

---

# Archivos del proyecto

| Archivo | Descripción |
|----------|-------------|
| `caso1.ipynb` | Desarrollo completo del análisis. |
| `caso_1_limpios.csv` | Base de datos utilizada durante el análisis. |
| `requirements.txt` | Librerías necesarias para ejecutar el proyecto. |
| `img/` | Imágenes de las visualizaciones utilizadas en el proyecto. |

---

# Principales resultados

El análisis de los indicadores monetarios y financieros de Guatemala para el período **2015–2025** permitió identificar los siguientes hallazgos:

* Las **remesas familiares** y el **numerario en circulación** fueron los indicadores que registraron el mayor crecimiento acumulado durante el período analizado, reflejando su importancia dentro de la economía nacional.
* El **Producto Interno Bruto (PIB)** presentó una tendencia de crecimiento sostenido, con una interrupción significativa únicamente durante la pandemia de COVID-19, recuperando posteriormente su patrón de crecimiento.
* Se identificó una **relación positiva** entre el PIB, el crédito bancario, los medios de pago (M2) y las remesas familiares, evidenciando la interacción existente entre la actividad económica, la liquidez y el financiamiento del sector privado.
* El **spread bancario en moneda nacional** mostró un comportamiento más estable que el correspondiente a moneda extranjera, sugiriendo una menor exposición a los efectos de los choques internacionales.
* El crecimiento observado en las remesas familiares evidencia su relevancia como fuente de liquidez para la economía guatemalteca, aunque también pone de manifiesto una importante dependencia de ingresos provenientes del exterior.

---

# Recomendaciones

A partir de los resultados obtenidos se proponen las siguientes recomendaciones:

* Mantener un monitoreo continuo de indicadores como las remesas familiares, el numerario en circulación, el crédito bancario y los medios de pago, debido a su estrecha relación con el desempeño de la economía.
* Complementar el análisis exploratorio mediante técnicas econométricas y modelos de series de tiempo que permitan cuantificar relaciones de causalidad y realizar proyecciones.
* Utilizar información estadística actualizada del Banco de Guatemala, considerando que las series más recientes pueden estar sujetas a revisiones.
* Promover estudios orientados a fortalecer la inclusión financiera y evaluar mecanismos que reduzcan la dependencia del crecimiento económico respecto a factores externos como las remesas familiares.

---


---

# Cómo ejecutar el proyecto

1. Clonar este repositorio.

2. Instalar las dependencias:

```bash
pip install -r requirements.txt
```

3. Abrir el archivo `caso1.ipynb` utilizando JupyterLab o Jupyter Notebook.

4. Ejecutar las celdas del notebook. El proyecto utiliza el archivo `caso_1_limpios.csv` incluido en este repositorio, por lo que no es necesario configurar una base de datos.
```


# Autor

**Javier Barillas**

Estudiante de Economía | Analista de Datos

Proyecto desarrollado con fines educativos y de construcción de portafolio profesional.