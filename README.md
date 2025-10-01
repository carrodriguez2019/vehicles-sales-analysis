# vehicles-sales-analysis
Una aplicación web interactiva para el análisis exploratorio de datos de ventas de vehículos, construida con Streamlit y Plotly.

![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)
![Plotly](https://img.shields.io/badge/Plotly-3F4F75?style=for-the-badge&logo=plotly)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)

## Descripción  del proyecto
Este proyecto proporciona un dashboard interactivo para analizar datos de anuncios de venta de vehículos. Permite explorar tendencias de precios, distribuciones por tipo de vehículo, marcas y más, mediante visualizaciones interactivas.

## Características principales

### Panel de Control Interactivo
- **Filtros Dinámicos**: Marca, tipo de vehículo, rango de precios
- **Filtros Inteligentes**: Los tipos de vehículo se actualizan según la marca seleccionada
- **Métricas en Tiempo Real**: KPIs actualizados según los filtros aplicados

### 📈 Visualizaciones Interactivas
- **Histograma de Precios**: Distribución de precios de vehículos. Si tiene menos de 10 precios relacionados, muestra un diagrama de barras. 
- **Gráfico de Dispersión**: Relación entre precio y año del modelo
- **Boxplot por Tipo**: Distribución de precios por categoría de vehículo
- **Gráfico de Pie**: Distribución por tipo de combustible

### Funcionalidades de Datos
- **Tabla Interactiva**: Vista paginada de los datos filtrados
- **Exportación de Datos**: Botón para descargar los resultados en la tabla en formato CSV por la cantidad de registros seleccionados. En la parte superior izquierda hay manera de descargar el archivo csv con el total de registros con los datos filtrados.
- **Búsqueda en Tiempo Real**: La tabla en la parte superior izquierda permite buscar en los registros cualquier dato.

## Tecnologías Utilizadas
- **Frontend**: Streamlit
- **Visualización**: Plotly Express
- **Procesamiento de Datos**: Pandas, NumPy
- **Análisis**: Jupyter Notebooks
- **Control de Versiones**: Git & GitHub

## Instalación y Uso

### Prerrequisitos
- Python 3.12.10
- Git

### Pasos de Instalación

#### 1. **Clonar el repositorio**   
   git clone https://github.com/carrodriguez2019/vehicles-sales-analysis.git
   cd vehicles-sales-analysis   

#### 2. **Crear entorno virtual**   
   python -m venv vehicles_env   
   #### Windows: vehicles_env\Scripts\activate   
   #### Mac/Linux: source vehicles_env/bin/activate

#### 3. **Instalar dependencias**
  pip install -r requirements.txt

#### 4. **Descargar Dataset**   
 ##### Opción automática (PowerShell)
  Invoke-WebRequest -Uri " https://practicum-content.s3.us-west-1.amazonaws.com/new-markets/Data_sprint_4_Refactored/vehicles_us.csv" -OutFile "vehicles_us.csv"
  
 ##### Opción manual: Descargar vehicles_us.csv y colocarlo en la raíz del proyecto

#### 5. **Ejecutar aplicación**   
   streamlit run app.py

## Estrctura del proyecto
<img width="476" height="309" alt="Captura de pantalla 2025-09-30 190857" src="https://github.com/user-attachments/assets/5567d00f-1fc7-4326-bf53-d41b8b93eab0" />

## Uso de la Aplicación

### Filtros Disponibles
- Marca: Selecciona una marca específica o "Todas"
- Tipo de Vehículo: Filtra por categoría (SUV, sedan, truck, etc.)
- Rango de Precio: Control deslizante para definir precio mínimo y máximo

### Visualizaciones
- Histograma: Distribución de precios en el mercado
- Gráfico de Barras: Cuando la distribución de precios en el mercado no tiene mucha variacion (<10)
- Dispersión: Relación entre año del modelo y precio
- Boxplot: Comparación de precios entre tipos de vehículo
- Gráfico Circular: Proporción de tipos de combustible

### Exportación de Datos
- Descarga los datos filtrados en formato CSV
- Incluye todas las columnas relevantes del dataset

## Dataset
- El proyecto utiliza el dataset vehicles_us.csv que contiene:
- 51,525 anuncios de vehículos
- 13 características incluyendo precio, año, modelo, condición, etc.
- Datos de diferentes marcas y tipos de vehículos

## Columnas Principales
- price: Precio del vehículo ($)
- model_year: Año del modelo
- model: Modelo del vehículo
- type: Tipo de vehículo (SUV, sedan, truck, etc.)
- condition: Condición del vehículo
- odometer: Kilometraje
- fuel: Tipo de combustible

## Análisis Exploratorio
El notebook notebooks/EDA.ipynb contiene:
- Análisis de valores nulos y tratamiento de datos
- Visualizaciones exploratorias
- Estadísticas descriptivas
- Identificación de patrones y tendencias

## 🤝 Contribuciones
¡Las contribuciones son bienvenidas y apreciadas! Si quieres mejorar este proyecto:

### Cómo contribuir:
1. **Haz un Fork** del proyecto
2. **Crea una Rama** para tu feature (`git checkout -b feature/AmazingFeature`)
3. **Commit** tus cambios (`git commit -m 'feat: Add some AmazingFeature'`)
4. **Push** a la rama (`git push origin feature/AmazingFeature`)
5. **Abre un Pull Request**

### Guía de contribución:
- **Reportar bugs**: Abre un issue describiendo el problema
- **Sugerir features**: Comparte tus ideas para mejorar el proyecto
- **Mejorar documentación**: Ayuda a hacer el README más claro
- **Agregar tests**: Contribuye con pruebas para el código

### Convenciones de código:
- Sigue el estilo de código existente
- Usa mensajes de commit descriptivos
- Asegúrate de que el código pase las validaciones
- Actualiza la documentación si es necesario

## Licencia
Este proyecto está bajo la **Licencia MIT** - ver el archivo [LICENSE](LICENSE) para más detalles.

### Contexto Educativo
Este es un proyecto desarrollado con fines educativos. El código es de uso libre para aprendizaje, práctica y desarrollo de habilidades en análisis de datos y desarrollo web.

**¿Qué puedes hacer?**
- Usar el código para aprender
- Modificar y experimentar
- Incluir en tus propios proyectos educativos
- Compartir con otros estudiantes

**Atribución apreciada**
Si usas este código como referencia, ¡menciona el proyecto original!

## Autor
Carolina Rodríguez Guerra
GitHub: https://github.com/carrodriguez2019
LinkedIn: 

## 🙏 Agradecimientos
Dataset proporcionado por Tripleten
Iconos y badges de flaticon.es

 ## ⭐ Si este proyecto te resultó útil, por favor dale una estrella en GitHub!




