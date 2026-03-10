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

st.header("💰 Ingresos")

# Cargar archivos
try:
    hogares = pd.read_csv(RESULTADOS_PATH / "hogares_completo.csv", sep=";", encoding="utf-8", on_bad_lines="skip")
except Exception as e:
    st.error(f"No se pudo cargar el archivo de hogares: {e}")
    hogares = None

try:
    canasta = pd.read_csv(RESULTADOS_PATH / "valores-canasta-basica-alimentos-canasta-basica-total-mensual-2016.csv", sep=",", encoding="utf-8")
except Exception as e:
    st.error(f"No se pudo cargar el archivo de canasta básica: {e}")
    canasta = None

if hogares is not None and canasta is not None:
    st.subheader("Hogares bajo la línea de pobreza e indigencia")

    # Convertir fechas del archivo de canasta
    canasta["indice_tiempo"] = pd.to_datetime(canasta["indice_tiempo"])
    canasta["AÑO"] = canasta["indice_tiempo"].dt.year
    canasta["MES"] = canasta["indice_tiempo"].dt.month
    canasta["TRIMESTRE"] = ((canasta["MES"] - 1) // 3 + 1)

    # Calcular promedio trimestral de CBA y CBT
    canasta_trimestral = (
        canasta.groupby(["AÑO", "TRIMESTRE"])[["canasta_basica_total", "canasta_basica_alimentaria"]]
        .mean()
        .reset_index()
        .rename(columns={
            "canasta_basica_total": "CBT_promedio",
            "canasta_basica_alimentaria": "CBA_promedio"
        })
    )

    # muestra opciones al usuario
    # aseguraque hogares tenga columnas numericas x las dudas pq tiraba error
    hogares["ANO4"] = pd.to_numeric(hogares["ANO4"], errors="coerce")
    hogares["TRIMESTRE"] = pd.to_numeric(hogares["TRIMESTRE"], errors="coerce")

    # Detectar años y trimestres disponibles en el dataset de hogares
    anios_disponibles = sorted(hogares["ANO4"].dropna().unique().astype(int))
    anio_sel = st.selectbox("Seleccioná un año", anios_disponibles)

    trimestres_disponibles = sorted(hogares[hogares["ANO4"] == anio_sel]["TRIMESTRE"].dropna().unique().astype(int))
    trim_sel = st.selectbox("Seleccioná un trimestre", trimestres_disponibles)

    # Obtener valores promedio para ese año y trimestre
    valores_canasta = canasta_trimestral[
        (canasta_trimestral["AÑO"] == anio_sel) & (canasta_trimestral["TRIMESTRE"] == trim_sel)
    ].iloc[0]

    CBT = valores_canasta["CBT_promedio"]
    CBA = valores_canasta["CBA_promedio"]

    # Filtrar hogares del año y trimestre seleccionados
    hogares["ANO4"] = pd.to_numeric(hogares["ANO4"], errors="coerce")
    hogares["TRIMESTRE"] = pd.to_numeric(hogares["TRIMESTRE"], errors="coerce")
    hogares["IX_TOT"] = pd.to_numeric(hogares["IX_TOT"], errors="coerce") # CANTIDAD DE INTEGRANTES
    hogares["ITF"] = pd.to_numeric(hogares["ITF"], errors="coerce") #MONTO INGRESO TOTAL FAMILIAR

    filtro = (hogares["ANO4"] == anio_sel) & (hogares["TRIMESTRE"] == trim_sel) & (hogares["IX_TOT"] == 4)
    hogares_filtrados = hogares[filtro].copy()

    # Calcular totales
    total = hogares_filtrados["PONDERA"].sum()
    pobres = hogares_filtrados[hogares_filtrados["ITF"] < CBT]["PONDERA"].sum()
    indigentes = hogares_filtrados[hogares_filtrados["ITF"] < CBA]["PONDERA"].sum()

    # Mostrar resultados
    st.markdown(f"### Resultados para {anio_sel} - Trimestre {trim_sel}")
    st.write(f" Hogares de 4 integrantes analizados: **{total}**")

    if total > 0:
        st.write(f" Bajo la linea de pobreza: **{pobres}** → {pobres/total*100:.2f}%")
        st.write(f" Bajo la linea de indigencia: **{indigentes}** → {indigentes/total*100:.2f}%")
    else:
        st.warning("No hay hogares de 4 integrantes para ese período. Cambiá el año o trimestre.")

