def tipo_hogar (datos):
    for fila in datos:
        valor = fila.get ("IX_TOT")
        if valor == '1':
            fila ["TIPO_HOGAR"] = "Unipersonal"
        elif valor in ('2' , '3' , '4'):
            fila ["TIPO_HOGAR"] = "Nuclear"
        else:
            fila ["TIPO_HOGAR"] = "Extendido"
    return (datos)


## modificada pq habian valores q eran cero y se rompia todo
def densidad_hogar(datos):
    for data in datos:
        try:
            total = int(data.get('IX_TOT', ''))
            cuartos = int(data.get('IV2', ''))
            if cuartos == 0:
                raise ZeroDivisionError
            densidad = total / cuartos

            if densidad < 1:
                data["DENSIDAD_HOGAR"] = "Bajo"
            elif densidad <= 2:
                data["DENSIDAD_HOGAR"] = "Medio"
            else:
                data["DENSIDAD_HOGAR"] = "Alto"
        except:
            data["DENSIDAD_HOGAR"] = ""  # celda vacía

    return datos



def material_techumbre (datos):
    for data in datos:
        match int(data['V4']):
            case 1|2|3|4:
                data['MATERIAL_TECHUMBRE']='Material durable'
            case 5|6|7:
                data['MATERIAL_TECHUMBRE']= 'Material precario'
            case 9:
                data['MATERIAL_TECHUMBRE']= 'No aplica'
    return datos
                
                
def clasificar_vivienda(datos):
    for data in datos:
        try:
            agua = int(data['IV6'])
            donde = int(data['IV7'])
            red = int(data['IV8'])
            banio = int(data['IV10'])
            ubicacion = int(data['IV11'])
        except (ValueError, KeyError):
            # Si falta algun dato o esta mal formateado, se asume insuficiente pq hay filas q no tienen nada, entonces nos tiraba error
            data['CONDICION_DE_HABITABILIDAD'] = 'insuficiente'
            continue

        if agua == 1 and donde == 1 and red == 1 and banio == 1 and ubicacion == 1:
            data['CONDICION_DE_HABITABILIDAD'] = 'buena'
        elif agua in [1, 2] and donde == 1 and red == 1 and banio in [1, 2] and ubicacion in [1, 2]:
            data['CONDICION_DE_HABITABILIDAD'] = 'saludables'
        elif agua in [1, 2] and donde in [1, 2] and red == 1 and banio in [1, 2] and ubicacion in [1, 2, 3]:
            data['CONDICION_DE_HABITABILIDAD'] = 'regular'
        else:
            data['CONDICION_DE_HABITABILIDAD'] = 'insuficiente'
    return datos


 ## aca se modifica usando el pondera!!!!   

def inquilinos_por_region (datos):
        regiones = {}

        for fila in datos:
            nombre_region = fila.get("REGION")
            tenencia = fila.get("II7")
            pondera = int(fila.get("PONDERA"))


            if nombre_region not in regiones:
                regiones[nombre_region] = {'total': 0, 'inquilinos': 0}

            regiones[nombre_region]['total'] += pondera
            if tenencia in ("3"):
                regiones[nombre_region]['inquilinos'] += pondera
        
            porcentajes = []
        for region, datos_region in regiones.items():
            total = datos_region['total']
            inquilinos = datos_region['inquilinos']
            porcentaje = (inquilinos / total) * 100 if total > 0 else 0
            porcentajes.append((region, porcentaje))

    
        porcentajes.sort(key=lambda x: x[1], reverse=True)

        for region, porcentaje in porcentajes:
            print(f"REGION CON CODIGO: {region} | {porcentaje:.2f}% inquilinos")


#modificado agregando pondera !!!!!
def porcentaje_viviendas_aglomerado (datos):
    hogares = {}
    for fila in datos:
        id_hogar = (fila.get("CODUSU"), fila.get("NRO_HOGAR"))
        if id_hogar not in hogares:
            hogares[id_hogar] = {
                "aglomerado": fila.get("AGLOMERADO"),
                "tenencia": fila.get("II7"), #corregida la variable
                "pondera": int(fila.get("PONDERA"))
            }

    aglomerados = {}
    for hogar in hogares.values():
        aglo = hogar["aglomerado"]
        tenencia = hogar["tenencia"]
        pondera = hogar["pondera"]
        if aglo not in aglomerados:
            aglomerados[aglo] = {
                "total": 0,
                "propias": 0
            }
        aglomerados[aglo]["total"] += pondera
        if tenencia == "1" or tenencia == "2":  # “1” indica propietario de la vivienda y el terreno y "2" Propietario de la vivienda solamente
            aglomerados[aglo]["propias"] += pondera
            

    print("Porcentaje de viviendas ocupadas por propietarios por aglomerado:")
    for aglo in sorted(aglomerados, key=lambda x: int(x)): # las ordeno con el sorted
        total = aglomerados[aglo]["total"]
        propias = aglomerados[aglo]["propias"]
        porcentaje = (propias / total) * 100 if total else 0
        print(f"Aglomerado {aglo}: {porcentaje:.2f}%") #acá imprimo el porcentaje de cada aglomerado con solo 2 decimales.


# se arreglo lo del pondera aca!!!
def aglomerado_mas_sin_baño(datos):
    # Paso 1: contar personas por hogar
    personas_por_hogar = {}
    info_hogar = {}
    for fila in datos:
        id_hogar = (fila["CODUSU"], fila["NRO_HOGAR"])
        personas_por_hogar[id_hogar] = personas_por_hogar.get(id_hogar, 0) + 1
        if id_hogar not in info_hogar:
            info_hogar[id_hogar] = {
                "aglomerado": fila["AGLOMERADO"],
                "bano": fila["IV8"], # tmb corregida
                "pondera": int(fila.get("PONDERA"))
            }

    # Paso 2: filtrar hogares con >2 personas y sin baño
    conteo_por_aglomerado = {}
    for hogar, cantidad in personas_por_hogar.items():
        if cantidad > 2:
            pondera = info_hogar[hogar]["pondera"]
            bano = info_hogar[hogar]["bano"]
            if bano == "0" or bano == "2":  # ajustar según codificación real
                aglo = info_hogar[hogar]["aglomerado"]
                conteo_por_aglomerado[aglo] = conteo_por_aglomerado.get(aglo, 0) + pondera

    # Paso 3: encontrar el aglomerado con mayor cantidad
    if conteo_por_aglomerado:
        aglo_max = max(conteo_por_aglomerado, key=conteo_por_aglomerado.get)
        cantidad = conteo_por_aglomerado[aglo_max]
        print(f"Aglomerado con más viviendas con >2 ocupantes y sin baño: {aglo_max}")
        print(f"Cantidad de viviendas: {cantidad}")
    else:
        print("No se encontraron viviendas con más de 2 ocupantes y sin baño.")



# corregido con pondera y para q tome el valor de la col material_techumbre
def buscar_aglomerados_material_precario(datos):
    """Solicita un año al usuario y encuentra el ultimo trimestre con el mayor y menor porcentaje de viviendas precarias."""

    # Pide el año al usuario y verificar que sea valido
    anio = input("Ingrese el año: ")
    if not anio.isdigit():
        print("Número inválido.")
        return
    anio = int(anio)

    # Filtra registros por el año
    registros_anio = [fila for fila in datos if fila.get("ANO4") == str(anio)]
    if not registros_anio:
        print(f"No se encontraron registros para el año {anio}.")
        return

    # Encuentra el ult trimestre
    ultimo_trimestre = max(int(fila["TRIMESTRE"]) for fila in registros_anio if fila.get("TRIMESTRE", "").isdigit())

    # Filtra registros del ult trimestre
    registros_trimestre = [fila for fila in registros_anio if int(fila["TRIMESTRE"]) == ultimo_trimestre]

    # inicializa diccionarios para ponderaciones
    ponderado_total = {}
    ponderado_precarias = {}

    for fila in registros_trimestre:
        aglomerado = fila.get("AGLOMERADO")
        tipo_techo = fila.get("MATERIAL_TECHUMBRE")
        pondera = int(fila.get("PONDERA", 0))

        if not aglomerado or not tipo_techo:
            continue  # saltear si faltan datos

        # cuenta como precaria si la columna material_techumbre dice precario
        if tipo_techo == "Material precario":
            ponderado_precarias[aglomerado] = ponderado_precarias.get(aglomerado, 0) + pondera

        # acumula el total
        ponderado_total[aglomerado] = ponderado_total.get(aglomerado, 0) + pondera


    # Calcula el porcentaje de viviendas precarias
    porcentajes = {
        aglo: (ponderado_precarias.get(aglo, 0) / ponderado_total[aglo]) * 100
        for aglo in ponderado_total
    }

    # Encuentra el aglomerado con el mayor y menor porcentaje
    aglomerado_max = max(porcentajes, key=porcentajes.get)
    aglomerado_min = min(porcentajes, key=porcentajes.get)

    # muestra los rdos
    print(f"Aglomerado con mayor porcentaje de viviendas precarias: {aglomerado_max} ({porcentajes[aglomerado_max]:.2f}%)")
    print(f"Aglomerado con menor porcentaje de viviendas precarias: {aglomerado_min} ({porcentajes[aglomerado_min]:.2f}%)")




def buscar_aglomerados_material_precario(datos):
    """Solicita un año al usuario y encuentra el último trimestre con el mayor y menor porcentaje de viviendas precarias."""

    # Pedir el año al usuario y verificar que sea válido
    anio = input("Ingrese el año: ")
    if not anio.isdigit():
        print("Número inválido.")
        return
    anio = int(anio)

    # Filtrar registros por el año
    registros_anio = [fila for fila in datos if fila["ANO4"] == str(anio)]
    if not registros_anio:
        print(f"No se encontraron registros para el año {anio}.")
        return

    # Encontrar el último trimestre
    ultimo_trimestre = max(int(fila["TRIMESTRE"]) for fila in registros_anio)

    # Filtrar registros del último trimestre
    registros_trimestre = [fila for fila in registros_anio if int(fila["TRIMESTRE"]) == ultimo_trimestre]

    # Inicializar diccionarios para ponderaciones
    ponderado_total = {}
    ponderado_precarias = {}

    for fila in registros_trimestre:
        aglomerado = fila["AGLOMERADO"]
        v4 = int(fila["V4"])
        es_precario = v4 in {5, 6, 7}  # Material precario
        peso = int(fila["PONDERA"])

        # Acumular ponderaciones
        ponderado_total[aglomerado] = ponderado_total.get(aglomerado, 0) + peso
        if es_precario:
            ponderado_precarias[aglomerado] = ponderado_precarias.get(aglomerado, 0) + peso

    # Calcular porcentajes de viviendas precarias
    porcentajes = {aglo: (ponderado_precarias.get(aglo, 0) / ponderado_total[aglo]) * 100
                   for aglo in ponderado_total}

    # Encontrar el aglomerado con el mayor y menor porcentaje
    aglomerado_max = max(porcentajes, key=porcentajes.get)
    aglomerado_min = min(porcentajes, key=porcentajes.get)

    # Mostrar resultados
    print(f"Aglomerado con mayor porcentaje de viviendas precarias: {aglomerado_max} ({porcentajes[aglomerado_max]:.2f}%)")
    print(f"Aglomerado con menor porcentaje de viviendas precarias: {aglomerado_min} ({porcentajes[aglomerado_min]:.2f}%)")

    print(f"Se analizaron {len(registros_trimestre)} registros del año {anio}, trimestre {ultimo_trimestre}")
