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
import random
from skimage import io

#------------------------------------------------------------------
#----- Configuración Inicial del Panel Central --------------------
#------------------------------------------------------------------

#----- Renderizado del Texto --------------------------------------
st.title("Análisis de Datos del Programa MiBici")
st.subheader(":blue[Para este proyecto se hizo un análisis de los datos del programa MiBici tomando en cuenta los meses de Enero a Junio desde el año 2015 a 2024.]")

#------------------------------------------------------------------
#----- Configuración de los Elementos del DashBoard ---------------
#------------------------------------------------------------------

#----- Renderizado de la Imagen y el Título en el Dashboard -------
st.sidebar.markdown("## MENÚ DE CONFIGURACIÓN")
st.sidebar.divider()

#----- NÚMERO DE VIAJES POR AÑO -----------------------------------------
#----- Selector del Año -------------------------------------------
vars_year = ['2015','2016','2017','2018','2019','2020','2021','2022','2023','2024']
default_hist = vars_year.index('2015')
histo_selected = st.sidebar.selectbox('Elección del Año para el Número de Viajes mensuales: ', vars_year, index = default_hist)
st.sidebar.divider()

#----- GRÁFICO DE USO POR DIAS DE SEMANA -----------------------
#----- Selector del Año -----------------------------------
ganan_selected = st.sidebar.selectbox('Elección del Año para el Uso de Bicicleta por Año: ', vars_year, index = default_hist)
st.sidebar.divider()

#----- GRÁFICO DE USO DE ESTACIONES -----------------------
#----- Selector del Año -----------------------------------
ganan_selected = st.sidebar.selectbox('Elección del Año para el Uso dE las Estaciones de MiBici: ', vars_year, index = default_hist)
st.sidebar.divider()

#------------------------------------------------------------------
#----- Configuración de los Elementos del Panel Central -----------
#------------------------------------------------------------------

#----- NÚMERO DE VIAJES POR AÑO -----------------------------------------
st.subheader('Agrupación viajes por estaciones')
#io.imread(r"./Imagenes_Proyecto/Agrupacion_por_estaciones.png")
st.image(io.imread(r"./Imagenes_Proyecto/Agrupacion_por_estaciones.png"))
"""
#----- HISTOGRAMA POR MES -----------------------------------------
#Definición de las columnas
colum_izq, colum_der = st.columns(2)

#Título para el gráfico
colum_izq.subheader('Histograma')

#Inicialización del gráfico
fig1, ax1 = plt.subplots()

#Generación del gráfico
sns.set(style = "darkgrid")
sns.histplot(data = datos_df[histo_selected])
ax1.set_title('Histograma de Valores')
ax1.set_xlabel(histo_selected)
ax1.set_ylabel('Frecuencia')

#----- GRÁFICO DE LÍNEAS PARA LAS GANANCIAS -----------------------
#Renderización del gráfico
colum_izq.pyplot(fig1)

#Título para el gráfico
colum_der.subheader('Ganancias')

#Inicialización del gráfico
fig2, ax2 = plt.subplots()

#Generación del gráfico
if ganan_selected == 'Iñaki González':
    periodo_df = datos_df.iloc[0]
elif ganan_selected == 'María Cázares':
    periodo_df = datos_df.iloc[1]
elif ganan_selected == 'José García':
    periodo_df = datos_df.iloc[2]
elif ganan_selected == 'Jérémie Muñoz':
    periodo_df = datos_df.iloc[3]
elif ganan_selected == 'Agnès Villalón':
    periodo_df = datos_df.iloc[4]
elif ganan_selected == 'Bérénice Pitkämäki':
    periodo_df = datos_df.iloc[5]
elif ganan_selected == 'Geneviève Rukajärvi':
    periodo_df = datos_df.iloc[6]
elif ganan_selected == 'Hélène Ñuñoz':
    periodo_df = datos_df.iloc[7]
elif ganan_selected == 'Ñaguí Grönholm':
    periodo_df = datos_df.iloc[8]
elif ganan_selected == 'Iván Földváry':
    periodo_df = datos_df.iloc[9]
else:
    periodo_df = datos_df
periodo_df = periodo_df.transpose()
periodo_df = periodo_df.to_frame()
periodo_df = periodo_df.rename(columns = {1: 'MES'})
periodo_df = periodo_df.drop(['NOMBRE','APELLIDO','CIUDAD'])
plt.plot(periodo_df)
ax2.set_title('Ganancias Mensuales por Persona')
ax2.set_xlabel(ganan_selected)
ax2.set_ylabel('Ganancias')

#Renderización del gráfico
colum_der.pyplot(fig2)
st.divider()

#----- GRÁFICO DE CORRELACIÓN DE LOS MESES ------------------------
#Título para el gráfico
st.subheader('Matriz de Correlación')

#Inicialización del gráfico
fig3, ax3 = plt.subplots()

#Generación del gráfico
df_corr = datos_df[mes_multi_selected].corr()
sns.heatmap(df_corr, annot = anotacion, fmt='.2f', cmap = color_selected)

#Renderización del gráfico
st.pyplot(fig3)
st.divider()

# GANANCIAS DE LA CIUDAD
st.title("Ganancias por Ciudad")

# Grafico sobre ganancias por ciudad
ciudades = ganancias_ciudad['Ciudad']
gan_ciu = ganancias_ciudad['Ganancia']

fig4, ax4 = plt.subplots()

ax4.bar(ciudades, gan_ciu, color='blue')
ax4.set_title("Ganancias por Ciudad")
ax4.set_xlabel("Ciudades")
ax4.set_xticklabels(ciudades, rotation=75)
ax4.set_ylabel("Ganancias")

st.pyplot(fig4)
"""