# SISTEMAS OPERATIVOS -  Práctica 1

---

## A - Introducción 

***El propósito de esta primera sección de la práctica es introducir los conceptos 
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
> - ***Compilación paralela:*** Mediante el parámetro -jX, permite ejecutar múltiples tareas de compilación de forma simultánea (donde X es el número de procesadores), acelerando significativamente el proceso en máquinas multinúcleo
.


### 3.  La carpeta /home/so/practica1/ejemplos/01-make de la VM contiene ejemplos de uso de make. Analice los ejemplos, en cada caso ejecute `make` y luego `make run` (es opcional ejecutar el ejemplo 4, el mismo requiere otras dependencias que  no vienen preinstaladas en la VM): 

### a.  Vuelva a ejecutar el comando `make`. ¿Se volvieron a compilar los programas?  ¿Por qué? 


### b.  Cambie la fecha de modificación de un archivo con el comando `touch` o  editando el archivo y ejecute `make`. ¿Se volvieron a compilar los programas? ¿Por qué? 


### c.  ¿Por qué “run” es un target “phony”? 


### d.  En el ejemplo 2 la regla para el target `dlinkedlist.o` no define cómo generar el  target, sin embargo el programa se compila correctamente. ¿Por qué es esto? 



### 4.  ¿Qué es el kernel de GNU/Linux? ¿Cuáles son sus funciones principales dentro del Sistema Operativo? 


### 5.  Explique brevemente la arquitectura del kernel Linux teniendo en cuenta: tipo de  kernel, módulos, portabilidad, etc. 



### 6.  ¿Cómo se define el versionado de los kernels Linux en la actualidad?


### 7.  ¿Cuáles son los motiv