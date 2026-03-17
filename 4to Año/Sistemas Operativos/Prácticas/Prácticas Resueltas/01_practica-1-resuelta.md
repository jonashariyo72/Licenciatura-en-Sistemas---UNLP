# SISTEMAS OPERATIVOS -  Práctica 1

---

## A - Introducción 

El propósito de esta primera sección de la práctica es introducir los conceptos 
preliminares que necesitarde esta guía de estudio.


### 1.  ¿Qué es GCC? 

> GCC es el compilador de C en el proyecto GNU. Es la herramienta principal utilizada para transformar el código fuente del kernel Linux (escrito mayormente en C y Assembler) en un binario ejecutable. Lo usamos también para crear **archivos objeto** y para realizar el enlazado final que crea el archivo ejecutable.

### 2.  ¿Qué es make y para que se usa? 

> Make es una herramienta fundamental diseñada para organizar y automatizar el proceso de generación de ejecutables u otros archivos a partir de código fuente. Su **función** **principal** es leer un archivo de texto llamado ***Makefile***, el cual contiene un conjunto de reglas que definen cómo se debe construir cada parte de un proyecto. 

> Se usa principalmente para: 
> - ***Gestión de dependencias:*** La herramienta lleva la cuenta de qué archivos de código objeto dependen de qué archivos fuente o de encabezado (.h)
> - ***Eficiencia en la compilación:***  verifica la fecha de modificación de los archivos y solo recompila aquellos que han cambiado desde la última vez que se generó el binariomake.
> - ***Automatización compleja:*** Permite ejecutar procesos largos y complicados con unos pocos comandos sencillos, interpretando directivas que de otro modo deberían ingresarse manualmente en la terminal
> - ***Versatilidad:*** Aunque se asocia principalmente a C, se utiliza para cualquier tarea donde un archivo de salida dependa de otros, como convertir LaTeX o Markdown a PDF, o compilar código en Ensambler y Rust
> - ***Compilación paralela:*** Mediante el parámetro `-jX`, permite ejecutar múltiples tareas de compilación de forma simultánea (donde X es el número de procesadores), acelerando significativamente el proceso en máquinas multinúcleo


### 3.  La carpeta /home/so/practica1/ejemplos/01-make de la VM contiene ejemplos de uso de make. Analice los ejemplos, en cada caso ejecute `make` y luego `make run` (es opcional ejecutar el ejemplo 4, el mismo requiere otras dependencias que  no vienen preinstaladas en la VM): 

### a.  Vuelva a ejecutar el comando `make`. ¿Se volvieron a compilar los programas?  ¿Por qué? 

>No, no se compila de nuevo. Porque `make` es inteligente y si la fecha del compilado anterior es reciente, no pierde tiempo en re-compilar.



### b.  Cambie la fecha de modificación de un archivo con el comando `touch` o  editando el archivo y ejecute `make`. ¿Se volvieron a compilar los programas? ¿Por qué? 

>Si, se vuelven a compilar. Porque ahora el archivo fuente tiene una fecha más reciente que el ejecutable, y make asume que hubo cambios que deben procesarse.

### c.  ¿Por qué “run” es un target “phony”?

>Un target ***Phony*** es aquel que no representa un archivo real que se va a generar. Si no fuera "phony" y por casualidad existiera un archivo llamado run en la carpeta, make nunca ejecutaría el comando porque pensaría que el archivo run ya está listo. Al marcarlo como .PHONY: run, le decís: "Ejecutá los comandos de esta regla siempre, sin importar si existe un archivo con ese nombre".


### d.  En el ejemplo 2 la regla para el target `dlinkedlist.o` no define cómo generar el  target, sin embargo el programa se compila correctamente. ¿Por qué es esto? 

>Esto es por las Reglas Implícitas de `make`. make sabe que para generar un objeto .o casi siempre se necesita un archivo .c con el mismo nombre y se usa el compilador cc o gcc. Si vos no le decís cómo hacerlo, él usa su regla interna por defecto.


### 4.  ¿Qué es el kernel de GNU/Linux? ¿Cuáles son sus funciones principales dentro del Sistema Operativo? 

>El ***Kernel*** es la pieza fundamental del software de un sistema operativo que se ejecuta directamente sobre el hardware en modo kernel. En este modo, el núcleo tiene acceso completo a todo el hardware y puede ejecutar cualquier instrucción que la máquina sea capaz de realizar.

> Sus funciones principales son:  
> - **Gestión de procesos:** Es responsible de la creación y terminación de procesos (programas en ejecución). Utiliza un ***planificador*** (***scheduler***) para decidir qué proceso obtiene acceso a la CPU, cuándo y por cuánto tiempo, permitiendo la multitarea.
> - **Gestión de memoria:** Administra la memoria RAM, asignándola a los procesos de manera equitativa y eficiente. Implementa ***memoria virtual***.
> - **Provisión de un sistema de archivos:** El núcleo gestiona el ***almacenamiento en disco***, permitiendo crear, recuperar, actualizar y eliminar archivos.
> - **Acceso a dispositivos de E/S:** Proporciona una interfaz estandarizada para comunicarse con dispositivos periféricos (teclado, ratón, monitor, discos) a través de los ***drivers o controladores***.

### 5.  Explique brevemente la arquitectura del kernel Linux teniendo en cuenta: tipo de  kernel, módulos, portabilidad, etc. 

> La arquitectura del kernel Linux se caracteriza por ser un diseño ***monolítico***, pero con una estructura altamente flexible y funcional gracias a su capacidad de modularización y abstracción de recursos.

> - ***Tipo de Kernel:*** **Monolítico**
>Linux es un kernel monolítico, lo que significa que todo el sistema operativo (incluyendo la gestión de procesos, memoria, sistemas de archivos y drivers) reside y se ejecuta dentro del espacio del kernel en modo privilegiado. 
> - ***Módulos del Kernel***
>A pesar de su naturaleza monolítica, Linux implementa un diseño modular mediante módulos cargables en caliente.  
>   - ***Funcionalidad:*** Permiten extender las capacidades del núcleo (como agregar soporte para un nuevo dispositivo o un sistema de archivos) sin necesidad de reiniciar el sistema ni recompilar todo el kernel. 
>   - ***Ejecución:*** Estos módulos se cargan en el mapa de memoria del kernel bajo demanda y se ejecutan en modo privilegiado, por lo que un error en un módulo puede comprometer la estabilidad de todo el sistema.

> - ***Portabilidad:*** Aunque originalmente fue desarrollado para la arquitectura x86 (Intel 386), Linux fue diseñado para ser altamente portable>:
>   - ***Lenguajes***: Está escrito mayoritariamente en lenguaje C, lo que facilita su traslado a diferentes arquitecturas de hardware.
>   - ***Abstracción***: Posee una pequeña capa de código dependiente de la máquina escrita en Assembler (para tareas de bajo nivel como el manejo de interrupciones o la inicialización de la CPU) que se reescribe para cada plataforma específica. 

### 6.  ¿Cómo se define el versionado de los kernels Linux en la actualidad?

> En la actualidad, el versionado de los kernels Linux se define mediante una nomenclatura de tres o cuatro números (A.B.C o A.B.C.D), abandonando esquemas antiguos donde se diferenciaba entre versiones estables e inestables por números pares o impares. La estructura actual del versionado se desglosa de la siguiente manera:

> - ***Primer número (Versión):*** Indica la versión principal del kernel (por ejemplo, el 6 en la versión 6.13.7).

> - ***Segundo número (Revisión mayor o serie):*** Indica cambios significativos o nuevas funcionalidades. A diferencia de lo que ocurría antes de la serie 2.6, actualmente cada nueva versión puede contener nuevas características y no existe una separación entre ramas de desarrollo y estables basadas en si este número es par o impar. Los ciclos de lanzamiento de estas versiones suelen ser de aproximadamente tres meses.

> - ***Tercer número (Revisión menor):*** Se refiere a lanzamientos que incluyen soporte para nuevos drivers o mejoras menores.

> - ***Cuarto número (Parches de seguridad o errores):*** Se utiliza cuando una versión estable requiere correcciones urgentes de errores o parches de seguridad. En este caso, se añade un cuarto número secuencial (por ejemplo, el 7 en 6.13.7) para identificar la revisión de esa versión específica sin esperar al siguiente ciclo de desarrollo.


### 7. ¿Cuáles son los motivos por los que un usuario/a GNU/Linux puede querer  re-compilar el kernel?

> Los principales motivos pueden ser: 
> - Soporte de hardware y nuevas funcionalidades
> - Optimización del rendimiento
> - Reducción del tamaño y uso de recursos
> - Soporte para sistemas de archivos específicos
> - Aplicación de parches y actualizaciones 
> - Seguridad

