import csv
from pathlib import Path

def cargar_archivos(tipo=None, data_path=Path("data")):
    
    if tipo not in ("individual", "hogar"):
        print("El archivo recibido no es válido")
        raise ValueError
    
    if not data_path.exists() or not data_path.is_dir(): #verifica si no existe el path o el path no es un directorio
        print(f"El path {data_path} no existe o no es un directorio válido.")
        raise FileNotFoundError

    # patron  general
    patron = f"usu_{tipo}_*.txt"
    archivos = list(data_path.glob(patron))

    # agrega excepciones de nombres q no siguen el patron normal
    if tipo == "individual":
        archivos += list(data_path.glob("EPH_usu_personas_*.txt"))
    elif tipo == "hogar":
        archivos += list(data_path.glob("EPH_usu_4to_*.txt"))

    if not archivos:
        print(f"no se encontraron archivos con patron {patron} en {data_path}")
        raise FileNotFoundError  # con esto se corta la ejecucion del programa si no encuentra nada

    datos = []
    for archivo in archivos:
        with open(archivo, encoding="utf-8") as f:
            lector = csv.reader(f, delimiter=";")
            encabezado = next(lector)
            for fila in lector:
                if len(fila) == len(encabezado):
                    datos.append(dict(zip(encabezado, fila)))

    return datos


def guardar_csv_basico(datos, salida_path):
    salida_path = Path(salida_path)
    salida_path.parent.mkdir(parents=True, exist_ok=True)  # Asegura que la carpeta exista
    """
    Guarda los datoscomo una lista de diccionarios en un csv y si no exite la carpeta la crea
    """
    salida_path = Path(salida_path)
    
    if not datos:
        print(" No hay datos para guardar.")
        return

    encabezado = list(datos[0].keys())
    with open(salida_path, mode="w", newline="", encoding="utf-8") as archivo:
        escritor = csv.writer(archivo, delimiter=";")
        escritor.writerow(encabezado)
        for fila in datos:
            escritor.writerow([fila[col] for col in encabezado])
            escritor.writerow([fila[col] for col in encabezado])
            
import os


def devolver_lista(archivo, carpeta_base=Path("../resultados")):
    path_file = carpeta_base/f"{archivo}_unificado.csv"
    if(not path_file.exists()): #verifico si el archivo existe
        print(f"El archivo {path_file} no existe.")
        raise FileNotFoundError(f"No se encontró: {path_file}")
    with open(path_file, encoding="utf-8") as f:
        reader = list(csv.DictReader(f,delimiter=";"))
    return reader
