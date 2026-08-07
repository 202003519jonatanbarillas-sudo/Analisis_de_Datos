# Caso 1 - Análisis del Comportamiento de los Saldos Bancarios durante 2025 

## Descripción

Este proyecto presenta un análisis exploratorio de datos (Exploratory Data Analysis - EDA) desarrollado para una institución bancaria ficticia con el objetivo de comprender el comportamiento de los saldos bancarios de sus clientes durante el año 2025.

El proyecto fue desarrollado utilizando **Python, MySQL, Bokeh y LaTeX**, implementando un flujo de trabajo que abarca desde la preparación de los datos hasta la generación automática de un informe técnico, permitiendo obtener información útil para apoyar la toma de decisiones comerciales.

---

# Contexto del negocio

Banco Capital GT desea comprender el comportamiento de los saldos de las cuentas de sus clientes durante el año 2025. La gerencia busca identificar patrones temporales, diferencias entre sucursales, segmentos de clientes y grupos de edad con el propósito de fortalecer la toma de decisiones comerciales y mejorar la gestión de su cartera de clientes.

---

# Objetivo general

Analizar el comportamiento de los saldos bancarios registrados durante el año 2025 mediante técnicas de análisis exploratorio de datos para identificar patrones, diferencias entre segmentos de clientes y oportunidades que contribuyan a la toma de decisiones.

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

| Archivo / Carpeta  | Descripción                                                                                                     |
| ------------------ | --------------------------------------------------------------------------------------------------------------- |
| `notebooks/`       | Contiene los notebooks del proyecto, incluyendo el desarrollo completo del caso de estudio y el EDA automático. |
| `data/`            | Conjunto de datos utilizado durante el análisis.                                                                |
| `charts/`          | Gráficas exportadas automáticamente para el informe.                                                            |
| `tables/`          | Tablas exportadas automáticamente en formato LaTeX.                                                             |
| `text/`            | Textos exportados automáticamente para el informe técnico.                                                      |
| `utils/`           | Funciones reutilizables para exportación de recursos y generación automática del reporte.                       |
| `report/`          | Reportes generados por el proyecto, incluyendo el EDA en HTML y el informe técnico en LaTeX/PDF.                |
| `README.md`        | Documentación general del proyecto.                                                                             |
| `requirements.txt` | Dependencias necesarias para ejecutar el proyecto.                                                              |

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

📄 **¿Quieres ver el resultado final?** El informe técnico ya está compilado e incluido en este repositorio. Puedes visualizarlo directamente aquí sin necesidad de ejecutar el código: 
👉 **[Ver el Informe Técnico en PDF](report/reporte_final.pdf)** *(Nota: asegúrate de cambiar la ruta por el nombre real de tu archivo PDF).*

---

# Principales resultados

El análisis permitió identificar los siguientes hallazgos:

* El saldo total administrado presentó fluctuaciones durante 2025, sin evidenciar una tendencia sostenida de crecimiento o disminución.
* La distribución de los saldos entre las sucursales fue relativamente equilibrada, sin observarse una concentración significativa en una única agencia.
* Los segmentos de clientes mostraron una distribución homogénea del saldo administrado.
* No se identificó una relación lineal claramente definida entre el ingreso de los clientes y el saldo disponible en sus cuentas.
* La mayor concentración de saldos se registró en clientes con edades comprendidas entre 20 y 69 años.

---

# Recomendaciones

Como resultado del análisis se proponen las siguientes acciones:

* Incorporar variables adicionales que permitan explicar con mayor precisión el comportamiento de los saldos.
* Realizar análisis específicos por sucursal y segmento de clientes para identificar oportunidades comerciales.
* Diseñar estrategias diferenciadas según el perfil de los clientes y los grupos de edad.
* Complementar el análisis exploratorio mediante técnicas estadísticas y modelos predictivos.

---

# Cómo ejecutar el proyecto

> 💡 **Tip rápido:** Si solo deseas ver el resultado final sin instalar dependencias ni ejecutar el código, puedes abrir directamente el **[Informe PDF ya generado](report/reporte_final.pdf)** que se encuentra en la carpeta `report/`.

Si deseas ejecutar el pipeline completo y generar el reporte por tu cuenta, sigue estos pasos:

1. Clonar este repositorio.

2. Instalar las dependencias:

> **Nota:** Para generar automáticamente el informe técnico es necesario tener instalada una distribución de LaTeX compatible con XeLaTeX (por ejemplo, MiKTeX o TeX Live).

```bash
pip install -r requirements.txt
```

3. Abrir el archivo `caso1.ipynb` utilizando Jupyter Notebook o JupyterLab.

4. Ejecutar todas las celdas del notebook.

Al finalizar la ejecución se generarán automáticamente:

* El conjunto de tablas en formato LaTeX.
* Las figuras utilizadas en el análisis.
* Los textos del informe.
* El informe técnico final en formato PDF.

---

# Autor

**Javier Barillas**

Estudiante de Economía | Analista de Datos

Proyecto desarrollado con fines educativos y como parte de un portafolio profesional de análisis de datos.
