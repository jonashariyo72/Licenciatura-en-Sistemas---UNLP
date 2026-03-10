import string
from utils import get_ignorecase

def traducir_ch04(datos):
    for fila in datos:
        valor = fila.get("CH04")
        if valor == "1":
            fila["CH04_str"] = "Masculino"
        elif valor == "2":
            fila["CH04_str"] = "Femenino"
        else:
            fila["CH04_str"] = "Desconocido"
    return datos


def traducir_nivelED(datos):
    for fila in datos:
        valor = fila.get("NIVEL_ED")
        if valor == "1":
            fila["NIVEL_ED_str"] = "Primario incompleto"
        elif valor == "2":
            fila["NIVEL_ED_str"] = "Primario completo"
        elif valor == "3":
            fila["NIVEL_ED_str"] = "Secundario incompleto"
        elif valor == "4":
            fila["NIVEL_ED_str"] = "Secundario completo"
        elif valor in ("5", "6"):
            fila["NIVEL_ED_str"] = "Superior o universitario"
        elif valor in ("7", "9"):
            fila["NIVEL_ED_str"] = "Sin informacion"
    return datos



#modificacion de esto porque cuando se guardaba el csv final tiraba error
def traducir_condicion(datos):
    for fila in datos:
        estado = fila.get("ESTADO")
        cat_ocup = fila.get("CAT_OCUP")

        if estado == "1":
            if cat_ocup in ("1", "2"):
                fila["CONDICION_LABORAL"] = "Ocupado autónomo"
            elif cat_ocup in ("3", "4", "9"):
                fila["CONDICION_LABORAL"] = "Ocupado dependiente"
            else:
                fila["CONDICION_LABORAL"] = "Ocupado sin categoría"
        elif estado == "2":
            fila["CONDICION_LABORAL"] = "Desocupado"
        elif estado == "3":
            fila["CONDICION_LABORAL"] = "Inactivo"
        elif estado == "4":
            fila["CONDICION_LABORAL"] = "Fuera de categoría/sin información"
        else:
            fila["CONDICION_LABORAL"] = "No especificado"

    return datos


#modificacion de esto porque cuando se guardaba el csv final tiraba error
def universitario(datos):
    for fila in datos:
        try:
            edad = int(fila.get("CH06", 0))
            nivel = fila.get("CH12")
            finalizo = fila.get("CH13")

            if edad >= 18:
                if nivel in ("7", "8") and finalizo == "1":
                    fila["UNIVERSITARIO"] = 1  # Sí
                else:
                    fila["UNIVERSITARIO"] = 0  # No
            else:
                fila["UNIVERSITARIO"] = 2      # No aplica

        except:
            fila["UNIVERSITARIO"] = 2  # Fallback seguro

    return datos


# ACA SEMODIFICA EL HARDCODEO DEL ULTIMO TRIMESTRE, Q SOLO TOMABA EL 4TO, CUANDO POR AHI NO HAY 4TO TRIMESTRE
def pueden_leer(datos):
    detalle_por_anio = {}
    
    for fila in datos:
        anio = fila["ANO4"]
        trim = int(fila["TRIMESTRE"])
        edad = int(fila["CH06"])
        puede_leer = fila["CH09"]
        pondera = int(fila["PONDERA"])

        # SE INICIALIZA la estructura si no existe
        if anio not in detalle_por_anio:
            detalle_por_anio[anio] = {
                "ultimo_trimestre": trim,
                "data": {
                    trim: {
                        "total": 0,
                        "saben_leer": 0,
                        "nosaben_leer": 0
                    }
                }
            }
        else:
            # actualiza el ult trimestre si es mayor
            if trim > detalle_por_anio[anio]["ultimo_trimestre"]:
                detalle_por_anio[anio]["ultimo_trimestre"] = trim

            # si el trim no estaba registrado lo registra
            if trim not in detalle_por_anio[anio]["data"]:
                detalle_por_anio[anio]["data"][trim] = {
                    "total": 0,
                    "saben_leer": 0,
                    "nosaben_leer": 0
                }

        if edad > 6:
            anio_info = detalle_por_anio[anio]["data"][trim]
            anio_info["total"] += pondera  # ← ESTA LÍNEA ES CLAVE
            try:
                valor = int(float(puede_leer))
                if valor == 1:
                    anio_info["saben_leer"] += pondera
                elif valor == 2:
                    anio_info["nosaben_leer"] += pondera
            except:
                pass

    resultado = []
    # muestra los resultados solo del ult trim por anio
    for anio in sorted(detalle_por_anio):
        ultimo = detalle_por_anio[anio]["ultimo_trimestre"]
        datos_trim = detalle_por_anio[anio]["data"][ultimo]
        total = datos_trim["total"]
        saben = datos_trim["saben_leer"]
        nosaben = datos_trim["nosaben_leer"]

        resultado.append({
            "Año": anio,
            "Capaces de leer/escribir (%)": round((saben / total) * 100, 2) if total > 0 else None,
            "Incapaces de leer/escribir (%)": round((nosaben / total) * 100, 2) if total > 0 else None
        })

    return resultado


def extranjeros_universitarios(datos, anio, trim):
    total_no_nacidos = 0
    total_no_nacidos_univ = 0
    hay = False

    for fila in datos:
        pondera = int(fila.get("PONDERA"))
        valor2 = fila.get("CH12")    # nivel más alto cursado: 7 univer, 8 posgrado
        valor3 = fila.get("CH13")    # finalizó? 1: sí / 2: no / 3: ns/nc
        nacimiento = fila.get("CH15")  # 4 o 5: extranjero
        ano_encuesta = fila.get("ANO4")
        trimestre = get_ignorecase(fila, "TRIMESTRE")

        if anio == ano_encuesta and trim == trimestre:
            hay = True
            if nacimiento in ("4", "5"):
                total_no_nacidos += pondera
                if valor2 in ("7", "8") and valor3 == "1":
                    total_no_nacidos_univ += pondera

    if not hay:
        print("No hay datos para el trimestre seleccionado")

    if total_no_nacidos == 0:
        porcentaje = 0.0
    else:
        porcentaje = round((total_no_nacidos_univ / total_no_nacidos) * 100,2)

    return porcentaje


def menor_desocupacion(datos):  # toma a los que tienen 18 años o más
    detalles = {}

    for fila in datos:
        trim = get_ignorecase(fila, "TRIMESTRE")
        edad = int(fila.get("CH06"))
        ano_encuesta = fila.get("ANO4")
        estado = fila.get("ESTADO")
        pondera = int(fila.get("PONDERA"))

        if edad >= 18 and estado not in ("3", "4"):
            if ano_encuesta not in detalles:
                detalles[ano_encuesta] = {}
            if trim not in detalles[ano_encuesta]:
                detalles[ano_encuesta][trim] = {
                    "cant_total": 0,
                    "cant_ocupados": 0,
                    "cant_desocupados": 0,
                    "porcentaje_desocupados": 0.0,
                }

            detalles[ano_encuesta][trim]["cant_total"] += pondera

            if estado == "1":
                detalles[ano_encuesta][trim]["cant_ocupados"] += pondera
            elif estado == "2":
                detalles[ano_encuesta][trim]["cant_desocupados"] += pondera

    # aca busco el menor porcentaje
    menor_porcentaje = 100.0
    menor_anio = None
    menor_trim = None

    for anio in detalles:
        for trim in detalles[anio]:
            desocup = detalles[anio][trim]["cant_desocupados"]
            total = detalles[anio][trim]["cant_total"]

            if total > 0:
                porcentaje = round((desocup / total) * 100, 2)
                detalles[anio][trim]["porcentaje_desocupados"] = porcentaje

                if porcentaje < menor_porcentaje:
                    menor_porcentaje = porcentaje
                    menor_anio = anio
                    menor_trim = trim

    if menor_anio and menor_trim:
        print(
            f"El año {menor_anio} y el trimestre {menor_trim} "
            f"tuvieron el menor porcentaje de desocupación: {menor_porcentaje}%"
        )


def ranking_aglomerados_estudios(datos):
    try:
        fechas = set()  # creo un conjunto vacio para ir agregando las fechas asi identifico la ultima y no agrega repetidas
        for fila in datos:
            fechas.add((int(fila["ANO4"]), int(get_ignorecase(fila, "TRIMESTRE"))))  # agrego tuplas con el anio y el mes !!!!!!!!!!!!!!!!!!!
        fechas_ordenadas = sorted(fechas)
        ultimas_dos = fechas_ordenadas[-2:]  # empiezo del anteultimo y me voy al ultimo - me quedo con las mas nuevas

        datos_filtrados = []  # creo una lista vacia para agregar ahora los datos ya filtrados con los q voy a trabajar (de los ultimos dos anios)

        for fila in datos:
            anio = int(fila["ANO4"])
            trimestre = int(get_ignorecase(fila, "TRIMESTRE"))  # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!
            if (anio, trimestre) in ultimas_dos:
                datos_filtrados.append(fila)  # voy agregando las filas del archivo q voy a recorrer, que me interesan

        # aca empiezo a agrupar a las personas por hogar
        hogares = {}
        for fila in datos_filtrados:
            try:
                pondera = int(fila.get("PONDERA"))
                id_hogar = (fila.get("CODUSU"), fila.get("NRO_HOGAR"))
                aglomerado = fila.get("AGLOMERADO")
                universitario = fila.get("UNIVERSITARIO")

                if id_hogar not in hogares:  # si no cargue este hogar en mi dict de hogares
                    hogares[id_hogar] = {
                        "universitario": 0,
                        "aglomerado": aglomerado
                    }

                if int(float(universitario)) == 1:
                    hogares[id_hogar]["universitario"] += pondera
            except Exception as e:
                print(f"Error procesando fila {fila}: {e}")
                continue

        # ahora creo un dict de los aglomerados
        aglomerados = {}
        for hogar in hogares.values():  # me quedo con los valores del dict values pq ya no me interesa las keys - que seria el id_hogar
            aglo = hogar["aglomerado"]
            if aglo not in aglomerados:
                aglomerados[aglo] = {
                    "total_hogares": 0,
                    "con2_o_mas_univ": 0,
                }

            aglomerados[aglo]["total_hogares"] += 1
            if hogar["universitario"] >= 2:
                aglomerados[aglo]["con2_o_mas_univ"] += 1

        # por ultimo hago una lista con tuplas de cada aglomerado con su porcentaje para dps ordenar y sacar a las primeras 5
        ranking = []
        for aglo in aglomerados:
            tot_hogares = aglomerados[aglo]["total_hogares"]
            con_2 = aglomerados[aglo]["con2_o_mas_univ"]
            if tot_hogares > 0:
                porcentaje = round((con_2 / tot_hogares) * 100, 2)
            else:
                porcentaje = 0.0
            ranking.append((aglo, porcentaje))

        # ordeno esa lista con los aglomerados y sus porcentajes, teniendo en cuenta el porcentaje, y de mayor a menor
        ranking_ordenado = sorted(ranking, key=lambda x: x[1], reverse=True)

        print("Top 5 aglomerados con mayor % de hogares con 2+ universitarios (ponderados):")
        for aglo, porcentaje in ranking_ordenado[:5]:  # imprimo de 0 a 4 pos
            print(f" Aglomerado {aglo}: {porcentaje}%")


        return ranking_ordenado[:5]

    except Exception as error:
        print(f"ERROR en ranking_aglomerados_estudios: {error}")
        return []




def tabla_nivel_estudios (datos, aglo):
    tabla = {}
    for fila in datos:
        edad = int(fila.get("CH06"))
        aglomerado = int(fila.get("AGLOMERADO"))
        trim = int(get_ignorecase(fila, "TRIMESTRE"))
        pondera = int(fila.get("PONDERA"))
        nivel_ed = fila.get("NIVEL_ED_str")
        anio = int(fila.get("ANO4"))
        if (edad >= 18 and aglomerado == int(aglo) and nivel_ed != "Sin informacion"): # filtro por los de 18 o + , que esten en el aglomerado que pasan x parametro y que no esten englobados en sin informacion
            clave = (anio, trim) # creo una variable clave con la tupla anio y trim para podr buscar si esta en mi dict o  no
            if clave not in tabla: # si no figura el anio y el trim en el dict, q lo cree con valores 0
                tabla[clave] = {
                    "Primario incompleto": 0,
                    "Primario completo": 0,
                    "Secundario incompleto": 0,
                    "Secundario completo": 0,
                    "Superior o universitario": 0
                }
            tabla[clave][nivel_ed] += pondera
    
    # esto hace que si no se encontro el aglomerado (y por eso no se creo la tabla), que tire que no se encontro
    if not tabla:
        print(f"No se encontraron datos para el aglomerado {aglo}.")
        return None

    # defino una lista con los niveles para poder imprimir en el encabezado
    niveles = ["Primario incompleto", "Primario completo",
            "Secundario incompleto", "Secundario completo",
            "Superior o universitario"]

    # aca imprimo el encabezado. Lo q hace el join es unir a toods con un espacio. pq si no me los imprime uno debajo del otro y yo quiero q esten todos en la misma linea
    print(f"{'Año':<6} {'Trim':<6} " + " ".join(f"{nivel:<25}" for nivel in niveles))
    for (anio, trim) in sorted(tabla): # aca imprimo ordenado
        fila = f"{anio:<6} {trim:<6} "
        for nivel in niveles:
            valor = tabla[(anio, trim)][nivel]
            fila += f"{valor:<26}"
        print(fila)     
            
        
def tabla_comparar_aglomerados(datos, aglo1, aglo2):
    aglo1 = int(aglo1)
    aglo2 = int(aglo2)
    tabla = {} # creo un dict vacio para ir cargandolo

    for fila in datos:
        edad = int(fila.get("CH06"))
        aglo = int(fila.get("AGLOMERADO"))
        nivel = fila.get("NIVEL_ED_str")
        pondera = int(fila.get("PONDERA"))
        anio = int(fila.get("ANO4"))
        trim = int(get_ignorecase(fila, "TRIMESTRE"))

        if edad >= 18 and aglo in (aglo1, aglo2):
                clave = (anio, trim) # creo una tupla con el anio y el trimestre para ver si ya lo habia cargado o si no estaba, hago uno nuevo
                if clave not in tabla:
                    tabla[clave] = {
                        aglo1: {"total": 0, "sec_incompleto": 0},
                        aglo2: {"total": 0, "sec_incompleto": 0}
                    }

                tabla[clave][aglo]["total"] += pondera
                if nivel == "Secundario incompleto":
                    tabla[clave][aglo]["sec_incompleto"] += pondera

    # con esto verifico q ingrese un nro de aglomerado valido, si no, salta este msj
    if not (2 <= int(aglo1) <= 93) or not (2 <= int(aglo2) <= 93):
        print("Uno o ambos aglomerados no existen (deben estar entre 2 y 93).")
        return         

# imprimo el ncabezado
    print(f"{'Año':<6} {'Trimestre':<6} {f'Aglomerado {aglo1}':<18} {f'Aglomerado {aglo2}':<18}") 
    
    # cuerpo ordenado
    for (anio, trim) in sorted(tabla):
        datos_aglo1 = tabla[(anio, trim)][aglo1]
        datos_aglo2 = tabla[(anio, trim)][aglo2]
        
        # el else ultimo hace q no de error si total es 0
        porcentaje1 = round((datos_aglo1["sec_incompleto"] / datos_aglo1["total"]) * 100, 2) if datos_aglo1["total"] else 0
        porcentaje2 = round((datos_aglo2["sec_incompleto"] / datos_aglo2["total"]) * 100, 2) if datos_aglo2["total"] else 0
        
        print(f"{anio:<6} {trim:<9} {str(porcentaje1)+'%':<18} {str(porcentaje2)+'%':<18}")

#ESTOS SON PARA HACER EL PUNTO 12 Y EL 13



def verificar_trimestres_compatibles(individuos, hogares):
    trimestres_indiv = {
        (i["ANO4"], get_ignorecase(i, "TRIMESTRE")) for i in individuos
    }
    trimestres_hogar = {
        (h["ANO4"], get_ignorecase(h, "TRIMESTRE")) for h in hogares
    }

    comunes = trimestres_indiv & trimestres_hogar
    if not comunes:
        print("No hay trimestres en común entre individuos y hogares.")
        print(f"Individuos: {trimestres_indiv}")
        print(f"Hogares: {trimestres_hogar}")
        return False
    return True



def unir_individuos_y_hogares(individuos, hogares):
    hogares_dict = {}
    for h in hogares:
        clave = (h['CODUSU'], h['NRO_HOGAR'], h['ANO4'], h['TRIMESTRE'])
        hogares_dict[clave] = h

    datos_combinados = []
    for persona in individuos:
        clave = (persona['CODUSU'], persona['NRO_HOGAR'], persona['ANO4'], persona['TRIMESTRE'])
        hogar = hogares_dict.get(clave)
        if hogar: # si se encontro un hogar con esa clave
            persona['CONDICION_DE_HABITABILIDAD'] = hogar.get('CONDICION_DE_HABITABILIDAD', "") # le sumo lo de hogares a personas
            persona['AGLOMERADO'] = hogar.get('AGLOMERADO', "")
            datos_combinados.append(persona) # y agrego esa persona a mi lista de datos combinados

    return datos_combinados


def detectar_ultimo_trimestre(datos):
    trimestres = set() # ahgo un set/conjunto para q no se repitan los anios ni los trim
    for fila in datos:
        anio = int(fila["ANO4"])
        trim = int(get_ignorecase(fila, "TRIMESTRE"))
        trimestres.add((anio, trim))
    if trimestres: # si el conjunto tiene algo
        return max(trimestres)
    else:
        return None


### se modifico usando pondra!!!
def porcentaje_jubilados_insuficiente(datos):
    anio, trim = detectar_ultimo_trimestre(datos)

    datos_filtrados = []
    for fila in datos:
        if fila["ANO4"] == str(anio) and fila["TRIMESTRE"] == str(trim):
            datos_filtrados.append(fila)
            
    total_jubilados = {}
    jubilados_insuficientes = {}

    for fila in datos_filtrados:
        pondera = int(fila.get("PONDERA"))
        if fila['CAT_INAC'] == '1':  # Jubilado
            aglomerado = fila['AGLOMERADO']
            if aglomerado not in total_jubilados:
                total_jubilados[aglomerado] = 0
                jubilados_insuficientes[aglomerado] = 0

            total_jubilados[aglomerado] += pondera

            if fila['CONDICION_DE_HABITABILIDAD'] == 'insuficiente':
                jubilados_insuficientes[aglomerado] += pondera

    resultados = []  # genero una lista con los aglomerados y los porcentajes
    for aglomerado in total_jubilados:
        total = total_jubilados[aglomerado]
        insuf = jubilados_insuficientes.get(aglomerado, 0)
        porcentaje = round((insuf / total) * 100 , 2)  if total > 0 else 0
        resultados.append((aglomerado, porcentaje))

    resultados_ordeandos = sorted (resultados, key=lambda x: int(x[0]))

    for aglomerado, porcentaje in resultados_ordeandos:
        print(f"Aglomerado {aglomerado}: {porcentaje}% de jubilados en viviendas con habitabilidad insuficiente")
        

def cant_individuos_uni_insuficiente (datos):
    año = input("Ingrese el año: ")
    ultimo_trimestre = 0
    for fila in datos: # Detectar el último trimestre disponible para ese año

        if fila['ANO4'] == año:
            ultimo_trimestre = max(ultimo_trimestre, int(get_ignorecase(fila, "TRIMESTRE")))

    niveles_superiores = {'5', '6'}
    contador = 0
    for fila in datos: # Contar personas que cumplan ambas condiciones
        if fila['ANO4'] == año and int(fila['TRIMESTRE']) == ultimo_trimestre:
            if fila['NIVEL_ED'] in niveles_superiores and fila['CONDICION_DE_HABITABILIDAD'] == 'insuficiente':
                pondera = int(fila.get("PONDERA"))
                contador += pondera

    print(f"Cantidad de personas con nivel universitario o superior en viviendas con condición insuficiente: {contador}")


def porcentajes_universitarios(datos):
        aglomerados = {}
        universitarios_por_aglomerado = {}
    

        for fila in datos:
            aglo = fila.get("AGLOMERADO")
            nivel = fila.get("CH12")
            if aglo:
                pondera = int(fila.get("PONDERA"))
                if aglo not in aglomerados:
                    aglomerados[aglo] = 0
                aglomerados[aglo] += pondera

                if nivel in ("7", "8"):  
                    if aglo not in universitarios_por_aglomerado:
                        universitarios_por_aglomerado[aglo] = 0
                    universitarios_por_aglomerado[aglo] += pondera

        porcentajes = {}
        for aglo in aglomerados:
            total = aglomerados[aglo]
            universitarios = universitarios_por_aglomerado.get(aglo, 0)
            porcentaje = (universitarios / total) * 100
            porcentajes[aglo] = porcentaje
    

        porcentajes_ordenados = sorted(porcentajes.items(), key=lambda x: int(x[0]))

        print ("El porcentaje de personas por aglomerado que hayan cursado al menos en nivel universitario o superior")
        for a, p in porcentajes_ordenados:
            print (f"AGLOMERADO:  {a}, PORCENTAJE:  {p:.2f}%")
