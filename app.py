# Importar librerias
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime
import numpy as np
import base64
import urllib.parse


#=================================================================================================
# Configuracion de la pagina
#=================================================================================================
st.set_page_config(
    page_title = 'Analisis de Vehiculos',
    page_icon = "🚗",
    layout = "wide",
    initial_sidebar_state = "expanded" 
)

#==================================================================================================
# Funciones auxiliares
@st.cache_data
def load_data():
    """Cargar y preparar datos"""
    try:
        df = pd.read_csv("vehicles_us.csv")
        
        # Limpieza básica
        df_clean = df.copy()
        
        # Eliminar columnas con null
        if 'is_4wd' in df_clean.columns:
            df_clean = df_clean.drop(columns=['is_4wd'])
        
        # Imputar valores nulos
        if 'paint_color' in df_clean.columns:
            df['paint_color'] = df_clean['paint_color'].fillna('Desconocido')
        
        # Columnas numéricas
        numeric_columns = ['model_year','cylinders','odometer']
        for col in numeric_columns:
            if df_clean[col].isnull().sum() > 0:
                df_clean[col] = df_clean[col].fillna(df_clean[col].median())
        
        df_clean['model_year'] = df_clean['model_year'].astype(int)
        
        df_clean['brand'] = df_clean['model'].str.split().str[0]
        df_clean['age'] = datetime.now().year - df_clean['model_year']
        
        return df_clean
    except Exception as e:
        st.error(f"Error cargando los datos: {e}")
        return None

#=========================================================================
# Interfaz Principal
#=========================================================================

def load_gif_as_base64(gif_path):
    with open(gif_path,"rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

try:
    gif_base64 = load_gif_as_base64("iconos/carro-nuevo.gif")
    # Usar columnas para alinear el GIF con el título
    col1, col2 = st.columns([0.1, 0.9])
    # Mostrar el GIF
    with col1:
        st.markdown(f'<img src="data:image/gif;base64,{gif_base64}" width="80">',unsafe_allow_html=True)
    with col2:
        st.title("Análisis del Mercado de Vehículos")
        st.markdown("----------")
except FileNotFoundError:
    st.error('No se encontro el archivo gif')
    st.title("🚗 Análisis del Mercado de Vehículos")

# Cargar datos
with st.spinner('Cargando datos...'):
    df = load_data()

if df is not None:
    # Controles
    st.sidebar.title("🎛️ Panel de Control")
    st.sidebar.markdown("---")
    
    # Filtros
    st.sidebar.subheader("🔍 Filtros")    
     
    # Filtro por narca
    with st.sidebar.container():        
        brands = ["Todos"] + sorted(df['brand'].unique().tolist())
        select_brand = st.sidebar.selectbox("Selecciona una marca: ",brands)
    
    # Filtro por tipo de vehículo
    types = ['Todos'] + sorted(df['type'].dropna().unique().tolist())
    select_type = st.sidebar.selectbox("Selecciona un tipo: ",types)
    
    # Filtro por rango de precio
    min_price, max_price = int(df['price'].min()), int(df['price'].max())
    price_range = st.sidebar.slider(
        "Rango de precio ($):",
        min_price,max_price,(min_price,min(max_price,50000))
    )

#==============================================================================================================
# Aplicar filtros
#==============================================================================================================
filtered_df = df.copy()

# Aplicar filtros solo si no son "Todos/Todas"
filtros_aplicados = []

if select_brand != 'Todos':
    filtered_df = filtered_df[filtered_df['brand'] == select_brand]
    filtros_aplicados.append(f"Marca: {select_brand}")
    
if select_type != 'Todos':
    filtered_df = filtered_df[filtered_df['type'] == select_type]
    filtros_aplicados.append(f"Tipo: {select_type}")

filtered_df = filtered_df[
            (filtered_df['price'] >= price_range[0]) & 
            (filtered_df['price'] <= price_range[1])
            ]
filtros_aplicados.append(f"Precio: ${price_range[0]:,} - ${price_range[1]:,}")

if filtros_aplicados:
    st.sidebar.subheader("Filtros Activos")
    for filtro in filtros_aplicados:
        st.sidebar.write(f"{filtro}")

# Botón para limpiar filtros
if st.sidebar.button("Limpiar todos los filtros"):
    st.markdown('<meta http-equiv="refresh" content="0">', unsafe_allow_html=True)               
    
# =======================================================================================================
# KPIS principales
# =======================================================================================================
