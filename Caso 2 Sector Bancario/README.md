# Caso 2 - Análisis de los Factores Asociados a la Mora Crediticia (Pendiente de implementar automatizacion del informe)

## Descripción

Este proyecto presenta un análisis exploratorio de datos (Exploratory Data Analysis - EDA) desarrollado para una institución bancaria ficticia con el objetivo de comprender los factores asociados al incumplimiento de pago (mora) de los clientes con créditos activos.

El proyecto fue desarrollado utilizando **Python, MySQL, Bokeh y LaTeX**, implementando un flujo de trabajo que abarca desde la preparación de los datos hasta la generación automática de un informe técnico, permitiendo identificar patrones relacionados con el comportamiento crediticio y generar información útil para apoyar la gestión del riesgo y la toma de decisiones.

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
3. ¿Existe una relación entre el ingreso mensual y el monto del préstamo otorgado?
4. ¿Cómo varía la antigüedad laboral entre clientes con y sin mora?
5. ¿Qué grupos de edad presentan una mayor concentración de clientes en mora?

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

> **Nota:** Para generar automáticamente el informe técnico es necesario tener instalada una distribución de LaTeX compatible con XeLaTeX (por ejemplo, MiKTeX o TeX Live).

```bash
pip install -r requirements.txt
```

3. Abrir el archivo `caso2.ipynb` utilizando Jupyter Notebook o JupyterLab.

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