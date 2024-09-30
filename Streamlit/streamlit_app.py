# =================================================================
# == INSTITUTO TECNOLOGICO Y DE ESTUDIOS SUPERIORES DE OCCIDENTE ==
# ==         ITESO, UNIVERSIDAD JESUITA DE GUADALAJARA           ==
# ==            PROGRAMACIÓN PARA ANÁLISIS DE DATOS             ==
# ==                 IMPLEMENTACIÓN EN STREAMLIT                 ==
# =================================================================

#----- Importación de Librerías -----------------------------------
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import os
import numpy as np

#------------------------------------------------------------------
#----- Configuración Inicial del Panel Central --------------------
#------------------------------------------------------------------

#----- Renderizado del Texto --------------------------------------
st.title("Análisis de Datos del Programa MiBici")
"""
#------------------------------------------------------------------
#----- Configuración de los Elementos del DashBoard ---------------
#------------------------------------------------------------------
st.sidebar.markdown("## Menú de Configuración")
st.sidebar.divider()

#----- LECTURA DE LOS DATOS ---------------------------------------
# Directorio donde están los archivos CSV
directorio = './Datos_MiBici'

# Crear una lista con todos los archivos CSV desde 2014_12 hasta 2024_08
archivos = [f'datos_abiertos_{year}_{str(month).zfill(2)}.csv' 
            for year in range(2014, 2025) 
            for month in range(1, 13) 
            if not (year == 2014 and month < 12) and not (year == 2024 and month > 8)]

# Leer y concatenar todos los archivos
dataframes = []
for archivo in archivos:
    path = os.path.join(directorio, archivo)
    if os.path.exists(path):
        df = pd.read_csv(path)
        year = int(archivo.split('_')[2])
        df['Anio_viaje'] = year
        dataframes.append(df)
    else:
        st.warning(f"Archivo no encontrado: {archivo}")

# Concatenar todos los DataFrames en uno solo
if dataframes:
    datos_mibici = pd.concat(dataframes, ignore_index=True)
else:
    st.error("No se encontraron archivos CSV.")

# Mostrar la información básica del DataFrame
st.write("Vista de los primeros registros del DataFrame:")
st.dataframe(datos_mibici.head())

st.write("Información del DataFrame:")
st.write(datos_mibici.info())

#------------------------------------------------------------------
#----- CONFIGURACIÓN DE GRÁFICOS EN EL PANEL CENTRAL --------------
#------------------------------------------------------------------
st.sidebar.markdown("## Configuración de Gráficos")
anio_seleccionado = st.sidebar.selectbox('Selecciona el Año para Mostrar Datos:', datos_mibici['Anio_viaje'].unique())
st.sidebar.divider()

# Filtrar por el año seleccionado
datos_filtrados = datos_mibici[datos_mibici['Anio_viaje'] == anio_seleccionado]

#----- HISTOGRAMA DE AÑOS DE NACIMIENTO ---------------------------
st.markdown(f"### Histograma del Año de Nacimiento para el Año {anio_seleccionado}")
plt.figure(figsize=(10, 6))
sns.histplot(datos_filtrados['Anio_de_nacimiento'], bins=20, kde=True, color='skyblue')
plt.title(f'Histograma de Año de Nacimiento ({anio_seleccionado})')
plt.xlabel('Año de Nacimiento')
plt.ylabel('Frecuencia')
st.pyplot(plt)

#----- GRÁFICO DE DISPERSIÓN --------------------------------------
st.markdown(f"### Gráfico de Dispersión: Año de Nacimiento vs Origen_Id ({anio_seleccionado})")
plt.figure(figsize=(10, 6))
plt.scatter(datos_filtrados['Anio_de_nacimiento'], datos_filtrados['Origen_Id'], color='purple', alpha=0.5)
plt.title(f'Dispersión de Año de Nacimiento vs Origen ({anio_seleccionado})')
plt.xlabel('Año de Nacimiento')
plt.ylabel('Origen_Id')
st.pyplot(plt)

#----- GRÁFICO DE PIE: VIAJES POR AÑO -----------------------------
st.markdown(f"### Distribución de Viajes por Año")
viajes_por_anio = datos_mibici.groupby('Anio_viaje').size().reset_index(name='Cantidad_viajes')
plt.figure(figsize=(8, 8))
viajes_por_anio.set_index('Anio_viaje').plot(kind='pie', y='Cantidad_viajes', autopct='%1.1f%%', legend=False)
plt.title("Viajes por Año")
plt.ylabel('')
st.pyplot(plt)

#------------------------------------------------------------------
#----- OPCIONES ADICIONALES EN LA BARRA LATERAL -------------------
#------------------------------------------------------------------
# Matriz de correlación
st.sidebar.markdown("### Visualización de Matriz de Correlación")
columnas_numericas = datos_mibici.select_dtypes(include=[np.number]).columns.tolist()
columnas_seleccionadas = st.sidebar.multiselect('Selecciona las Columnas para la Matriz de Correlación:', columnas_numericas, default=columnas_numericas)

if columnas_seleccionadas:
    plt.figure(figsize=(10, 6))
    sns.heatmap(datos_mibici[columnas_seleccionadas].corr(), annot=True, cmap='coolwarm')
    plt.title('Matriz de Correlación')
    st.pyplot(plt)
else:
    st.warning("Selecciona al menos una columna para mostrar la matriz de correlación.")

#------------------------------------------------------------------
#----- DESPEDIDA --------------------------------------------------
#------------------------------------------------------------------
st.markdown("### ¡Gracias por usar la aplicación de análisis de MiBici!")

"""