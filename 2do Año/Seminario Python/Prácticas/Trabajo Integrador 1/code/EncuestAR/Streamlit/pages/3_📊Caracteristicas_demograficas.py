import streamlit as st
import os  # Importa os para poder trabajar con carpetas y archivos
import sys
import pandas as pd
import matplotlib.pyplot as plt
import json
import folium
from streamlit_folium import st_folium
import io # se importa para el punto de educacion, para no modificar la funcion original de ranking de aglomedrados



# arega la carpeta src al sys.path (necesario porque estamos  en /pages/)
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
SRC_DIR = os.path.join(BASE_DIR, 'src')

if SRC_DIR not in sys.path:
    sys.path.append(SRC_DIR)

print("SRC DIR:", SRC_DIR)
print("SYS PATH:", sys.path)

from utils import obtener_trimestres
from lectura import guardar_csv_basico, cargar_archivos
from config import DATA_PATH, RESULTADOS_PATH, SRC_PATH
from utils import asegurar_existencia_carpeta_data, verificar_existencia_archivos_matcheados

from procesamiento_individuos import ranking_aglomerados_estudios
from procesamiento_individuos import pueden_leer


# define la ruta a la carpeta donde estan los archivos de datos
# Como el archivo streamlit.py esta en la carpeta "src", usamos ../ para subir un nivel
carpeta_datos = DATA_PATH
# Verifica la existencia de archivos, si se subieron o no
archivo_hogar = RESULTADOS_PATH / "hogar_unificado.csv"
archivo_ind = RESULTADOS_PATH / "individuos_unificado.csv"

st.header("📊 Características demográficas")
st.markdown("En esta sección se visualizará información relacionada a la características demográficas de la población argentina según la EPH. ")


etiquetas_aglo = {
    2: "Gran La Plata",
    3: "Bahía Blanca - Cerri",
    4: "Gran Rosario",
    5: "Gran Santa Fé",
    6: "Gran Paraná",
    7: "Posadas",
    8: "Gran Resistencia",
    9: "Comodoro Rivadavia - Rada Tilly",
    10: "Gran Mendoza",
    12: "Corrientes",
    13: "Gran Córdoba",
    14: "Concordia",
    15: "Formosa",
    17: "Neuquén – Plottier",
    18: "Santiago del Estero - La Banda",
    19: "Jujuy-Palpalá",
    20: "Río Gallegos",
    22: "Gran Catamarca",
    23: "Gran Salta",
    25: "La Rioja",
    26: "Gran San Luis",
    27: "Gran San Juan",
    29: "Gran Tucumán - Tafí Viejo",
    30: "Santa Rosa – Toay",
    31: "Ushuaia - Río Grande",
    32: "Ciudad Autónoma de Buenos Aires",
    33: "Partidos del GBA",
    34: "Mar del Plata",
    36: "Río Cuarto",
    38: "San Nicolás – Villa Constitución",
    91: "Rawson – Trelew",
    93: "Viedma – Carmen de Patagones"
}


archivo_ind = RESULTADOS_PATH / "individuos_completo.csv"  # este es el archivo a usar
try:
    #cargo archivo
    arch = pd.read_csv(archivo_ind,sep=";", encoding="utf-8")
except FileNotFoundError:
    st.error("No se encontró el archivo 'individuos_completo.csv'.")
    arch = None

except Exception as e:
    st.error(f"Ocurrió un error: {e}")
    arch = None

    #punto 1.3.1

if arch is not None:
    # valido las columnas que necesito
    if "ANO4" not in arch or "TRIMESTRE" not in arch or "CH04" not in arch or "CH06" not in arch:
        st.error("Faltan columnas requeridas en el archivo CSV.")
    else:
        st.header("Distribución de la población por grupos de edad (cada 10 años) y sexo")


    #armo la lista para que el usuario elija año y trimestre
    años_disponibles = sorted([int(a) for a in arch["ANO4"].dropna().unique()])
    año = st.selectbox("Seleccione el año", años_disponibles)
    trimestres_disponibles = sorted([int(t) for t in arch[arch["ANO4"] == año]["TRIMESTRE"].dropna().unique()])
    trimestre = st.selectbox("Seleccione el trimestre", trimestres_disponibles)


    # filtro por año y trimestre
    arch_filtrado = arch[(arch["ANO4"] == año) & (arch["TRIMESTRE"] == trimestre)]

    # filtro edades válidas
    arch_filtrado = arch_filtrado[arch_filtrado["CH06"] >= 0]

    # armo los grupos de edad
    arch_filtrado["Grupo Edad"] = ((arch_filtrado["CH06"] // 10) * 10).astype(int)
    arch_filtrado = arch_filtrado[arch_filtrado["Grupo Edad"] <= 100]  # descartar edades muy altas #arreglar

    # junto por grupo de edad y sexo
    distribucion = arch_filtrado.groupby(["Grupo Edad", "CH04"])["PONDERA"].sum().unstack(fill_value=0)
    distribucion.columns = ["Varón", "Mujer"] if 1 in distribucion.columns else distribucion.columns

    # grafico
    fig, ax = plt.subplots(figsize=(10, 6))
    distribucion.plot(kind="bar", ax=ax)
    ax.set_title("Distribución por grupo de edad y sexo")
    ax.set_xlabel("Grupo de edad")
    ax.set_ylabel("Cantidad de personas")
    ax.legend(title="Sexo")

    ax.get_yaxis().set_major_formatter(plt.FuncFormatter(lambda x, _: f'{int(x):,}'.replace(",", ".")))
                                       
    st.pyplot(fig)


    #punto 1.3.2
    st.header("Edad promedio de personas por aglomerado (último trimestre y año disponible)")

    ult_anio = arch["ANO4"].max() 
    ult_trimestre = arch[arch["ANO4"] == ult_anio]["TRIMESTRE"].max() #me quedo con el ultimo trimestre del ultimo año

    arch_con_filtro = arch[(arch["ANO4"] == ult_anio) & (arch["TRIMESTRE"] == ult_trimestre)]

    edad_promedio = (arch_con_filtro.groupby("AGLOMERADO").apply(lambda x: (x["CH06"] * x["PONDERA"]).sum() / x["PONDERA"].sum()).sort_index())
    edad_promedio.index = edad_promedio.index.astype(int).astype(str)
    #armo el grafico de barras y lo muestro
    info, ax = plt.subplots(figsize=(10, 6))
    edad_promedio.plot(kind="bar", ax=ax)
    ax.set_title(f"Edad promedio por aglomerado - Año {int(ult_anio)}, Trimestre {int(ult_trimestre)}")
    ax.set_xlabel("Aglomerado")
    ax.set_ylabel("Edad promedio")

    st.pyplot(info)

    #punto 1.3.3
    st.header("Evolución de la dependencia demográfica por aglomerado")

    aglomerados = sorted([int(a) for a in arch["AGLOMERADO"].dropna().unique()])
    opciones = [(etiquetas_aglo.get(a, f"Aglomerado {a}"), a) for a in aglomerados]
    nombre_visible, select_aglom = st.selectbox("Seleccione un aglomerado", opciones)

    #filtro el dataframe
    df_aglo = arch[arch["AGLOMERADO"] == select_aglom]

    # clasifico por edad
    df_aglo["Grupo Edad"] = pd.cut(df_aglo["CH06"], bins=[0, 14, 64, arch["CH06"].max()], labels=["0-14", "15-64", "65+"], right=True)

    # los junto por año, trimestre y edad
    grupo = df_aglo.groupby(["ANO4", "TRIMESTRE", "Grupo Edad"])["PONDERA"].sum().unstack(fill_value=0)  

    # saco la dependencia demográfica
    grupo["Dependencia Demográfica"] = ((grupo["0-14"] + grupo["65+"]) / grupo["15-64"]) * 100


    # creo columna de periodo
    grupo["Periodo"] = grupo.index.map(lambda x: f"{int(x[0])}-T{int(x[1])}")

    # grafico y muestro
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.plot(grupo["Periodo"], grupo["Dependencia Demográfica"], marker="o")
    ax.set_title(f"Evolución de la dependencia demográfica para el aglomerado seleccionado --> {select_aglom}")
    ax.set_xlabel("Periodo")
    ax.set_ylabel("Dependencia demográfica")
    plt.xticks(rotation=45)

    st.pyplot(fig)

    #punto 1.3.4
    st.subheader("Media y Mediana de Edad por Año y Trimestre")

    # agrupo por año y trimestre y saco la media y mediana edad
    def media_ponderada(x):
        return (x["CH06"] * x["PONDERA"]).sum() / x["PONDERA"].sum()

    info_edad = (arch.groupby(["ANO4", "TRIMESTRE"]).apply(lambda g: pd.Series({"Media": media_ponderada(g),"Mediana": g["CH06"].median()}))).reset_index()

    # muestro en una tabla
    st.dataframe(info_edad)

    info_edad["Periodo"] = info_edad.apply(lambda x: f"{int(x['ANO4'])}-T{int(x['TRIMESTRE'])}", axis=1) #sobre filas

    # grafico y muestro
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.plot(info_edad["Periodo"], info_edad["Media"], marker='o', color='blue', label='Media')
    ax.plot(info_edad["Periodo"], info_edad["Mediana"], marker='s', color='orange', label='Mediana')
    ax.set_title("Media y Mediana de Edad por Año y Trimestre")
    ax.set_xlabel("Año y Trimestre")
    ax.set_ylabel("Edad")
    ax.legend()
    plt.xticks(rotation=45)
    st.pyplot(fig)