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

def densidad_hogar (datos):
    for data in datos:
        if ((int(data['IX_TOT']) / int(data ['IV2'])) < 1):
            data ["DENSIDAD_HOGAR"] = "Bajo"
        elif (((int(data['IX_TOT']) / int(data ['IV2'])) >= 1) and ((int(data['IX_TOT']) / int(data ['IV2'])) <= 2)):
            data ["DENSIDAD_HOGAR"] = "Medio"
        else:
            data ["DENSIDAD_HOGAR"] = "Alto"
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
                
                
def clasificar_vivienda(datos):
    for data in datos:
        A = int(data['IV6'])
        B = int(data['IV7'])
        C = int(data['IV8'])
        D = int(data['IV10'])
        E = int(data['IV11'])

        if A == 1 and B == 1 and C == 1 and D == 1 and E == 1:
            data['CONDICION_DE_HABITABILIDAD'] = 'buena'
        elif A in [1, 2] and B == 1 and C == 1 and D in [1, 2] and E in [1, 2]:
            data['CONDICION_DE_HABITABILIDAD'] = 'saludables'
        elif A in [1, 2] and B in [1, 2] and C == 1 and D in [1, 2] and E in [1, 2, 3]:
            data['CONDICION_DE_HABITABILIDAD'] = 'regular'
        else:
            data['CONDICION_DE_HABITABILIDAD'] = 'insuficiente'
    return datos

def inquilinos_por_region (datos):
        regiones = {}

        for fila in datos:
            nombre_region = fila.get("REGION")
            tenencia = fila.get("II7")

            if nombre_region not in regiones:
                regiones[nombre_region] = {'total': 0, 'inquilinos': 0}

            regiones[nombre_region]['total'] += 1
            if tenencia in ("3"):
                regiones[nombre_region]['inquilinos'] += 1
        
            porcentajes = []
        for region, datos_region in regiones.items():
            total = datos_region['total']
            inquilinos = datos_region['inquilinos']
            porcentaje = (inquilinos / total) * 100 if total > 0 else 0
            porcentajes.append((region, porcentaje))

    
        porcentajes.sort(key=lambda x: x[1], reverse=True)

        print ("CÓDIGOS DE REGIONES: ")
        print ("01 = Gran Buenos Aires -- 40 = Noroeste -- 41 = Noreste -- 42 = Cuyo -- 43 = Pampeana -- 44 = Patagonia")
        print ("---------------------------------------------------------------------------------------------------------")
        for region, porcentaje in porcentajes:
            print(f"REGION CON CODIGO: {region} | {porcentaje:.2f}% inquilinos")

def porcentaje_viviendas_aglomerado (datos):
    hogares = {}
    for fila in datos:
        pondera = int(fila.get("PONDERA"))
        id_hogar = (fila.get("CODUSU"), fila.get("NRO_HOGAR"))
        if id_hogar not in hogares:
            hogares[id_hogar] = {
                "aglomerado": fila.get("AGLOMERADO"),
                "tenencia": fila.get("II7") #corregida la variable
            }

    aglomerados = {}
    for hogar in hogares.values():
        aglo = hogar["aglomerado"]
        tenencia = hogar["tenencia"]
        if aglo not in aglomerados:
            aglomerados[aglo] = {
                "total": 0,
                "propias": 0
            }
        aglomerados[aglo]["total"] += 1
        if tenencia == "1" or tenencia == "2":  # “1” indica propietario de la vivienda y el terreno y "2" Propietario de la vivienda solamente
            aglomerados[aglo]["propias"] += 1
            

    print("Porcentaje de viviendas ocupadas por propietarios por aglomerado:")
    for aglo in sorted(aglomerados, key=lambda x: int(x)): # las ordeno con el sorted
        total = aglomerados[aglo]["total"]
        propias = aglomerados[aglo]["propias"]
        porcentaje = (propias / total) * 100 if total else 0
        print(f"Aglomerado {aglo}: {porcentaje:.2f}%") #acá imprimo el porcentaje de cada aglomerado con solo 2 decimales.


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
                "bano": fila["IV8"] # tmb corregida
            }

    # Paso 2: filtrar hogares con >2 personas y sin baño
    conteo_por_aglomerado = {}
    for hogar, cantidad in personas_por_hogar.items():
        if cantidad > 2:
            bano = info_hogar[hogar]["bano"]
            if bano == "0" or bano == "2":  # ajustar según codificación real
                aglo = info_hogar[hogar]["aglomerado"]
                conteo_por_aglomerado[aglo] = conteo_por_aglomerado.get(aglo, 0) + 1

    # Paso 3: encontrar el aglomerado con mayor cantidad
    if conteo_por_aglomerado:
        aglo_max = max(conteo_por_aglomerado, key=conteo_por_aglomerado.get)
        cantidad = conteo_por_aglomerado[aglo_max]
        print(f"Aglomerado con más viviendas con >2 ocupantes y sin baño: {aglo_max}")
        print(f"Cantidad de viviendas: {cantidad}")
    else:
        print("No se encontraron viviendas con más de 2 ocupantes y sin baño.")
