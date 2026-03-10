import csv
from pathlib import Path
import os
from config import DATA_PATH
from lectura import cargar_archivos, guardar_csv_basico
from config import RESULTADOS_PATH
import streamlit as st
import pandas as pd




def asegurar_existencia_carpeta_data():
    if not os.path.exists(DATA_PATH):
        os.makedirs(DATA_PATH)



# esta funcion se hace porque hay nombres en las variables de las encuestas que salen con minusculas
def get_ignorecase(dic, key):
    for palabra in dic:
        if palabra.lower() == key.lower():
            return dic[palabra]
    return None


# Esta funcion busca todos los archivos en la carpeta de datos y extrae los trimestres
def obtener_trimestres(carpeta_datos):
    archivos = os.listdir(carpeta_datos)
    trimestres = []

    for archivo in archivos:
        clave = extraer_clave(archivo)
        if clave and clave.startswith("T") and len(clave) == 4:
            try:
                trimestre = int(clave[1])        # T216 --> 2
                anio = 2000 + int(clave[2:])     # T216 ---> 2016
                trimestres.append((anio, trimestre))
            except:
                pass  # por si la clave no es convertible, no rompe

    if trimestres:
        trimestres.sort()
        return trimestres[0], trimestres[-1]
    else:
        return None, None
    


def extraer_clave(nombre_archivo):
    nombre = nombre_archivo.strip().lower()

    # Elimina repeticiones de ".txt", "_txt", "txt" al final
    while any(nombre.endswith(sufijo) for sufijo in [".txt", "_txt", "txt"]):
        for sufijo in [".txt", "_txt", "txt"]:
            if nombre.endswith(sufijo):
                nombre = nombre[: -len(sufijo)]
                break

    while nombre.endswith(("_", ".")):
        nombre = nombre[:-1]

    partes = []
    for frag in nombre.split("_"):
        partes.extend(frag.split("."))

    trimestre = None
    anio = None

    for parte in partes:
        # Detecta claves tipo "T216"
        if len(parte) == 4 and parte[0] == "t" and parte[1:].isdigit():
            return parte.upper()  # Ej: "T216"

        # Detecta "1to", "2to", ..., "4to"
        if parte in ["1to", "2to", "3to", "4to"]:
            trimestre = parte[0]

        # Detecta "trim2020"
        elif parte.startswith("trim20") and parte[5:].isdigit():
            anio = parte[-2:]

        # Anio suelto tipo "2020"
        elif len(parte) == 4 and parte.isdigit() and parte.startswith("20"):
            if anio is None:
                anio = parte[2:]

    if trimestre and anio:
        return f"T{trimestre}{anio}"

    return None





def verificar_existencia_archivos_matcheados(data_dir):
    archivos = os.listdir(data_dir)

    hogares = {}
    individuos = {}
    ignorados = []

    for archivo in archivos:
        nombre = archivo.lower()

        # Determinar tipo
        if "hogar" in nombre:
            tipo = "hogar"
        elif "individual" in nombre or "personas" in nombre:
            tipo = "individual"
        else:
            ignorados.append((archivo, "sin tipo reconocible"))
            continue

        clave = extraer_clave(archivo)

        if not clave:
            ignorados.append((archivo, "clave no válida"))
            continue

        if tipo == "hogar":
            hogares[clave] = archivo
        elif tipo == "individual":
            individuos[clave] = archivo

    faltantes = []

    for clave in hogares:
        if clave not in individuos:
            faltantes.append((clave, "individuos"))

    for clave in individuos:
        if clave not in hogares:
            faltantes.append((clave, "hogares"))

    return faltantes




from procesamiento_hogares import (
tipo_hogar,
densidad_hogar,
material_techumbre,
clasificar_vivienda,
porcentaje_viviendas_aglomerado,
aglomerado_mas_sin_baño
)

def generar_csv_completo_hogares():
    lista = cargar_archivos("hogar", DATA_PATH)

    tipo_hogar(lista)
    densidad_hogar(lista)
    material_techumbre(lista)
    clasificar_vivienda(lista)
    porcentaje_viviendas_aglomerado(lista)
    aglomerado_mas_sin_baño(lista)

    guardar_csv_basico(lista, RESULTADOS_PATH / "hogares_completo.csv", clave_unica=["ANO4", "TRIMESTRE"])


from procesamiento_individuos import (
traducir_ch04,
traducir_nivelED,
traducir_condicion,
universitario
)

def generar_csv_completo_individuos():
    lista = cargar_archivos("individual", DATA_PATH)

    traducir_ch04(lista)
    traducir_nivelED(lista)
    traducir_condicion(lista)
    universitario(lista)

    guardar_csv_basico(lista, RESULTADOS_PATH / "individuos_completo.csv", clave_unica=["ANO4", "TRIMESTRE"])



def chequear_inconsistencias_por_trimestre(df_hogar, df_ind):
    trimestres_hogar = df_hogar[["ANO4", "TRIMESTRE"]].drop_duplicates()
    trimestres_ind = df_ind[["ANO4", "TRIMESTRE"]].drop_duplicates()

    set_hogar = set(map(tuple, trimestres_hogar.values))
    set_ind = set(map(tuple, trimestres_ind.values))

    solo_en_hogar = set_hogar - set_ind
    solo_en_ind = set_ind - set_hogar

    inconsistencias = []
    for anio, trim in sorted(solo_en_hogar):
        inconsistencias.append((anio, trim, "individuos"))

    for anio, trim in sorted(solo_en_ind):
        inconsistencias.append((anio, trim, "hogares"))

    return inconsistencias



def verificar_inconsistencias_si_existen(archivo_hogar, archivo_ind):
    if archivo_hogar.exists() and archivo_ind.exists():
        if archivo_hogar.stat().st_size > 0 and archivo_ind.stat().st_size > 0:
            df_h = pd.read_csv(archivo_hogar, sep=";", encoding="utf-8", on_bad_lines="skip", engine="python")
            df_i = pd.read_csv(archivo_ind, sep=";", encoding="utf-8", on_bad_lines="skip", engine="python")

            inconsistencias = chequear_inconsistencias_por_trimestre(df_h, df_i)
            if inconsistencias:
                st.subheader("🔍 Inconsistencias entre hogares e individuos:")
                for anio, trim, falta in inconsistencias:
                    st.write(f"Año {anio} - Trimestre {trim} → Falta en {falta}")
            else:
                st.success(" No se encontraron inconsistencias entre hogares e individuos.")
