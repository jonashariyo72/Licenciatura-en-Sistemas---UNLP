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

st.header("📝 Educación")

# individuos es unDF y hogares tmb
try:
    hogares = pd.read_csv(RESULTADOS_PATH / "hogares_completo.csv", sep=";", encoding="utf-8", on_bad_lines="skip")
except FileNotFoundError:
    st.error("No se encontró el archivo 'hogares_completo.csv'.")
    hogares = None
except Exception as e:
    st.error(f"Error al abrir 'hogares_completo.csv': {e}")
    hogares = None

try:
    individuos = pd.read_csv(RESULTADOS_PATH / "individuos_completo.csv", sep=";", encoding="utf-8", on_bad_lines="skip")
except FileNotFoundError:
    st.error("No se encontró el archivo 'individuos_completo.csv'.")
    individuos = None
except Exception as e:
    st.error(f"Error al abrir 'individuos_completo.csv': {e}")
    individuos = None

if individuos is not None:
    # 1.6.1
    st.subheader("Cantidad de personas por nivel educativo alcanzado")

    # asegunra de q la columna es numerica (floats o NaN)
    individuos["ANO4"] = pd.to_numeric(individuos["ANO4"], errors="coerce")

    # filtra las filas donde ANO4 no sea NaN
    individuos = individuos[individuos["ANO4"].notna()]

    # hora deja convertir a entero sin problemas
    individuos["ANO4"] = individuos["ANO4"].astype(int)


    años = sorted(individuos["ANO4"].unique())
    año = st.selectbox("Seleccioná un año", años)

    df_filtrado = individuos[individuos["ANO4"] == año]
    niveles = df_filtrado["NIVEL_ED_str"].value_counts().reset_index()
    niveles.columns = ["Nivel educativo", "Cantidad de personas"]

    st.dataframe(niveles)
    st.bar_chart(niveles.set_index("Nivel educativo"))



    # 1.6.2
    st.subheader("Nivel educativo más común por grupo etario")
    # Convertir CH05 a datetime si no lo hiciste antes
    individuos["CH05"] = pd.to_datetime(individuos["CH05"], format="%d/%m/%Y", errors="coerce")

    rangos = [(20, 30), (30, 40), (40, 50), (50, 60), (60, 101)]
    opciones = [f"{r[0]}-{r[1]}" for r in rangos] + ["Todos"]
    seleccion = st.multiselect("Seleccioná uno o más rangos etarios", opciones, default=["Todos"])

    if "Todos" in seleccion:
        seleccion = opciones[:-1]

    resultados = []
    for r in seleccion:
        edad_min, edad_max = map(int, r.split("-"))

        # Calcular edad en función del año de referencia (ANO4) y año de nacimiento (CH05)
        # Edad aproximada = ANO4 - año de nacimiento
        nacimiento_año = individuos["CH05"].dt.year
        edad = individuos["ANO4"] - nacimiento_año

        # Filtrar filas con edad en el rango
        df_rango = individuos[(edad >= edad_min) & (edad < edad_max)]

        if not df_rango.empty:
            nivel_mas_comun = df_rango["NIVEL_ED_str"].mode().iloc[0]
            resultados.append({"Rango etario": r, "Nivel educativo más común": nivel_mas_comun})

    st.dataframe(pd.DataFrame(resultados))

if individuos is not None and hogares is not None:

    # 1.6.3
    st.subheader("Ranking de aglomerados con mayor porcentaje de hogares con universitarios")

    # convierte las columnas claves a texto para poder combinarlas
    individuos["CODUSU"] = individuos["CODUSU"].astype(str)
    individuos["NRO_HOGAR"] = individuos["NRO_HOGAR"].astype(str)
    individuos["AGLOMERADO"] = individuos["AGLOMERADO"].astype(str)
    individuos["hogar_id"] = individuos["AGLOMERADO"] + "_" + individuos["CODUSU"] + "_" + individuos["NRO_HOGAR"]

    hogares["CODUSU"] = hogares["CODUSU"].astype(str)
    hogares["NRO_HOGAR"] = hogares["NRO_HOGAR"].astype(str)
    hogares["AGLOMERADO"] = hogares["AGLOMERADO"].astype(str)
    hogares["hogar_id"] = hogares["AGLOMERADO"] + "_" + hogares["CODUSU"] + "_" + hogares["NRO_HOGAR"]

    #  convierte anio y trimestre a numero (por si están mal cargados)
    individuos["ANO4"] = pd.to_numeric(individuos["ANO4"], errors="coerce")
    individuos["TRIMESTRE"] = pd.to_numeric(individuos["TRIMESTRE"], errors="coerce")
    hogares["ANO4"] = pd.to_numeric(hogares["ANO4"], errors="coerce")
    hogares["TRIMESTRE"] = pd.to_numeric(hogares["TRIMESTRE"], errors="coerce")

    # busca fechas que esten en los dos archivos para poder comparar mismo momento, pq si no, no sirve
    fechas_hogares = set(zip(hogares["ANO4"].dropna(), hogares["TRIMESTRE"].dropna()))
    fechas_individuos = set(zip(individuos["ANO4"].dropna(), individuos["TRIMESTRE"].dropna()))
    fechas_comunes = sorted(fechas_hogares & fechas_individuos)



    if len(fechas_comunes) < 1:
        st.warning("No hay datos coincidentes en hogares e individuos para hacer el ranking.")
    else:
        # tomamos las 2 fechas más recientes
        ultimas_dos = fechas_comunes[-2:]

        # filtra los individuos de esas fechas
        ind = individuos[individuos[["ANO4", "TRIMESTRE"]].apply(tuple, axis=1).isin(ultimas_dos)].copy()

        # convierte columnas necesarias
        ind["UNIVERSITARIO"] = pd.to_numeric(ind["UNIVERSITARIO"], errors="coerce")
        ind["PONDERA"] = pd.to_numeric(ind["PONDERA"], errors="coerce")

        # nos quedamos con universitarios solamente
        ind_universitarios = ind[ind["UNIVERSITARIO"] == 1]

        # agrupa por hogar y suma la ponderacion
        suma_por_hogar = ind_universitarios.groupby(["hogar_id", "AGLOMERADO"])["PONDERA"].sum().reset_index()
        suma_por_hogar["con_2_o_mas"] = (suma_por_hogar["PONDERA"] >= 2).astype(int)

        # sacar lista de todos los hogares unicos
        hogares_unicos = ind[["hogar_id", "AGLOMERADO", "PONDERA"]].drop_duplicates()  ### MODIFICADO
        hogares_unicos["total"] = hogares_unicos["PONDERA"] ## MODIFICADO

        # unimos los hogares con la info de universitarios
        resultado = hogares_unicos.merge(suma_por_hogar[["hogar_id", "con_2_o_mas"]], on="hogar_id", how="left")
        resultado["con_2_o_mas"] = resultado["con_2_o_mas"].fillna(0)

        # agrupa por aglomerado y calcula totales
        resumen = resultado.groupby("AGLOMERADO").agg(
            total_hogares=("total", "sum"),
            con_2_o_mas_universitarios=("con_2_o_mas", "sum")
        ).reset_index()

        resumen["porcentaje"] = (resumen["con_2_o_mas_universitarios"] / resumen["total_hogares"]) * 100

        # mostrar top 5 aglomerados
        ranking = resumen.sort_values("porcentaje", ascending=False).round(2).head(5)
        st.dataframe(ranking)

        # boton para descargar CSV
        csv = ranking.to_csv(index=False).encode("utf-8")
        st.download_button("Descargar CSV", data=csv, file_name="ranking_aglomerados_universitarios.csv", mime="text/csv")

if individuos is not None:
    # 1.6.4
    st.subheader("Porcentaje de personas mayores de 6 años capaces de leer y escribir")
    df = pd.read_csv(RESULTADOS_PATH / "individuos_completo.csv", sep=";", encoding="utf-8")


    # nos aseguramos de que las columnas clave existan
    if 'CH06' in df.columns and 'CH09' in df.columns and 'ANO4' in df.columns:
        # filtra personas > de 6
        df = df[df['CH06'] > 6]

        # Filtra personas con valores validos en CH09 (1 sí, 2  no)
        df = df[df['CH09'].isin([1, 2])]

        # creaa una lista para guardar los resultados
        resultado = []

        # recorre cada anio unico
        for año in sorted(df['ANO4'].dropna().unique()):
            datos_del_año = df[df['ANO4'] == año]

            total = len(datos_del_año)
            saben = len(datos_del_año[datos_del_año['CH09'] == 1])
            no_saben = len(datos_del_año[datos_del_año['CH09'] == 2])

            porcentaje_saben = (saben / total) * 100 if total > 0 else 0
            porcentaje_no_saben = (no_saben / total) * 100 if total > 0 else 0

            resultado.append({
                "Año": int(año),
                "Saben leer y escribir (%)": round(porcentaje_saben, 2),
                "No saben leer y escribir (%)": round(porcentaje_no_saben, 2)
            })

        # convierte rdos a tabla
        resultado_df = pd.DataFrame(resultado)

        # muestra la tabla
        st.write("Porcentaje por año:")
        st.dataframe(resultado_df)

        # boton para descargar CSV
        csv = resultado_df.to_csv(index=False).encode('utf-8')
        st.download_button("Descargar CSV", data=csv, file_name="alfabetismo.csv", mime="text/csv")

    else:
        st.error("Tu archivo no tiene la informacion necesaria")