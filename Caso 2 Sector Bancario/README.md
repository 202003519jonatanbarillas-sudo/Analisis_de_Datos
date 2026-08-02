# Caso 2 - Análisis Exploratorio de los Factores Asociados a la Mora Crediticia

## Descripción

Este proyecto presenta un análisis exploratorio de datos (Exploratory Data Analysis - EDA) desarrollado para una institución bancaria ficticia con el objetivo de comprender los factores asociados al incumplimiento de pago (mora) de los clientes con créditos activos.

El análisis fue realizado utilizando Python, MySQL y Bokeh, aplicando técnicas de limpieza, exploración y visualización de datos para identificar patrones relacionados con el comportamiento crediticio y generar información que apoye la gestión del riesgo y la toma de decisiones.

---

# Contexto del negocio

Banco Capital GT busca fortalecer su proceso de evaluación crediticia mediante el análisis de las características demográficas, laborales y financieras de sus clientes. La Gerencia de Riesgos desea identificar patrones asociados al incumplimiento de pago (mora) con el propósito de mejorar las políticas de otorgamiento de créditos y fortalecer la administración del riesgo crediticio.

---

# Objetivo general

Analizar las características financieras, laborales y demográficas de los clientes con créditos activos mediante técnicas de análisis exploratorio de datos para identificar patrones asociados a la mora y generar información que contribuya a una mejor gestión del riesgo crediticio.

---

# Preguntas de negocio

Durante el análisis se buscó responder las siguientes preguntas:

1. ¿Cuál es la distribución de clientes con y sin mora?
2. ¿Qué sectores laborales presentan una mayor proporción de clientes en mora?
3. ¿Existe relación entre el ingreso mensual y el monto del préstamo otorgado?
4. ¿Cómo varía la antigüedad laboral entre clientes con y sin mora?
5. ¿Qué grupos de edad presentan una mayor concentración de clientes en mora?

---

# Metodología

El proyecto fue desarrollado siguiendo un flujo de trabajo de análisis exploratorio de datos (EDA), compuesto por las siguientes etapas:

1. Comprensión del problema de negocio y definición de las preguntas de análisis.
2. Creación e importación de la base de datos en MySQL.
3. Limpieza, validación y preparación de los datos utilizando consultas SQL.
4. Exportación del conjunto de datos limpio a formato CSV.
5. Importación del archivo CSV en Python mediante Pandas.
6. Análisis exploratorio de los datos utilizando estadísticas descriptivas y agregaciones.
7. Construcción de visualizaciones interactivas con Bokeh para responder las preguntas de negocio.
8. Interpretación de los resultados obtenidos.
9. Elaboración de conclusiones y recomendaciones orientadas a la toma de decisiones.

---

# Tecnologías utilizadas

- Python
- Pandas
- NumPy
- MySQL
- Bokeh
- Jupyter Lab

---

# Archivos del proyecto

| Archivo | Descripción |
|----------|-------------|
| `caso2.ipynb` | Desarrollo completo del análisis. |
| `caso_2_lim.csv` | Base de datos utilizada durante el análisis. |
| `caso_2_lim.sql` | Script opcional de la base de datos en MySQL. |
| `requirements.txt` | Librerías necesarias para ejecutar el proyecto. |
| `img/` | Imágenes de las visualizaciones utilizadas en el proyecto. |

---

# Principales resultados

El análisis exploratorio permitió identificar los siguientes hallazgos:

- La cartera de créditos presenta una tasa de mora del **12.7%**, equivalente a 127 clientes de una muestra de 1,000 registros.
- La distribución de clientes en mora entre los distintos sectores laborales es relativamente homogénea, sin evidenciar un sector económico que concentre significativamente un mayor riesgo de incumplimiento.
- No se identificó una relación lineal claramente definida entre el ingreso mensual de los clientes y el monto del préstamo otorgado.
- La antigüedad laboral presenta una distribución similar entre clientes con y sin mora, por lo que esta variable, analizada de forma individual, muestra un bajo poder explicativo sobre el incumplimiento de pago.
- La mayor concentración de clientes en mora se encuentra en los grupos de edad comprendidos entre **20 y 64 años**; sin embargo, el análisis descriptivo no permite afirmar que la edad sea un factor determinante del riesgo crediticio.

---

# Recomendaciones

Como resultado del análisis se proponen las siguientes acciones:

- Complementar el análisis exploratorio mediante técnicas estadísticas y modelos predictivos que permitan identificar los factores con mayor capacidad explicativa sobre la mora.
- Incorporar variables adicionales relacionadas con el comportamiento crediticio, como historial de pagos, nivel de endeudamiento, relación cuota-ingreso, calificación de riesgo e información financiera del cliente.
- Implementar indicadores de seguimiento que permitan monitorear periódicamente la evolución de la tasa de mora y detectar oportunamente cambios en el comportamiento de la cartera.
- Fortalecer las políticas de evaluación y otorgamiento de créditos apoyándose en análisis de datos y evidencia estadística para mejorar la gestión del riesgo crediticio.

---

# Cómo ejecutar el proyecto

1. Clonar este repositorio.

2. Instalar las dependencias:

```bash
pip install -r requirements.txt
```

3. Abrir el archivo `caso2.ipynb` utilizando JupyterLab o Jupyter Notebook.

4. Ejecutar las celdas del notebook. El proyecto utiliza el archivo `caso_2_lim.csv` incluido en este repositorio, por lo que no es necesario configurar una base de datos.
```


# Autor

**Javier Barillas**

Estudiante de Economía | Analista de Datos

Proyecto desarrollado con fines educativos y de construcción de portafolio profesional.