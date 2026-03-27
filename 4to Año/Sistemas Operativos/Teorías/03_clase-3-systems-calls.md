# Llamadas al Sistema

## ¿Qué es una Llamada al Sistema (System Call)?

Es el mecanismo fundamental que utiliza un proceso de usuario para solicitar un servicio al Sistema Operativo. Los sistemas modernos operan bajo un modelo de protección que distingue dos entornos:
> - ***Modo Usuario:*** Donde se ejecutan los procesos de usuario con privilegios limitados, sin acceso directo al hardware y restringidos a su propio espacio de memoria.
> - ***Modo Kernel (o Privilegiado):*** Donde reside el núcleo del SO con acceso total a los recursos de la máquina.

La llamada al sistema actúa como la interfaz o API (como la biblioteca libc en UNIX/Linux) que permite a los programas cruzar de forma segura la barrera entre estos dos modos para acceder a recursos gestionados por el kernel.

## El Mecanismo de Ejecución (Paso a Paso)
El proceso de realizar una llamada al sistema (como un ) sigue una serie de pasos lógicos para garantizar la seguridad y el orden `read`:

> - ***Preparación de parámetros:*** El programa de usuario coloca los parámetros necesarios en la pila (stack) o en los registros del procesador.

> - ***Invocación de la biblioteca:*** Se llama a un procedimiento de biblioteca (ej.  en la librería de C)`read`.

> - ***Identificación de la llamada:*** La biblioteca coloca el número de la llamada al sistema en un registro específico (en Linux x86 de 32 bits es el registro EAX).

> - ***El TRAP:*** Se ejecuta una instrucción especial de trap o interrupción por software (ej.  en 32 bits o  en 64 bits)`int 80hsyscall`.

> - ***Cambio de Modo:*** El hardware cambia la CPU de Modo Usuario a Modo Kernel y transfiere el control a una dirección fija en el núcleo.

> - ***Despacho y Ejecución:*** El dispatcher del kernel consulta una tabla de punteros (indexada por el número de llamada) para encontrar el manejador correcto y ejecutar el código del servicio solicitado.

> - ***Retorno:*** Una vez finalizada la tarea, el control se devuelve al procedimiento de biblioteca en el espacio de usuario, cambiando nuevamente al modo no privilegiado.

> - ***Limpieza:*** El programa de usuario limpia la pila de los parámetros y continúa su ejecución.

## Categorías principales de System Calls

Para UNIX y Linux, las llamadas se agrupan generalmente en las siguientes categorías:

> - ***Control de Procesos:*** Creación, terminación y gestión de procesos. Ejemplos:  (crear hijo),  (reemplazar imagen del núcleo),  (esperar terminación),  (finalizar ejecución)forkexecvewaitpidexit.

> - ***Gestión de Archivos:*** Operaciones sobre archivos individuales. Ejemplos:  (resumir),  (leer),  (escribir),  (cerrar),  (mover puntero)`open read write close seek.`

> - ***Gestión de Directorios y Sistema de Archivos:*** Manejo de la estructura del disco. Ejemplos:  (crear directorio),  (eliminar),  (vínculos),  (montar sistemas de archivos)mkdirrmdirlinkmount.

> - ***Miscelánea y Comunicaciones:*** Envío de señales y obtención de información del sistema. Ejemplos:  (cambiar directorio actual),  (enviar señal),  (obtener hora),  (crear tuberías de comunicación)`chdir kill time pipe`.

## Detalles Técnicos en Linux
> - ***Parámetros:*** En Linux, las llamadas pueden tener como máximo 6 parámetros.

> - ***Registros (x86 32 bits):*** EAX lleva el número de syscall; EBX, ECX, EDX, ESI, EDI llevan los parámetros del 1 al 5 respectivamente.

> - ***Seguridad:*** El kernel debe validar cuidadosamente los parámetros que provienen del espacio de usuario. Por ejemplo, los punteros pasados no pueden apuntar al espacio de memoria del Kernel.

> - ***Estándar POSIX:*** Especifica la interfaz de las bibliotecas de procedimientos que el sistema debe proveer, pero no dicta cómo deben implementarse las llamadas al sistema subyacentes.

Este sistema de capas asegura que, aunque el programador vea la llamada como una función común, el SO mantenga el control total y la protección del hardware.