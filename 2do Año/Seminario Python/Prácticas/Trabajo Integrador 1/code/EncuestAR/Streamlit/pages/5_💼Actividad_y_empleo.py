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

st.header("💼 Actividad y empleo")

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

#1.5.1
st.subheader("Personas desocupadas por nivel educativo")
try:
    # cargo el CSV
    cargo_archivo = pd.read_csv(RESULTADOS_PATH / "individuos_completo.csv", sep=";", encoding="utf-8", on_bad_lines="skip")
    cargo_archivo["Nombre_aglomerado"] = cargo_archivo["AGLOMERADO"].map(etiquetas_aglo)

except FileNotFoundError:
    st.error("No se encontró el archivo de hogares.")
    cargo_archivo = None
except Exception as e:
    st.error(f"Ocurrió un error al abrir el archivo: {e}")
    cargo_archivo = None

if cargo_archivo is not None:

    # Listado y seleccion de años
    anios_disponibles = sorted(int(a) for a in cargo_archivo["ANO4"].dropna().unique())
    anio_seleccionado = st.selectbox("Seleccioná un año", anios_disponibles)

    # Listado y selección de trimestres, **filtrados** por el ano elegido
    #    Solo tomo los TRIMESTRE que existen en ese año
    trimestres_por_ano = sorted(
        int(t) for t in 
        cargo_archivo.loc[cargo_archivo["ANO4"] == anio_seleccionado, "TRIMESTRE"]
        .dropna()
        .unique()
    )
    trimestre_seleccionado = st.selectbox("Seleccioná un trimestre", trimestres_por_ano)

    #filtro por año, trimestre y desocupados
    filtrado = cargo_archivo[
        (cargo_archivo["ANO4"] == anio_seleccionado) &
        (cargo_archivo["TRIMESTRE"] == trimestre_seleccionado) &
        (cargo_archivo["CAT_OCUP"] == 3)
    ]

    #agrupo por nivel educativo y hago el conteo y USO DEL PONDERA
    conteo = (filtrado.groupby("NIVEL_ED_str")["PONDERA"].sum().reset_index().rename(columns={"NIVEL_ED_str": "Nivel educativo", "PONDERA": "Cantidad de desocupados"}))

    st.write(f"Cantidad de personas desocupadas por nivel educativo ({anio_seleccionado} - T{trimestre_seleccionado}):")
    st.dataframe(conteo)

    st.bar_chart(conteo.set_index("Nivel educativo"))

    
    #1.5.2    
    st.subheader("Evolución de la tasa de desempleo")

    #filtro las personas en edad laboral y con datos de ocupación 1 o 3
    cargo_archivo = cargo_archivo[cargo_archivo["CAT_OCUP"].isin([1, 3])]  # 1 = ocupado, 3 = desocupado

    #filtro por aglomerado
    aglomerados = cargo_archivo["Nombre_aglomerado"].dropna().unique()
    aglomerado_seleccionado = st.selectbox("Filtrar por aglomerado (opcional)", ["Todo el país"] + list(aglomerados))

    if aglomerado_seleccionado != "Todo el país":
        cargo_archivo = cargo_archivo[cargo_archivo["Nombre_aglomerado"] == aglomerado_seleccionado]


    # convierto a enteros (suponiendo que no haya nulos)
    cargo_archivo["ANO4"]      = cargo_archivo["ANO4"].astype(int)
    cargo_archivo["TRIMESTRE"] = cargo_archivo["TRIMESTRE"].astype(int)

    # ahora creo la etiqueta de periodo
    cargo_archivo["PERIODO"] = (
        cargo_archivo["ANO4"].astype(str)
        + "-T"
        + cargo_archivo["TRIMESTRE"].astype(str)
    )

    tasa = (
    cargo_archivo
    .groupby(["PERIODO", "CAT_OCUP"])["PONDERA"] # USO DEL PONDERA
    .sum()
    .unstack(fill_value=0)
    .rename(columns={1: "Ocupados", 3: "Desocupados"})
    )

    tasa["Tasa de desempleo (%)"] = (tasa["Desocupados"] / (tasa["Desocupados"] + tasa["Ocupados"])) * 100


    #calculo la tasa
    tasa["Tasa de desempleo (%)"] = (tasa["Desocupados"] / (tasa["Desocupados"] + tasa["Ocupados"])) * 100

    #muestro gráfico
    st.line_chart(tasa["Tasa de desempleo (%)"])

    #muestro tabla
    st.dataframe(tasa[["Ocupados", "Desocupados", "Tasa de desempleo (%)"]].round(2))


    #1.5.3
    st.subheader("Evolución de la tasa de empleo")

    #filtro ocupados y desocupados
    cargo_archivo = cargo_archivo[cargo_archivo["CAT_OCUP"].isin([1, 3])]  # 1 = ocupado, 3 = desocupado

    #selector de aglomerado
    aglomerados = cargo_archivo["Nombre_aglomerado"].dropna().unique()
    aglomerado_empleo = st.selectbox("Filtrar por aglomerado (opcional) - Tasa de empleo", ["Todo el país"] + list(aglomerados))

    if aglomerado_empleo != "Todo el país":
        cargo_archivo = cargo_archivo[cargo_archivo["Nombre_aglomerado"] == aglomerado_empleo]

    # convierto a enteros (suponiendo que no haya nulos)
    cargo_archivo["ANO4"]      = cargo_archivo["ANO4"].astype(int)
    cargo_archivo["TRIMESTRE"] = cargo_archivo["TRIMESTRE"].astype(int)

    # ahora creo la etiqueta de periodo
    cargo_archivo["PERIODO"] = (
        cargo_archivo["ANO4"].astype(str)
        + "-T"
        + cargo_archivo["TRIMESTRE"].astype(str)
    )

    #agrupo y hago el conteo
    tasas_empleo = (
    cargo_archivo
    .groupby(["PERIODO", "CAT_OCUP"])["PONDERA"] #USO EL PONDERA
    .sum()
    .unstack(fill_value=0)
    .rename(columns={1: "Ocupados", 3: "Desocupados"})
    )

    tasas_empleo["Tasa de empleo (%)"] = (tasas_empleo["Ocupados"] / (tasas_empleo["Ocupados"] + tasas_empleo["Desocupados"])) * 100


    tasas_empleo["Tasa de empleo (%)"] = (tasas_empleo["Ocupados"] / (tasas_empleo["Ocupados"] + tasas_empleo["Desocupados"])) * 100

    #muestro los resultados
    st.line_chart(tasas_empleo["Tasa de empleo (%)"])
    st.dataframe(tasas_empleo[["Ocupados", "Desocupados", "Tasa de empleo (%)"]].round(2))


    # 1.5.4
    st.subheader("Distribución de tipo de empleo entre ocupados por aglomerado")

    #filtro los ocupados
    cargo_archivo = cargo_archivo[cargo_archivo["CAT_OCUP"] == 1]

    #filtro los datos válidos en PP04G (tipo de ocupación)
    cargo_archivo = cargo_archivo[cargo_archivo["PP04G"].isin([1, 2, 3, 4, 5])]

    #mapeo de los tipos de ocupación
    cargo_archivo["Tipo_empleo"] = cargo_archivo["PP04G"].map({
        1: "Estatal",
        2: "Privado",
        3: "Otro",
        4: "Otro",
        5: "Otro"
    })

    #agrupo por aglomerado y tipo de empleo
    agrupado = cargo_archivo.groupby(["Nombre_aglomerado", "Tipo_empleo"])["PONDERA"].sum().unstack(fill_value=0) #USO DEL PONDERA


    #total por aglomerado
    agrupado["Total ocupados"] = agrupado.sum(axis=1)

    #calculo los porcentajes
    agrupado["% Estatal"] = (agrupado["Estatal"] / agrupado["Total ocupados"]) * 100
    agrupado["% Privado"] = (agrupado["Privado"] / agrupado["Total ocupados"]) * 100
    agrupado["% Otro"] = (agrupado["Otro"] / agrupado["Total ocupados"]) * 100

    #aca solo redondeo resultados
    resultado = agrupado[["Total ocupados", "% Estatal", "% Privado", "% Otro"]].round(2)

    st.dataframe(resultado)

    # 1.5.5
    st.subheader("Mapa de evolución de tasa de empleo o desempleo por aglomerado")

    
    cargo_archivo = pd.read_csv(RESULTADOS_PATH / "individuos_completo.csv", sep=";", encoding="utf-8")

    #filtro los datos nuevamente
    cargo_archivo = cargo_archivo[cargo_archivo["CAT_OCUP"].isin([1, 3])]  # 1: ocupado, 3: desocupado

    #determino el año y trimestre más antiguo y más reciente
    cargo_archivo["FECHA"] = pd.to_datetime(cargo_archivo["ANO4"].astype(str) + "-Q" + cargo_archivo["TRIMESTRE"].astype(str))
    min_fecha = cargo_archivo["FECHA"].min()
    max_fecha = cargo_archivo["FECHA"].max()

    df_min = cargo_archivo[cargo_archivo["FECHA"] == min_fecha]
    df_max = cargo_archivo[cargo_archivo["FECHA"] == max_fecha]

    def calcular_tasa(df, tipo):
        resumen = df.groupby(["AGLOMERADO", "CAT_OCUP"])["PONDERA"].sum().unstack(fill_value=0) #USO DEL PONDERA
        if tipo == "empleo":
            resumen["tasa"] = resumen[1] / (resumen[1] + resumen[3]) * 100
        elif tipo == "desempleo":
            resumen["tasa"] = resumen[3] / (resumen[1] + resumen[3]) * 100
        return resumen["tasa"]

    tipo_tasa = st.radio("¿Qué tasa querés visualizar?", ["Tasa de empleo", "Tasa de desempleo"])

    tipo = "empleo" if tipo_tasa == "Tasa de empleo" else "desempleo"
    tasa_min = calcular_tasa(df_min, tipo)
    tasa_max = calcular_tasa(df_max, tipo)

    #uno las tasas
    variacion = pd.DataFrame({
        "AGLOMERADO": tasa_min.index,
        "tasa_inicio": tasa_min.values,
        "tasa_final": tasa_max.reindex(tasa_min.index).values
    })

    variacion["diferencia"] = variacion["tasa_final"] - variacion["tasa_inicio"]

    #asigno el color
    def elegir_color(dif):
        if tipo == "empleo":
            return "green" if dif > 0 else "red"
        else:
            return "red" if dif > 0 else "green"

    variacion["color"] = variacion["diferencia"].apply(elegir_color)

    #agrego las coordenadas por aglomerado
    with open(RESULTADOS_PATH / "aglomerados_coordenadas.json", "r", encoding="utf-8") as f:
        datos_json = json.load(f)

    #convierto a DataFrame
    coordenadas_aglomerados = pd.DataFrame([{"AGLOMERADO": int(cod), "LAT": valor["coordenadas"][0], "LONG": valor["coordenadas"][1]}for cod, valor in datos_json.items()])

    variacion = variacion.merge(coordenadas_aglomerados, on="AGLOMERADO")

    #creo el mapa
    m = folium.Map(location=[-38, -63], zoom_start=4)

    for _, row in variacion.iterrows():
        popup_text = (
            f"Aglomerado: {row['AGLOMERADO']}<br>"
            f"Tasa inicio: {row['tasa_inicio']:.2f}%<br>"
            f"Tasa final: {row['tasa_final']:.2f}%<br>"
            f"Diferencia: {row['diferencia']:.2f}%"
        )
        folium.CircleMarker(
            location=[row["LAT"], row["LONG"]],
            radius=8,
            color=row["color"],
            fill=True,
            fill_opacity=0.7,
            popup=popup_text,
        ).add_to(m)

    st_folium(m, width=700, height=500)

