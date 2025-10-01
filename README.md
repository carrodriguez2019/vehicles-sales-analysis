# vehicles-sales-analysis
Una aplicación web interactiva para el análisis exploratorio de datos de ventas de vehículos, construida con Streamlit y Plotly.

![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)
![Plotly](https://img.shields.io/badge/Plotly-3F4F75?style=for-the-badge&logo=plotly)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)

# Descripción  del proyecto
Este proyecto proporciona un dashboard interactivo para analizar datos de anuncios de venta de vehículos. Permite explorar tendencias de precios, distribuciones por tipo de vehículo, marcas y más, mediante visualizaciones interactivas.

# Características principales

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
   ```bash
   git clone https://github.com/carrodriguez2019/vehicles-sales-analysis.git
   cd vehicles-sales-analysis

#### 2. **Crear entorno virtual**
   ```bash
  python -m venv vehicles_env

#### Windows
vehicles_env\Scripts\activate

#### Mac/Linux
source vehicles_env/bin/activate

#### 3. **Instalar dependencias**
   ```bash
  pip install -r requirements.txt

#### 4. **Descargar Dataset**
   ```bash
 ##### Opción automática (PowerShell)
  Invoke-WebRequest -Uri " https://practicum-content.s3.us-west-1.amazonaws.com/new-markets/Data_sprint_4_Refactored/vehicles_us.csv" -OutFile "vehicles_us.csv"
  
 ##### Opción manual: Descargar vehicles_us.csv y colocarlo en la raíz del proyecto

#### 5. **Ejecutar aplicación**
   ```bash
   streamlit run app.py

# Estrctura del proyecto

<img width="454" height="354" alt="Captura de pantalla 2025-09-30 185612" src="https://github.com/user-attachments/assets/aa535852-c63c-47b9-b6f1-b5d33a798c0d" />


 



