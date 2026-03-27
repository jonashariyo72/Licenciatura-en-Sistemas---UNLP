# Final Redes y Comunicaciones - 2da Mesa Febrero

### 1)

> El control de congestión tiene como finalidad conseguir que no se sature la red en una comunicación. Funciona End-To-End. Tiene en cuenta siempre el estado de la red, a diferencia del control de flujo. Sus tres fases son: SLOW START, CONGESTION AVOIDANCE y por último la DETECCIÓN DE CONGESTIÓN.

### 2) 

> DHCP es un protocolo de Capa 3 Helper de I, tiene como funcionalidad asignar configuración a las distintas redes. Sus mensajes principales son: ACK, NAK, Release, Request y Discover (Broadcast),  y Offer (Unicast).

### 3) 
### POP e IMAP

> - ***SIMILITUDES***: 
>   - Ambos requieren autenticación 
>   - Ambos permiten correr de forma segura (TLS)
>   - Ambos corren sobre TCP

> - ***DIFERENCIAS***
>   - POP3 corre sobre el puerto 110 e IMAP sobre el puerto 143
>   - POP3 descarga los mails y los borra e IMAP los mantiene
>   - POP3 no mantiene estado de las carpetas y mensajes e IMAP si.
>   - POP3 puede ser limitado para usuarios nómades e IMAP es mucho más flexible para sincronizar carpetas y mensajes.

### 4)

### a)

| Destino | Mask | Next-Hop | Iface | 
| :--- | :---: | :---: | :---: |
| **10.0.0.0** | /29 | - | 10.0.0.2
| **172.17.1.0** | /24 | 10.0.0.1 | 10.0.0.2 |
| **192.168.10.0**|  /24 | 10.0.0.3 | 10.0.0.2 |
| **210.20.10.4**|  /30 | - | 10.0.0.5 |
| **163.10.0.0**|  /26 | 210.20.10.6 | 10.0.0.5 |
| **0.0.0.0**|  /30 | 210.20.10.6 | 10.0.0.5 |

### b)

> Se le debería agregar la IP `172.17.0.0/24`. La sumarización quedaría así:

| Destino | Mask | Next-Hop | Iface | 
| :--- | :---: | :---: | :---: |
| **172.17.1.0** | /24 | 10.0.0.1 | 10.0.0.2 |
| **172.17.0.0** | /24 | 10.0.0.1 | 10.0.0.2 |
|  ***(Sumarización)*** **172.17.0.0**| /23 | 10.0.0.1 | 10.0.0.2 |

### 5)

### a)

> | **MAC Origen**: MAC_R1_IFACE1 | **MAC Destino**: MAC_R2_IFACE2 | **IP Origen**: 10.0.0.1 | **IP Destino**: 10.0.0.2|