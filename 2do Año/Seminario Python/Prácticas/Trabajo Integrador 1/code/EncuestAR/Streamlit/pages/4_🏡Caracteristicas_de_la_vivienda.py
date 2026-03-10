import streamlit as st
import os  # Importa os para poder trabajar con carpetas y archivos
import sys
import pandas as pd
import matplotlib.pyplot as plt
import json
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

st.header("🏡 Características de la vivienda") 
st.markdown("En esta sección se visualizará información relacionada a la características de la vivienda de la población argentina según la EPH. ")  

# Dicc de etiquetas para interpretar los cod numericoss de las columnas IV1, IV3, II7
etiquetas_iv1 = {
    1: "Casa",
    2: "Departamento",
    3: "Pieza de inquilinato",
    4: "Pieza en hotel/pensión",
    5: "Local no construido para habitacion"
}
etiquetas_iv3 = {
    1: "Mosaico/Baldosa/Madera/Ceramica/Alfombra",
    2: "Cemento/Ladrillo fijo",
    3: "Ladrillo suelto/Tierra"
}
etiquetas_ii7 = {
    1: "Propietario (vivienda y terreno)",
    2: "Propietario (solo vivienda)",
    3: "Inquilino",
    4: "Ocupante por pago de impuestos/expensas",
    5: "Ocupante en relacion de dependencia",
    6: "Ocupante gratuito (con permiso)",
    7: "Ocupante de hecho (sin permiso)",
    8: "Sucesión"
}

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

archivo = RESULTADOS_PATH / "hogares_completo.csv"  # este es el archivo a usar


try:
    df = pd.read_csv(archivo, sep=";", encoding="utf-8", on_bad_lines="skip")
except FileNotFoundError:
    st.error("No se encontró el archivo de hogares.")
    df = None
except Exception as e:
    st.error(f"Ocurrió un error al abrir el archivo: {e}")
    df = None

if df is not None:
    df["ANO4"] = pd.to_numeric(df["ANO4"], errors="coerce")  # Asegura que ANO4 sea numerico xq me tiraba error en un grafico

    anios_disponibles = sorted(df["ANO4"].dropna().unique())  # lista de anios en los datos
    anio_seleccionado = st.selectbox("Seleccione un año para filtrar (o deje vacío para usar todos los datos):", ["Todos"] + list(map(str, anios_disponibles)))  

    if anio_seleccionado != "Todos":  # Si se eligio un anio, filtra por el dataframe de ese anio # un dataframe es como una nueva tabla en pandas con esa info
        df = df[df["ANO4"] == int(anio_seleccionado)]

    st.subheader("1.4.1 Cantidad total de viviendas")  
    total_viviendas = df["PONDERA"].sum()  # suma total ponderada de las viviendas
    st.write(f"Cantidad total estimada de viviendas: {int(total_viviendas):,}")  # aca muestra el total con separador de miles




    st.subheader("1.4.2 Proporción de viviendas por tipo (gráfico de torta)")

    # Me quedo solo con los valores validos
    df = df[df["IV1"].isin(etiquetas_iv1)]

    # agrupo por tipo de vivienda y sumo con pondera
    agrupado = df.groupby("IV1")["PONDERA"].sum()

    # calculo el total para saber los porcentajes
    total = agrupado.sum()
    porcentajes = (agrupado / total) * 100

    # redondeo los porcentajes y armo etiquetas
    etiquetas = []
    for codigo in agrupado.index:
        nombre = etiquetas_iv1[codigo]
        porcentaje = round(porcentajes[codigo], 1)
        etiquetas.append(f"{nombre}: {porcentaje}%")

    # uso el explode para que separe del grafico a los valores chiquitos que no llegaban a verse bien
    explode = []
    for p in porcentajes:
        if p < 2:
            explode.append(0.1)
        else:
            explode.append(0)

    # hago el grafico de torta
    fig, ax = plt.subplots()
    wedges, texts = ax.pie(
        agrupado,
        labels=None,        # no muestra el texto encima
        autopct=None,       # no muestra el porcentaje en la torta
        explode=explode,
        startangle=90
    )

    # agrego la leyenda con los nombres y porcentajes
    ax.legend(wedges, etiquetas, title="Tipo de vivienda", loc="center left", bbox_to_anchor=(1, 0.5))

    # hago q el grafico sea circular
    ax.axis('equal')

    # se ajusta y muestra elgrafico de torta
    plt.tight_layout()
    st.pyplot(fig)

    
    
    st.subheader("1.4.3 Material predominante en pisos por aglomerado") #usar pondera

    # traduce los codigos de materiales a nombres legibles
    df["Material_piso"] = df["IV3"].map(etiquetas_iv3)

    # hago una ista para guardar el resultado por aglomerado
    material_por_aglomerado = []

    # recorro los aglomerados uno por uno
    for aglo in df["AGLOMERADO"].unique():
        datos = df[df["AGLOMERADO"] == aglo]  # filtro por aglomerado
        ponderado = datos.groupby("Material_piso")["PONDERA"].sum()
           
        if not ponderado.empty:
            piso = ponderado.idxmax()  # material con mayor suma de pondera
        else:
            piso = "Sin datos"
        material_por_aglomerado.append({   #agrego esto para q aparezca el nombre del aglomerado
            "Aglomerado": etiquetas_aglo.get(aglo, f"Aglomerado {aglo}"),
            "Material Predominante": piso
        })


    # convierto la lista en dataframe
    resultado = pd.DataFrame(material_por_aglomerado)

    # uso el nombre del aglomerado como indice
    resultado = resultado.set_index("Aglomerado").sort_index()

    # muestro sin indice visual adicional
    st.dataframe(resultado)



    st.subheader("1.4.4 Proporción de viviendas con baño dentro del hogar")

    # lista para guardar resultados
    resultados = []

    # recorro cada aglomerado unico
    for aglo in df["AGLOMERADO"].unique():
        datos_aglo = df[df["AGLOMERADO"] == aglo]  # filtro por aglomerado

        # sumo la ponderacion total de viviendas
        total = datos_aglo["PONDERA"].sum()

        # sumo la ponderacion de viviendas con baño (IV8 = 1)
        con_banio = datos_aglo[datos_aglo["IV8"] == 1]["PONDERA"].sum()

        # calculo el porcentaje
        if total > 0:
            porcentaje = round((con_banio / total) * 100, 2)
        else:
            porcentaje = 0.0

        resultados.append({
            "AGLOMERADO": etiquetas_aglo.get(aglo, f"Aglomerado {aglo}"),
            "% con baño": f"{porcentaje:.2f}%"
        })
    # muestro los resultados como tabla
    tabla = pd.DataFrame(resultados)
    tabla = tabla.set_index("AGLOMERADO").sort_index()
    st.dataframe(tabla)


    st.subheader("1.4.5 Evolución de tenencia por aglomerado")

    # lista de aglomerados por nombre, pero devuevle el nro de aglomerado para el codigo. Los ordeno alfabetucamente antes

    aglos_ordenados = sorted(etiquetas_aglo.keys(), key=lambda x: etiquetas_aglo[x])

    aglo_sel = st.selectbox(
        "Seleccione un aglomerado:",
        aglos_ordenados,
        format_func=lambda x: etiquetas_aglo.get(x, f"Aglomerado {x}")
    )

    # convierte los codigos de tenencia a texto usando el diccionario definido mas arrba
    df["II7_LABEL"] = df["II7"].map(etiquetas_ii7)
    df["II7_LABEL"] = df["II7_LABEL"].fillna("Otro")  # si hay valores no mapeados

    # obtengo lista de tenencias disponibles
    tenencias_disponibles = df["II7_LABEL"].dropna().unique().tolist()
    tenencias_disponibles.sort()
    ten_sel = st.multiselect("Seleccione tipo(s) de tenencia:", tenencias_disponibles, default=tenencias_disponibles)

    # filtrar por aglomerado y tipo de tenencia
    df_filtrado = df[df["AGLOMERADO"] == aglo_sel]
    df_filtrado = df_filtrado[df_filtrado["II7_LABEL"].isin(ten_sel)]

    # Convierte anio a numero por si hay errores de texto pq me tiraba error
    df_filtrado["ANO4"] = pd.to_numeric(df_filtrado["ANO4"], errors="coerce")

    if df_filtrado.empty:
        st.warning("No hay datos disponibles para ese aglomerado y selección.")
    else:
        # agrupar los datos por anio y tipo de tenencia
        datos_agrupados = df_filtrado.groupby(["ANO4", "II7_LABEL"])["PONDERA"].sum()

        # reorganiza los datos para graficarlos
        datos_grafico = datos_agrupados.reset_index()

        # crea figura y grafica manualmente por tenencia
        fig, ax = plt.subplots()

        for tenencia in ten_sel:
            datos_t = datos_grafico[datos_grafico["II7_LABEL"] == tenencia]
            ax.plot(datos_t["ANO4"], datos_t["PONDERA"], marker="o", label=tenencia)

        ax.set_title("Evolución de tenencia")
        ax.set_xlabel("Año")
        ax.set_ylabel("Ponderación total")
        ax.set_xlim(2015, 2025)
        ax.set_xticks(list(range(2015, 2026)))
        ax.legend(loc="center left", bbox_to_anchor=(1, 0.5))

        st.pyplot(fig)


    st.subheader("1.4.6 Viviendas en villa de emergencia por aglomerado")

    # filtra las filas donde IV12_3 vale 1 (es villa)
    df_villas = df[df["IV12_3"] == 1]

    # agrupa y suma la ponderacion para saber cuantas viviendas hay en villas por aglomerado
    conteo_villas = df_villas.groupby("AGLOMERADO")["PONDERA"].sum()

    # total de viviendas por aglomerado
    conteo_total = df.groupby("AGLOMERADO")["PONDERA"].sum()

    # calcular el porcentaje (puede haber valores nulos si algun aglomerado no tiene villas)
    porcentaje_villa = (conteo_villas / conteo_total) * 100

    # Reemplazar los NaN por 0 porq me mostraba en el grafico nan
    porcentaje_villa = porcentaje_villa.fillna(0)
    conteo_villas = conteo_villas.fillna(0)

    # crea un nuevo datarframe con los resultados
    villa_resultado = pd.DataFrame()
    villa_resultado["Cantidad"] = conteo_villas
    villa_resultado["Porcentaje"] = porcentaje_villa

    # ordena de mayor a menor cantidad
    villa_resultado = villa_resultado.sort_values("Cantidad", ascending=False)
    villa_resultado = villa_resultado.rename(index=etiquetas_aglo) # para mostrar los aglomerados con nombre

    # muestra en el streamlit
    st.dataframe(villa_resultado)



    st.subheader("1.4.7 Condición de habitabilidad por aglomerado")

    # calculaa la cantidad de viviendas por aglomerado y condicion
    df_condiciones = df.groupby(["AGLOMERADO", "CONDICION_DE_HABITABILIDAD"])["PONDERA"].sum()
    df_condiciones = df_condiciones.reset_index()

    # calculaa el total de viviendas por aglomerado
    df_totales = df.groupby("AGLOMERADO")["PONDERA"].sum()
    df_totales = df_totales.reset_index()
    df_totales = df_totales.rename(columns={"PONDERA": "TOTAL"})

    # junta los dos resultados
    df_completo = pd.merge(df_condiciones, df_totales, on="AGLOMERADO")

    # calcula el porcentaje
    df_completo["PORCENTAJE"] = (df_completo["PONDERA"] / df_completo["TOTAL"]) * 100
    df_completo["PORCENTAJE"] = df_completo["PORCENTAJE"].round(2)

    # creaa tabla final con porcentajes (una columna por condicion
    tabla_final = df_completo.pivot( # hace que se vea mejor y no aparezca triplicado todo
        index="AGLOMERADO",
        columns="CONDICION_DE_HABITABILIDAD",
        values="PORCENTAJE"
    )


    # reemplaza NaNs con 0
    tabla_final = tabla_final.fillna(0)

    # reemplaza el indice por nombre legible
    tabla_final = tabla_final.rename(index=etiquetas_aglo)

    # ordena alfabeticamente por nombre de aglomerado
    tabla_final = tabla_final.sort_index()

    # muestra tabla sin indice numerico
    st.dataframe(tabla_final)

    # exporta CSV para descarga
    csv = tabla_final.reset_index().to_csv(index=False).encode("utf-8")
    st.download_button("Descargar CSV", data=csv, file_name="habitabilidad_por_aglomerado.csv", mime="text/csv")
