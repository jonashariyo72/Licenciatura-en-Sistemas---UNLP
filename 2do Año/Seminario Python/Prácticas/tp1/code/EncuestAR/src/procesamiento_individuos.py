import string

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
            fila["NIVEL_ED_str"] = "Secundario completo"
        elif valor in ("5", "6"):
            fila["NIVEL_ED_str"] = "Superior o universitario"
        elif valor in ("7", "9"):
            fila["NIVEL_ED_str"] = "Sin informacion"
    return datos


def traducir_condicion(datos):
    for fila in datos:
        valor = fila.get("ESTADO")
        valor2 = fila.get("CAT_OCUP")
        if valor == "1" and valor2 in ("1", "2"):
            fila["CONDICION_LABORAL"] = "Ocupado autónomo"
        if valor == "1" and valor2 in ("3", "4", "9"):
            fila["CONDICION_LABORAL"] = "Ocupado dependiente"
        if valor == "2":
            fila["CONDICION_LABORAL"] = "Desocupado"
        if valor == "3":
            fila["CONDICION_LABORAL"] = "Inactivo"
        if valor == "4":
            fila["CONDICION_LABORAL"] = "Fuera de categoría/sin información"
    return datos


def universitario(datos):  # nivel mínimo universitario
    for fila in datos:
        valor = int(fila.get("CH06"))   # años cumplidos
        valor2 = fila.get("CH12")  # nivel más alto cursado (7 universitario, 8 posgrado)
        valor3 = fila.get("CH13")  # finalizó el nivel? 1: sí / 2: no / 3: ns/nc
        if valor >= 18 and valor2 in ("7", "8") and valor3 == "1":
            fila["UNIVERSITARIO"] = "1" # si
        elif valor >= 18 and valor2 not in ("7", "8"):
            fila["UNIVERSITARIO"] = "0" # no
        elif valor < 18:
            fila["UNIVERSITARIO"] = "2" # no aplica
    return datos


def pueden_leer(datos):
    detalle_por_anio = {}
    encontro_trimestre = False

    for fila in datos:
        trim = fila.get("TRIMESTRE")
        edad = int(fila.get("CH06"))
        puede_leer = fila.get("CH09")  # 1: sí / 2: no / 3: menor de 2 años
        ano_encuesta = fila.get("ANO4")
        pondera = int(fila.get("PONDERA"))

        if trim == "4" and edad > 6:
            encontro_trimestre = True
            if ano_encuesta not in detalle_por_anio:
                detalle_por_anio[ano_encuesta] = {
                    "total": 0,
                    "saben_leer": 0,
                    "nosaben_leer": 0,
                }
            detalle_por_anio[ano_encuesta]["total"] += pondera
            if puede_leer == "1":
                detalle_por_anio[ano_encuesta]["saben_leer"] += pondera
            elif puede_leer == "2":
                detalle_por_anio[ano_encuesta]["nosaben_leer"] += pondera

    if not encontro_trimestre:
        print("No se cargaron archivos del cuarto trimestre de ningun anio")

    return detalle_por_anio


def extranjeros_universitarios(datos, anio, trim):
    total_no_nacidos = 0
    total_no_nacidos_univ = 0
    hay = False

    for fila in datos:
        pondera = int(fila.get("PONDERA"))
        valor2 = fila.get("CH12")    # nivel más alto cursado: 7 univer, 8 posgrado
        valor3 = fila.get("CH13")    # finalizó? 1: sí / 2: no / 3: ns/nc
        nacimiento = fila.get("CH15")  # 4 o 5: extranjero
        ano_encuesta = int(fila.get("ANO4"))
        trimestre = int(fila.get("TRIMESTRE"))

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
        porcentaje = total_no_nacidos_univ / total_no_nacidos * 100

    return porcentaje


def menor_desocupacion(datos):  # toma a los que tienen 18 años o más
    detalles = {}

    for fila in datos:
        trim = fila.get("TRIMESTRE")
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
                porcentaje = round((desocup / total) * 100, 1)
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


def ranking_aglomerados_estudios (datos):
    fechas = set() # creo un conjunto vacio para ir agregando las fechas asi identifico la ultima y no agrega repetidas
    for fila in datos:
        fechas.add((int(fila["ANO4"]), int(fila["TRIMESTRE"]))) # agrego tuplas con el anio y el mes
    fechas_ordenadas = sorted(fechas)
    ultimas_dos = fechas_ordenadas[-2:] # empiezo del anteultimo y me voy al ultimo - me quedo con las mas nuevas
   
    datos_filtrados = [] # creo una lista vacia para agregar ahora los datos ya filtrados con los q voy a trabajar (de los ultimos dos anios)

    for fila in datos:
        anio = int(fila["ANO4"])
        trimestre = int(fila["TRIMESTRE"])
        if (anio,trimestre) in ultimas_dos:
            datos_filtrados.append(fila) # voy agregando las filas del archivo q voy a recorrer, que me interesan
    
    #aca empiezo a agrupar a las personas por hogar
    hogares = {}
    for fila in datos_filtrados:
        pondera = int(fila.get("PONDERA"))
        id_hogar = (fila.get("CODUSU"), fila.get("NRO_HOGAR"))
        aglomerado = fila.get("AGLOMERADO")
        universitario = fila.get("UNIVERSITARIO")

        if id_hogar not in hogares: # si no cargue este hogar en mi dict de hogares
            hogares[id_hogar] = {
                "universitario" : 0,
                "aglomerado" : aglomerado
            }
        
        if universitario == "1":
            hogares[id_hogar]["universitario"] += pondera

    #ahora creo un dict de los aglomerados
    aglomerados = {}
    for hogar in hogares.values(): # me quedo con los valores del dict values pq ya no me interesa las keys - que seria el id_hogar
        aglo = hogar["aglomerado"]
        if aglo not in aglomerados:
            aglomerados[aglo] = {
                "total_hogares" : 0,
                "con2_o_mas_univ" : 0,
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
            porcentaje = round((con_2/tot_hogares) * 100)
        else:
            porcentaje = 0.0
        ranking.append((aglo,porcentaje))

    
    # ordeno esa lista con los aglomerados y sus porcentajes, teniendo en cuenta el porcentaje, y de mayor a menor
    ranking_ordenado = sorted(ranking, key= lambda x: x[1], reverse = True)

    print("Top 5 aglomerados con mayor % de hogares con 2+ universitarios (ponderados):")
    for aglo, porcentaje in ranking_ordenado[:5]:   # imprimo de 0 a 4 pos
        print(f" Aglomerado {aglo}: {porcentaje}%")
    
    def porcentaje_universitarios(datos):
        aglomerados = {}
        universitarios_por_aglomerado = {}
    

        for fila in datos:
            aglo = fila.get("AGLOMERADO")
            nivel = fila.get("CH12")
            if aglo:
                if aglo not in aglomerados:
                    aglomerados[aglo] = 0
                aglomerados[aglo] += 1 

                if nivel in ("7", "8"):  
                    if aglo not in universitarios_por_aglomerado:
                        universitarios_por_aglomerado[aglo] = 0
                    universitarios_por_aglomerado[aglo] += 1

        porcentajes = {}
        for aglo in aglomerados:
            total = aglomerados[aglo]
            universitarios = universitarios_por_aglomerado.get(aglo, 0)
            porcentaje = (universitarios / total) * 100
            porcentajes[aglo] = porcentaje
    

        porcentajes_ordenados = sorted(porcentajes.items(), key=lambda x: int(x[0]))



        print ("El porcentaje de personas por aglomerado que hayan cursado al menos en nivel universitario o superior")
        for a, p in porcentajes_ordenados:
            print (f"AGLOMERADO:  {a}, PORCENTAJE:  {p:.2f}%")






        




    
    
