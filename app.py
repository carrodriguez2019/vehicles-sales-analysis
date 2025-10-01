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
    gif_base64 = load_gif_as_base64("assets/carro-nuevo.gif")
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
     
    # Filtro por marca con contadores
    brand_options = ['Todas'] + sorted(df['brand'].unique().tolist())
    
    # Mostrar marca con cantidad de vehículos
    selected_brand = st.sidebar.selectbox(
        "Selecciona Marca:", 
        brand_options,
        key='brand_filter_smart'
        )

    # Filtro por tipo de vehículo
    if selected_brand != 'Todas':        
         # Obtener datos específicos de la marca seleccionada
        brand_data = df[df['brand'] == selected_brand]
        available_types = sorted(brand_data['type'].dropna().unique().tolist())
        
        if available_types:
            type_options = ['Todos'] + available_types
            selected_type = st.sidebar.selectbox(
                f"Tipo de {selected_brand}:",
                type_options,
                key='type_filter_dynamic'                
            )
        else:
            st.sidebar.warning("No hay tipos especificos definidos")   
            selected_type = 'Todos'         
    else:
        all_types = ['Todos'] + sorted(df['type'].dropna().unique().tolist())
        selected_type = st.sidebar.selectbox(
            f"Selecciona Tipo:",
            all_types,
            key='type_filter_all'
        )
    
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

# Aplicar filtro de marca
if selected_brand != 'Todas':
    filtered_df = filtered_df[filtered_df['brand'] == selected_brand]

# Aplicar filtro de tipo (solo si hay tipos disponibles) 
if selected_type != 'Todos' and selected_type in filtered_df['type'].values:
    filtered_df = filtered_df[filtered_df['type'] == selected_type]

# Aplicar el filtro del pecio siempre
filtered_df = filtered_df[
            (filtered_df['price'] >= price_range[0]) & 
            (filtered_df['price'] <= price_range[1])
            ]
filtros_aplicados.append(f"Precio: ${price_range[0]:,} - ${price_range[1]:,}")

# Mostrar resumen de los filtros aplicados
if selected_brand != 'Todas':
    st.sidebar.write(f"• **Marca**: {selected_brand}")
if selected_type != 'Todos':
    st.sidebar.write(f"• **Tipo**: {selected_type}")
st.sidebar.write(f"• **Precio**: ${price_range[0]:,} - ${price_range[1]:,}")

# Botón para limpiar filtros
if st.sidebar.button("Limpiar todos los filtros"):
    st.markdown('<meta http-equiv="refresh" content="0">', unsafe_allow_html=True)               
    
# =======================================================================================================
# KPI's principales
# =======================================================================================================
st.header("📊 Métricas Principales")

col1, col2, col3, col4 = st.columns(4)

if len(filtered_df)== 0:
    st.warning("🚫 No vehículos que coincidan con los filtros seleccionados.")
    st.info ("💡 Prueba a ajustar los filtros para ver más resultados")     
else:
    with col1:
        
        st.metric(
            label="Vehículos Totales",
            value=f"{len(filtered_df):,}",
            delta=f"{len(filtered_df) - len(df)}" if len(filtered_df) != len(df) else None
        )
    
    with col2:
        avg_price = filtered_df['price'].mean()
        st.metric(
            label="Precio promedio",
            value=f"${avg_price:,.0f}",
            delta=f"${avg_price - df['price'].mean():0f}" if len(filtered_df) != len(df) else None            
        )

    with col3:
        avg_odometer = filtered_df['odometer'].mean()
        st.metric(
            label="Odómetro Promedio",
            value=f"${avg_odometer:,.0f} km",
            delta=f"${avg_odometer - df['odometer'].mean():0f}" if len(filtered_df) != len(df) else None            
        )

    with col4:
        avg_year = filtered_df['model_year'].mean()
        # Mostrar como entero y manejar mejor el delta
        delta_year = avg_year - df['model_year'].mean()
        # Formatear el delta para que sea más legible
        delta_formatted = f"{delta_year:+.1f}" if abs(delta_year) >= 0.1 else None

        st.metric(
            label="Año Promedio",
            value=f"**{int(avg_year)}**",
            delta=delta_formatted
        )
    
    st.markdown("---")

#=============================================================================================================
# Visualizaciones interactivas
#=============================================================================================================
st.header ("📈 Visualizaciones Interactivas")

# Selección de gráficos con checkboxes
col1, col2 = st.columns(2)

with col1:
    show_histogram = st.checkbox("📊 Histograma/D. de Barras de Precios", value=True)
    show_scatter = st.checkbox("📈 Dispersión Precio vs Año")

with col2:
    show_boxplot = st.checkbox("📦 Boxplot por Tipo")
    show_pie = st.checkbox("🥧 Distribución por Combustible")

# Crear visualizaciones por seleccion
# HISTOGRAMA / D. de Barras
if show_histogram and len(filtered_df) > 0:
    st.subheader("Distribución de Precios")
    
    # Verificar si todos los precios son iguales
    precios_unicos = filtered_df['price'].nunique()
    precio_min = filtered_df['price'].min()
    precio_max = filtered_df['price'].max()
    
    if precios_unicos == 1:
        # Todos los precios son iguales
        st.info(f" **Todos los vehículos tienen el mismo precio: ${precio_min:,.0f}**")
        
        # Mostrar un gráfico de barras simple en lugar de histograma
        fig_bar = px.bar(
            x=[f"${precio_min:,.0f}"],
            y=[len(filtered_df)],
            title=f"Todos los vehículos - Precio: ${precio_min:,.0f}",
            labels={'x': 'Precio', 'y': 'Cantidad de vehículos'},
            color_discrete_sequence=['#1f77b4']
        )
        fig_bar.update_layout(showlegend=False)
        st.plotly_chart(fig_bar, use_container_width=True)
        
        # Mostrar información adicional
        st.write(f"**Total de vehículos:** {len(filtered_df)}")
        if 'model' in filtered_df.columns:
            st.write(f"**Modelos disponibles:** {', '.join(filtered_df['model'].unique()[:5])}")
            if len(filtered_df['model'].unique()) > 5:
                st.write(f"... y {len(filtered_df['model'].unique()) - 5} modelos más")
    
    elif precios_unicos < 10:
        # Pocos precios diferentes (menos de 10)
        st.info(f" **Solo {precios_unicos} precios diferentes en {len(filtered_df)} vehículos**")
        
        # Crear gráfico de barras con conteo por precio
        conteo_precios = filtered_df['price'].value_counts().sort_index()
        
        fig_bar = px.bar(
            x=[f"${precio:,.0f}" for precio in conteo_precios.index],
            y=conteo_precios.values,
            title=f"Distribución de Precios ({precios_unicos} precios diferentes)",
            labels={'x': 'Precio', 'y': 'Cantidad de vehículos'},
            color_discrete_sequence=['#1f77b4']
        )
        fig_bar.update_layout(
            xaxis_tickangle=-45,
            showlegend=False
        )
        st.plotly_chart(fig_bar, use_container_width=True)
        
        # Mostrar tabla con detalles
        st.write("**Detalle por precio:**")
        for precio, cantidad in conteo_precios.items():
            st.write(f"- ${precio:,.0f}: {cantidad} vehículos")
    
    else:
        # Suficiente variación para histograma normal
        fig_hist = px.histogram(
            filtered_df,
            x='price',       
            nbins=min(30, precios_unicos),  # No más bins que precios únicos
            title=f"Distribución de Precios ({len(filtered_df)} vehículos - {precios_unicos} precios diferentes)",
            labels={'price': 'Precio ($)', 'count': 'Cantidad de vehículos'},        
            color_discrete_sequence=['#1f77b4']        
        )
        
        # Ajustar rango para mejor visualización
        rango_precio = precio_max - precio_min
        fig_hist.update_layout(
            xaxis_range=[precio_min - (rango_precio * 0.05), precio_max + (rango_precio * 0.05)],
            showlegend=False
        )
        
        st.plotly_chart(fig_hist, use_container_width=True)

# SCATTER PLOT 
if show_scatter and len(filtered_df) > 0:
    st.subheader("Relación: Precio vs Año del Modelo")
    try:
        fig_scatter = px.scatter(filtered_df, x='model_year', y='price', 
                                color='type',size='odometer', title='Precio vs Año',labels={
                'model_year': 'Año del Modelo', 
                'price': 'Precio($)',
                'type': 'Tipo de Vehículo'
            },opacity=0.7)
        st.plotly_chart(fig_scatter, use_container_width=True)
    except Exception as e:        
        st.error(f"No se pudo crear el gráfico de dispersión: {e}")
           
# BOXPLOT   
if show_boxplot and len(filtered_df) > 0:
    if show_boxplot and len(filtered_df) > 0:
        st.subheader("Distribución de Precios por Tipo")
        try:
            fig_box = px.box(filtered_df, x='type', y='price', 
                            title='Precios por Tipo de Vehículo')
            st.plotly_chart(fig_box, use_container_width=True)
        except Exception as e:
            st.error(f"No se pudo crear el boxplot: {e}")             
        
# PIE CHART
if show_pie and len(filtered_df) > 0:
    st.subheader("Distribución por Combustible")
    try:
        fuel_data = filtered_df['fuel'].value_counts()
        fig_pie = px.pie(values=fuel_data.values, names=fuel_data.index,
                        title='Distribución por Combustible')
        st.plotly_chart(fig_pie, use_container_width=True)
    except Exception as e:
        st.error(f"No se pudo crear el gráfico de pie: {e}")
        
#==============================================================================================================
# Datos en tabla
#==============================================================================================================
st.markdown("---")
st.header("📋 Vista de Datos")
if st.checkbox("Mostrar tabla de datos"):
    
    # Selector de cantidad de registros
    num_records = st.selectbox(
        "Número de vehículos a mostrar:",
        options=[50, 100, 200, 500, "Todos"],
        index=1
    )
    
    if num_records == "Todos":
        display_data = filtered_df
    else:
        display_data = filtered_df.head(num_records)
    
    # Mostrar tabla
    st.dataframe(
        display_data[
            ['model', 'model_year', 'price', 'odometer', 'type', 'condition', 'fuel']
        ],
        use_container_width=True
    )
    
    st.write(f"**Mostrando {len(display_data)} de {len(filtered_df)} vehículos**")
    
    # Botón de descarga
    csv = filtered_df.to_csv(index=False)
    st.download_button(
        label="📥 Descargar Datos Filtrados (CSV)",
        data=csv,
        file_name=f"vehiculos_filtrados_{datetime.now().strftime('%Y%m%d')}.csv",
        mime="text/csv"
    )

    
