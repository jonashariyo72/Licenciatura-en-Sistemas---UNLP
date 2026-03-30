# Clase 3 - Administración de Proyectos (Parte 3)

## Estimación de Costos en Ingeniería de Software
> La **estimación** consiste en realizar predicciones sobre el tiempo, esfuerzo y perfiles de recursos humanos necesarios para construir un sistema.
> - ***Inexactitud***: En la Ingeniería de Software (ISW), el cálculo de tiempo y costo es notoriamente inexacto debido a que los proyectos no son repetitivos; varían en dominio, hardware, herramientas y personal.
> - ***Dificultades***: Existen problemas políticos (cuando la estimación se ajusta por conveniencia o se convierte en un objetivo rígido) y técnicos (falta de datos históricos).
> - ***Usos:*** Es fundamental para la planificación (saber cuántos recursos se insumirán) y para el control (saber cuánto se ha hecho y cuánto falta).

## 2. Técnicas de Estimación
> Se presentan diversas metodologías para predecir el esfuerzo:
> - ***Opinión Experta:*** Se basa en la experiencia de personal senior que hace predicciones según parámetros del proyecto.
> - ***Analogía:*** Compara el proyecto actual con proyectos pasados para identificar similitudes y diferencias.
> - ***Descomposición:*** Se focaliza en dividir el producto en componentes o las actividades en tareas detalladas.
> - ***Modelos:*** Técnicas que utilizan fórmulas matemáticas para relacionar ítems clave con el esfuerzo total.
> - ***Enfoques:*** Puede ser Bottom-Up (estimar partes menores y sumar) o Top-Down (estimar el todo y calcular proporciones).

## 3. Modelo COCOMO (Constructive Cost Model)
> Es un modelo de costos desarrollado por Barry Boehm que utiliza una fórmula base: E=a×S b×F, donde E es el esfuerzo (personas-mes), S es el tamaño (en miles de líneas de código fuente entregables o KDSI), F es un factor de ajuste y a,b son constantes.
> - La fórmula es ***PM = c KLOC^k***
> - **PM** -> esfuerzo en personas mes 
> - **c** y **k** constantes dadas por el modelo. k > 1
> - ***Clasificación de Sistemas***: COCOMO define tres tipos de sistemas para determinar las constantes de cálculo:
> - ***Orgánico:*** Sistemas de procesamiento de datos simples y transaccionales (ej. facturación).
> - ***Embebido:*** Software de tiempo real integrado a hardware complejo (ej. control de ascensores).
> - ***Semi-embebido:*** Un punto intermedio con mayor procesamiento de transacciones (ej. monitoreo de redes).

> - ***No*** es sabio ***confiar ciegamente*** en los resultados del modelo.
> - PERO, ***es menos sabio*** *ignorar* el valor de las herramientas que  complementan el juicio experto y la intuición

> **Versiones del Modelo**
> - ***Básico:*** Se usa cuando se conoce muy poco del proyecto (el factor de ajuste F es igual a 1).
> - ***Intermedio:*** Se aplica tras la especificación de requerimientos e introduce conductores de costos.
> - ***Avanzado/Detallado:*** Se aplica al terminar el diseño y estima el esfuerzo a nivel de componentes.


## 4. Conductores de Costos (Cost Drivers)
> Son ***criterios*** que influyen en el cálculo del COCOMO. En el modelo intermedio, el esfuerzo inicial se revisa mediante 15 conductores agrupados en cuatro categorías:
> - ***Atributos del Producto:*** Confiabilidad requerida (RELY), tamaño de base de datos (DATA) y complejidad (CPLX).
> - ***Atributos del Hardware:*** Restricciones de tiempo (TIME) y almacenamiento (STOR), volatilidad de máquina virtual (VIRT).
> - ***Atributos del Personal:*** Capacidad de analistas (ACAP) y programadores (PCAP), experiencia en la aplicación (AEXP), lenguaje (LEXP) y máquina virtual (VEXP).
> - ***Atributos del Proyecto:*** Uso de prácticas modernas (MODP), herramientas de software (TOOL) y limitaciones de cronograma (SCED).

>Cada conductor tiene un factor multiplicador según su grado (desde "Muy Bajo" a "Extra Alto"); por ejemplo, una capacidad de análisis muy baja (ACAP) puede aumentar el esfuerzo calculado en un 46% (factor 1.46).

## 5. COCOMO II y Nuevas Métricas
> Es una actualización para adaptarse a tecnologías modernas y ciclos de vida iterativos. Se basa en tres etapas:
> - ***Prototipos:*** Utiliza Puntos Objeto (basado en número de pantallas, reportes y componentes 3GL).
> - ***Decisiones de Arquitectura***: Utiliza Puntos Función (basado en entradas, salidas, consultas y archivos externos/internos).
> - ***Diseño Detallado:*** Utiliza líneas de código (KDSI).

### Economía de Escala
> COCOMO II introduce un exponente B basado en 5 factores de escala (antecedentes, flexibilidad, resolución de riesgos, cohesión del equipo y madurez del proceso).
> - ***Si B < 1.0***, el proyecto exhibe economía de escala (la productividad aumenta con el tamaño).
> - ***Si B > 1.0***, hay deseconomía de escala debido al aumento de comunicaciones y esfuerzo de integración.