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

#------------------------------------------------------------------
#----- Configuración de los Elementos del Panel Central -----------
#------------------------------------------------------------------

#----- VIAJES POR ESTACIONES -----------------------------------------
st.subheader('Agrupación de viajes por estaciones')
st.markdown("Se tomó únicamente el primer tercio para que se alcanzara a ver claramente a qué estación pertenece cada barra.")
st.image(io.imread(r"./Imagenes_Proyecto/Agrupacion_por_estaciones.png"))
st.divider()

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

st.divider()

#----- VARIACIÓN TIEMPO Y DISTANCIA DE VIAJE -----------------------------------------
#Definición de las columnas
colum_izq, colum_der = st.columns(2)

#Título para el gráfico
colum_izq.subheader('Promedio de tiempo de viaje')
colum_izq.image(io.imread(r"./Imagenes_Proyecto/Promedios_tiempo_viajes.png"))
colum_izq.markdown("El tiempo promedio de un viaje es: 15.244 minutos.")

#Título para el gráfico
colum_der.subheader('Aproximación de distancia recorrida')
colum_der.image(io.imread(r"./Imagenes_Proyecto/Aproximacion_distancia_recorrida.png"))
colum_der.markdown("La distancia promedio recorrida es: 3.56 km.")

st.divider()

#----- GRÁFICO DE COMPARACIÓN TIEMPO Y RUTA / GÉNERO -----------------------------------------
st.subheader('Comparación del tiempo y la ruta con el género de la persona')
st.markdown("Se utilizó únicamente 1 parte de 1536 para que se viera claramente la gráfica con los datos divididos.")
st.image(io.imread(r"./Imagenes_Proyecto/Comparacion_tiempo_ruta_genero.png"))

st.divider()

#----- GRÁFICO DE USO POR DÍAS DE SEMANA -----------------------------------------
st.subheader('Uso de bicicleta según el día de la semana')
# Generación del gráfico
if sem_selected == '2016':
    st.image(io.imread(r"./Imagenes_Proyecto/Grafica_uso_dias_semana_2016.png"))
elif sem_selected == '2017':
    st.image(io.imread(r"./Imagenes_Proyecto/Grafica_uso_dias_semana_2017.png"))
elif sem_selected == '2018':
    st.image(io.imread(r"./Imagenes_Proyecto/Grafica_uso_dias_semana_2018.png"))
elif sem_selected == '2019':
    st.image(io.imread(r"./Imagenes_Proyecto/Grafica_uso_dias_semana_2019.png"))
elif sem_selected == '2020':
    st.image(io.imread(r"./Imagenes_Proyecto/Grafica_uso_dias_semana_2020.png"))
elif sem_selected == '2021':
    st.image(io.imread(r"./Imagenes_Proyecto/Grafica_uso_dias_semana_2021.png"))
elif sem_selected == '2022':
    st.image(io.imread(r"./Imagenes_Proyecto/Grafica_uso_dias_semana_2022.png"))
elif sem_selected == '2023':
    st.image(io.imread(r"./Imagenes_Proyecto/Grafica_uso_dias_semana_2023.png"))
elif sem_selected == '2024':
    st.image(io.imread(r"./Imagenes_Proyecto/Grafica_uso_dias_semana_2024.png"))
else:
    st.image(io.imread(r"./Imagenes_Proyecto/Grafica_uso_dias_semana_2015.png"))

st.divider()

#----- TOTAL DE DINERO GASTADO ------------------------
#Título para el gráfico
st.subheader('Total de dinero gastado')
st.image(io.imread(r"./Imagenes_Proyecto/Total_dinero_gastado.png"))
st.markdown("En total, se gastó aproximadamente $1,645'683,973.00 en la suma de todos los viajes en este rango de fechas.")

st.divider()
#----- GRÁFICAS POS USO DE ESTACIONES ------------------------
#Título para el gráfico
st.subheader('Uso de estaciones')
# Generación del gráfico
if estacion_selected == '2016':
    st.image(io.imread(r"./Imagenes_Proyecto/Grafico_uso_estaciones_2016.png"))
elif estacion_selected == '2017':
    st.image(io.imread(r"./Imagenes_Proyecto/Grafico_uso_estaciones_2017.png"))
elif estacion_selected == '2018':
    st.image(io.imread(r"./Imagenes_Proyecto/Grafico_uso_estaciones_2018.png"))
elif estacion_selected == '2019':
    st.image(io.imread(r"./Imagenes_Proyecto/Grafico_uso_estaciones_2019.png"))
elif estacion_selected == '2020':
    st.image(io.imread(r"./Imagenes_Proyecto/Grafico_uso_estaciones_2020.png"))
elif estacion_selected == '2021':
    st.image(io.imread(r"./Imagenes_Proyecto/Grafico_uso_estaciones_2021.png"))
elif estacion_selected == '2022':
    st.image(io.imread(r"./Imagenes_Proyecto/Grafico_uso_estaciones_2022.png"))
elif estacion_selected == '2023':
    st.image(io.imread(r"./Imagenes_Proyecto/Grafico_uso_estaciones_2023.png"))
elif estacion_selected == '2024':
    st.image(io.imread(r"./Imagenes_Proyecto/Grafico_uso_estaciones_2024.png"))
else:
    st.image(io.imread(r"./Imagenes_Proyecto/Grafico_uso_estaciones_2015.png"))

st.divider()

#----- MATRIZ DE CORRELACIÓN ------------------------
#Título para el gráfico
st.subheader('Correlación entre la edad, el día de la semana y el tiempo de viaje')
st.image(io.imread(r"./Imagenes_Proyecto/Correlacion_edad_dia_semana_tiempo_viaje.png"))

st.divider()

#----- BOXPLOT DE EDADES ------------------------
#Título para el gráfico
st.subheader('Año de nacimiento más común entre quienes usan MiBici')
st.image(io.imread(r"./Imagenes_Proyecto/Edades_Boxplot_Extra.png"))