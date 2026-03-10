import csv
from pathlib import Path
import os
from config import RESULTADOS_PATH


def cargar_archivos(tipo=None, data_path=Path("data")):
    if tipo not in ("individual", "hogar"):
        raise ValueError("El tipo debe ser 'individual' o 'hogar'.")

    if not data_path.exists() or not data_path.is_dir():
        raise FileNotFoundError(f"El path {data_path} no existe o no es un directorio válido.")

    # acepta prefijos con maysc o min y extensiones variadas
    archivos = [ruta for ruta in data_path.iterdir()
                if ruta.is_file()
                and ruta.name.lower().startswith(f"usu_{tipo}_")
                and ruta.name.lower().endswith((".txt", ".txt.txt"))]

    # archivos con nombres distintos
    if tipo == "individual":
        archivos += list(data_path.glob("EPH_usu_personas_*.txt"))
    elif tipo == "hogar":
        archivos += list(data_path.glob("EPH_usu_hogar_*.txt"))

    if not archivos:
        raise FileNotFoundError(f"No se encontraron archivos con patron '{tipo}' en {data_path}")

    datos = []
    for archivo in archivos:
        try:
            with open(archivo, encoding="utf-8") as f:
                lector = csv.reader(f, delimiter=";")
                encabezado = next(lector)
                for fila in lector:
                    if len(fila) == len(encabezado):
                        datos.append(dict(zip(encabezado, fila)))
                    else:
                        print(f"Fila descartada en {archivo.name}: {fila}") # esto es para evitar procesar una fila mal cargada, q le faltan datos
        except Exception as e:
            print(f"Error al leer {archivo.name}: {e}")

    return datos


# se modifico para q no vuelva a cargar el encabezado y para que no duplique cada vez que se aprieta en actualizar dataset en streamlit
def guardar_csv_basico(datos, salida_path, forma="a", clave_unica=None):
    salida_path = Path(salida_path)
    salida_path.parent.mkdir(parents=True, exist_ok=True)  # Asegura que exista la carpeta

    if not datos:
        print("No hay datos para guardar.")
        return

    encabezado = list(datos[0].keys())
    datos_nuevos = datos.copy()# crea una copia de la lista para filtrar sin modificar el original


    archivo_existe = salida_path.exists()
    archivo_vacio = not archivo_existe or salida_path.stat().st_size == 0

 # Cargar claves existentes si se especifica clave_unica y el archivo ya tiene contenido
    claves_existentes = set()
    if clave_unica and archivo_existe and not archivo_vacio:
        with open(salida_path, newline="", encoding="utf-8") as archivo:
            lector = csv.DictReader(archivo, delimiter=";")
            for fila in lector:
                clave = tuple(str(fila.get(k, "")).strip() for k in clave_unica)
                claves_existentes.add(clave)

        datos_nuevos = []
        descartados = []

        for fila in datos:
            clave = tuple(str(fila.get(k, "")).strip() for k in clave_unica)  # # genera una tupla con las claves únicas, pasadas a texto y sin espacios para comparar si existe
            if clave not in claves_existentes:
                datos_nuevos.append(fila)
            else:
                descartados.append(clave)

        print(f"Se descartaron {len(descartados)} filas duplicadas. Claves ya existentes:")
    if not datos_nuevos:
        print("No hay datos nuevos para guardar.")
        return

    with open(salida_path, mode=forma, newline="", encoding="utf-8") as archivo:
        escritor = csv.writer(archivo, delimiter=";")

        if archivo_vacio or forma == "w":
            escritor.writerow(encabezado)

        for fila in datos_nuevos:
            escritor.writerow([fila.get(col, "") for col in encabezado])

def devolver_lista(archivo, carpeta_base=Path(RESULTADOS_PATH)):
    path_file = carpeta_base/f"{archivo}_unificado.csv"
    if(not path_file.exists()): #verifico si el archivo existe
        print(f"El archivo {path_file} no existe.")
        raise FileNotFoundError(f"No se encontró: {path_file}")
    with open(path_file, encoding="utf-8") as f:
        reader = list(csv.DictReader(f,delimiter=";"))
    return reader


