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
sem_selected = st.sidebar.selectbox('Elección del Año para el Uso de Bicicleta por Año: ', vars_year, index = default_hist)
st.sidebar.divider()

#----- GRÁFICO DE USO DE ESTACIONES -----------------------
#----- Selector del Año -----------------------------------
estacion_selected = st.sidebar.selectbox('Elección del Año para el Uso de las Estaciones de MiBici: ', vars_year, index = default_hist)
st.sidebar.divider()

#------------------------------------------------------------------
#----- Configuración de los Elementos del Panel Central -----------
#------------------------------------------------------------------

#----- VIAJES POR ESTACIONES -----------------------------------------
st.subheader('Agrupación de viajes por estaciones')
st.markdown("Se tomó únicamente el primer tercio para que se alcanzara a ver claramente a qué estación pertenece cada barra.")
st.image(io.imread(r"./Imagenes_Proyecto/Agrupacion_por_estaciones.png"))

#----- NÚMERO DE VIAJES POR AÑO -----------------------------------------
st.subheader('Gráfica con número de viajes por mes de cada año')
# Generación del gráfico
if histo_selected == '2016':
    st.image(io.imread(r"./Imagenes_Proyecto/Graficas_numeros_viajes_2016.png"))
elif histo_selected == '2017':
    st.image(io.imread(r"./Imagenes_Proyecto/Graficas_numeros_viajes_2017.png"))
elif histo_selected == '2018':
    st.image(io.imread(r"./Imagenes_Proyecto/Graficas_numeros_viajes_2018.png"))
elif histo_selected == '2019':
    st.image(io.imread(r"./Imagenes_Proyecto/Graficas_numeros_viajes_2019.png"))
elif histo_selected == '2020':
    st.image(io.imread(r"./Imagenes_Proyecto/Graficas_numeros_viajes_2020.png"))
elif histo_selected == '2021':
    st.image(io.imread(r"./Imagenes_Proyecto/Graficas_numeros_viajes_2021.png"))
elif histo_selected == '2022':
    st.image(io.imread(r"./Imagenes_Proyecto/Graficas_numeros_viajes_2022.png"))
elif histo_selected == '2023':
    st.image(io.imread(r"./Imagenes_Proyecto/Graficas_numeros_viajes_2023.png"))
elif histo_selected == '2024':
    st.image(io.imread(r"./Imagenes_Proyecto/Graficas_numeros_viajes_2024.png"))
else:
    st.image(io.imread(r"./Imagenes_Proyecto/Graficas_numeros_viajes_2015.png"))

#----- VARIACIÓN TIEMPO Y DISTANCIA DE VIAJE -----------------------------------------
#Definición de las columnas
colum_izq, colum_der = st.columns(2)

#Título para el gráfico
colum_izq.subheader('Promedio de tiempo de viaje')

colum_izq.image(io.imread(r"./Imagenes_Proyecto/Promedios_tiempo_viajes.png"))
"""
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