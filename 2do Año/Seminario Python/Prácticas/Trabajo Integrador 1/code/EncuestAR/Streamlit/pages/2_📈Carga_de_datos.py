import streamlit as st
import os
import sys
import pandas as pd
import matplotlib.pyplot as plt
import json
import folium
from streamlit_folium import st_folium
import io

# arega la carpeta src al sys.path (necesario porque estamos  en /pages/)
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
SRC_DIR = os.path.join(BASE_DIR, 'src')

if SRC_DIR not in sys.path:
    sys.path.append(SRC_DIR)

print("SRC DIR:", SRC_DIR)
print("SYS PATH:", sys.path)

# al hacer eso de arriba ahora los imports funcionan
from utils import obtener_trimestres, asegurar_existencia_carpeta_data, verificar_existencia_archivos_matcheados, chequear_inconsistencias_por_trimestre, verificar_inconsistencias_si_existen
from lectura import guardar_csv_basico, cargar_archivos
from config import DATA_PATH, RESULTADOS_PATH, SRC_PATH
from procesamiento_individuos import ranking_aglomerados_estudios, pueden_leer

# Ruta de los archivos
carpeta_datos = DATA_PATH
archivo_hogar = RESULTADOS_PATH / "hogar_unificado.csv"
archivo_ind = RESULTADOS_PATH / "individuos_unificado.csv"

archivo_hogares_completo = RESULTADOS_PATH / "hogares_completo.csv"
archivo_individuos_completo = RESULTADOS_PATH / "individuos_completo.csv"

st.header("📈 Carga de datos")
st.subheader("Subir archivos TXT")

uploaded_files = st.file_uploader(
    "Seleccioná uno o más archivos TXT para cargar al sistema. Una vez cargados, selecciona la opcion de ***Actualizar Dataset*** para que sean incorporados a la base de datos. Luego de este paso o si ya tenias archivos cargados, podes verificar si hay inconsistencias entre los dataset cargados seleccionando el boton ***Verificar inconsistencias por trimestre***",
    type=["txt"],
    accept_multiple_files=True
)

if uploaded_files:
    os.makedirs(DATA_PATH, exist_ok=True)  # Crea la carpeta si no existe
    archivos_validos = 0

    for uploaded_file in uploaded_files:
        # Validación: nombre debe contener "usu" sin importar mayúsculas
        if "usu" in uploaded_file.name.lower():
            save_path = os.path.join(DATA_PATH, uploaded_file.name)
            with open(save_path, "wb") as f:
                f.write(uploaded_file.read())
            archivos_validos += 1
        else:
            st.warning(f"{uploaded_file.name} --> Archivo ignorado por nombre inválido")

    if archivos_validos > 0:
        st.success(f"{archivos_validos} archivo(s) TXT válidos cargado(s) correctamente en la carpeta de datos.")
    else:
        st.error("No se subió ningún archivo válido. Asegurate de que sea un archivo de la EPH.")

    # llama a la funciOn y guarda el primer y ULT trimestre 
    primero, ultimo = obtener_trimestres(carpeta_datos)

    if primero and ultimo:  # si se encontraron trimestres validos
        st.write(f"El sistema tiene informacion desde el {primero[1]:02}/{primero[0]} hasta el {ultimo[1]:02}/{ultimo[0]}")
    else:
        st.warning("No se encontraron archivos de datos en la carpeta '../data'.")

if st.button("Actualizar dataset"):

    archivos = os.listdir(DATA_PATH)  # Lista todos los archivos en la carpeta de datos

    if not archivos:  # si no hay ningún archivo, muestra error y no sigue
        st.error("No se encontraron archivos en la carpeta de datos.")
    else:
        # hace el chequeo solo si hay archivos presentes
        faltantes = verificar_existencia_archivos_matcheados(DATA_PATH)

        # hastaaca
        datos_hogar = None
        datos_ind = None

        # Procesa archivos de hogar
        try:
            datos_hogar = cargar_archivos(tipo="hogar", data_path=DATA_PATH)
            guardar_csv_basico(datos_hogar, RESULTADOS_PATH / "hogar_unificado.csv", clave_unica=["ANO4", "TRIMESTRE"]) # SE AGREGO ESTO PARA Q NO REPITA LOS DATOS CADA VEZ Q SE APRIETA ACTUALIZAR 
        except FileNotFoundError:
            pass  # No muestra ningun msj aun
        except Exception as e:
            st.error(f"Error al procesar archivos de hogar: {e}")

        # Procesa archivos de individuos
        try:
            datos_ind = cargar_archivos(tipo="individual", data_path=DATA_PATH)
            guardar_csv_basico(datos_ind, RESULTADOS_PATH / "individuos_unificado.csv", clave_unica=["ANO4", "TRIMESTRE"]) # SE AGREGO ESTO PARA Q NO REPITA LOS DATOS CADA VEZ Q SE APRIETA ACTUALIZAR )
        except FileNotFoundError:
            pass  # No muestra ningun msj tdv
        except Exception as e:
            st.error(f"Error al procesar archivos de individuos: {e}")

        # Verifica la existencia de archivos, si se subieron o no
        archivo_hogar = RESULTADOS_PATH / "hogar_unificado.csv"
        archivo_ind = RESULTADOS_PATH / "individuos_unificado.csv"

        if archivo_hogar.exists() and not archivo_ind.exists():
            st.warning("Aclaracion: solo se subieron archivos de hogares.")
        elif archivo_ind.exists() and not archivo_hogar.exists():
            st.warning("Aclaracion: solo se subieron archivos de individuos.")
        elif not archivo_hogar.exists() and not archivo_ind.exists():
            st.error("No se creo ningun archivo.")
        else:
            mensaje = "Archivos creados:"
            if archivo_hogar.exists():
                mensaje += "\n- hogar_unificado.csv"
            if archivo_ind.exists():
                mensaje += "\n- individuos_unificado.csv"
            st.success(mensaje)

    # Verifica si se genero el archivo de hogares unificado para llamar a todas las funciones, agregar columnas y crear el csv completo de hogares 
    if archivo_hogar.exists() and archivo_hogar.stat().st_size > 0:
        try:
            from utils import generar_csv_completo_hogares
            generar_csv_completo_hogares()
        except Exception as e:
            pass  # silencioso
            print("Error al generar hogares completo:", e)

    
            # Verifica si se genero el archivo de ind unificado para llamar a todas las funciones, agregar columnas y crear el csv completo de hogares 
    if archivo_ind.exists() and archivo_ind.stat().st_size > 0:
        try:
            from utils import generar_csv_completo_individuos
            generar_csv_completo_individuos()
        except:
            pass  # silencioso


# Boton manual para verificar inconsistencias en datos completos
# Chequeo manual de inconsistencias por trimestre usando hogares_completo e individuos_completo

archivo_hogares_completo = RESULTADOS_PATH / "hogares_completo.csv"
archivo_individuos_completo = RESULTADOS_PATH / "individuos_completo.csv"

# Solo mostramos el boton si al menos uno de los archivos existe y tiene contenido
tiene_hogares = archivo_hogares_completo.exists() and archivo_hogares_completo.stat().st_size > 0
tiene_individuos = archivo_individuos_completo.exists() and archivo_individuos_completo.stat().st_size > 0

if tiene_hogares or tiene_individuos:
    if st.button("🔍 Verificar inconsistencias por trimestre"):
        inconsistencias = []

        if tiene_hogares:
            df_h = pd.read_csv(archivo_hogares_completo, sep=";", encoding="utf-8", engine="python", on_bad_lines="skip")
            trimestres_hogar = df_h[["ANO4", "TRIMESTRE"]].drop_duplicates()
        else:
            trimestres_hogar = pd.DataFrame(columns=["ANO4", "TRIMESTRE"])

        if tiene_individuos:
            df_i = pd.read_csv(archivo_individuos_completo, sep=";", encoding="utf-8", engine="python", on_bad_lines="skip")
            trimestres_ind = df_i[["ANO4", "TRIMESTRE"]].drop_duplicates()
        else:
            trimestres_ind = pd.DataFrame(columns=["ANO4", "TRIMESTRE"])

        # Pasamos los valores a conjuntos para comparar mas facil
        set_hogar = set(tuple(x) for x in trimestres_hogar.values)
        set_ind = set(tuple(x) for x in trimestres_ind.values)

        # busca trimestres que estan en hogares pero no en individuos
        solo_en_hogar = set_hogar - set_ind
        for anio, trim in sorted(solo_en_hogar):
            inconsistencias.append((anio, trim, "individuos"))

        # busca trimestres que estan en individuos pero no en hogares
        solo_en_ind = set_ind - set_hogar
        for anio, trim in sorted(solo_en_ind):
            inconsistencias.append((anio, trim, "hogares"))

        # muestra resultado
        if inconsistencias:
            st.warning("Se encontraron inconsistencias entre hogares e individuos:")
            for anio, trim, falta in inconsistencias:
                st.write(f"Año {anio} - Trimestre {trim} → falta en {falta}")
        else:
            st.success("✅ No se encontraron inconsistencias entre hogares e individuos.")

