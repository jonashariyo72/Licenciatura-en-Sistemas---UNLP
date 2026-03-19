# Conceptos y Paradigmas de Lenguajes de Programación  2026 
# Práctica Nro 1 - Historia, evolución y características de Leng. de Programación 


### Objetivo:  Conocer la evolución de los lenguajes de programación y sus características.


### Ejercicio 1: Los lenguajes de programación más representativos son:  

- ***1951 - 1955: Lenguajes tipo assembly*** : Introducción de códigos simbólicos y mnemónicos para instrucciones y direcciones de memoria, reemplazando el código binario manual
. Se crean herramientas como el ensamblador para automatizar la traducción a código máquina
---
- ***1956 - 1960: FORTRAN, ALGOL 58, ALGOL 60, LISP*** - ***FORTRAN:*** Primer lenguaje de alto nivel con soporte para notación algebraica y números de punto flotante, orientado a científicos, 
                                                        ***ALGOL 60:*** Introduce la estructura de bloques, recursividad, tipos de datos numéricos explícitos y estructuras de control estructuradas (, loops if-elsefor), 
                                                        ***LISP:*** Pionero en el paradigma funcional, procesamiento simbólico, manejo dinámico de memoria y el concepto de programas como datos (S-expressions)

---
- ***1961 - 1965: COBOL, ALGOL 60, SNOBOL, JOVIAL*** : 
    ***COBOL:*** Enfocado en el procesamiento de datos comerciales, introduce la descripción de registros y archivos, y busca una sintaxis similar al inglés natural para mejorar la legibilidad

    ***SNOBOL:*** Especializado en la manipulación de cadenas y reconocimiento de patrones

---
- ***1966 - 1970: APL, FORTRAN 66, BASIC, PL/I, SIMULA 67, ALGOL-W*** : ***SIMULA 67:*** Introduce el concepto de clase, objeto y herencia, sentando las bases de la programación orientada a objetos.
***PL/I:*** Intenta integrar características de FORTRAN, ALGOL y COBOL; introduce el manejo de excepciones y multitarea primitiva

    BASIC: Diseñado para la facilidad de uso y la programación interactiva en terminales
---
- ***1971 - 1975: Pascal, C, Scheme, Prolog*** : ***Pascal:*** Énfasis en la programación estructurada y tipos de datos definidos por el usuario para la enseñanza

***C:*** Lenguaje de sistemas que combina potencia y portabilidad, muy ligado al éxito de Unix

***Prolog:*** Basado en la lógica formal, introduce el paradigma de programación lógica y declarativa

***Esquema:*** Dialecto de LISP que introduce el alcance estático (alcance léxico)

---
- ***1976 - 1980: Smalltalk, Ada, FORTRAN 77, ML*** : ***Smalltalk:*** Primer lenguaje puramente orientado a objetos con un entorno gráfico integrado y tipado dinámico

***Ada:*** Diseñado para sistemas embebidos, enfatiza la confiabilidad, tipado fuerte, concurrencia y TADs (paquetes)

***ML:*** Introduce el paradigma funcional con tipado estático e inferencia de tipos

---
- ***1981 - 1985: Smalltalk 80, Turbo Pascal, Postscript***: 
---

- ***1986 - 1990: FORTRAN 90, C++, SML***: ***C++:*** Extensión de C que incorpora clases y orientación a objetos manteniendo la eficiencia de C
.
---
- ***1991 - 1995: TCL, PERL, HTML***:
---
- ***1996 - 2000: Java, Javascript, XML***: ***Java:*** Portabilidad total mediante byte code y Máquina Virtual (JVM), diseñado para la red

***Python:*** Énfasis en la simplicidad y legibilidad extrema, tipado dinámico y sintaxis concisa (uso de indentación significativa)

---

### Indique para cada uno de los períodos presentados cuales son las características nuevas que se incorporan y cual de ellos la incorpora. 



### Ejercicio 2: Escriba brevemente la historia del lenguaje de programación que eligió en la encuesta u otro de su preferencia.

> ***Python*** fue creado por Guido van Rossum a finales de los 80 en el CWI (Países Bajos). Deriva del lenguaje ABC, diseñado para científicos y no programadores. Van Rossum buscaba un lenguaje de "puente" entre lenguajes de sistemas (C) y de scripting (Perl), con una sintaxis más limpia y tipos de datos potentes como diccionarios y listas. Su éxito masivo se dio por su distribución gratuita y su gran comunidad.



### Ejercicio 3: ¿Qué atributos debería tener un buen lenguaje de programación? Por ejemplo, ortogonalidad, expresividad, legibilidad, simplicidad, etc. De al menos un ejemplo de un lenguaje que cumple con las características citadas.

> Estos son algunos conceptos que engloban a un buen lenguaje de programación:
> - ***Simplicidad y Legibilidad:*** Programas fáciles de leer y mantener. Ejemplo: Python, por su sintaxis clara y pocas reglas complejas.
> - ***Ortogonalidad:*** Capacidad de combinar un conjunto pequeño de constructores primitivos de forma consistente. Ejemplo: Algol 68, donde los constructores se combinan sin restricciones inesperadas.
> - ***Confiabilidad:*** Seguridad ante errores (tipado fuerte, chequeo en compilación) . Ejemplo: Ada, por sus estrictas reglas de tipado y manejo de excepciones.
> - ***Eficiencia:*** Uso óptimo de recursos (tiempo/memoria). Ejemplo: FORTRAN o C, diseñados para generar código máquina muy rápido.


### Ejercicio 4: Tome uno o dos lenguajes de los que ud. Conozca  y 
    ● Describa los tipos de expresiones que se pueden escribir en él/ellos  
    ● Describa las facilidades provistas para la organización del programa 
    ● Indique cuáles de los atributos del ejercicio anterior posee el/los lenguaje/s elegidos y cuáles 
    no posee, justifique en cada caso. 

    ---

## 4. Lenguaje elegido: JAVA 
> - ***Tipos de expresiones:*** Soporta expresiones aritméticas, lógicas y relacionales. En Java, la asignación es una expresión que devuelve un valor.
> - ***Organización del programa:*** Utiliza paquetes para agrupar clases relacionadas, interfaces para definir comportamientos y un sistema de archivos que refleja la estructura de clases.
> - ***Atributos:***
>   - **Confiabilidad:** Posee (tipado fuerte, recolección de basura automática que evita fugas de memoria).
>   - **Simplicidad:** Parcialmente (elimina punteros explícitos de C++, pero su estructura de clases puede ser verbosa).
>   - **Ortogonalidad:** No totalmente (distingue entre tipos primitivos y objetos, lo que requiere clases "envoltorio").
---


## Lenguajes    -    ADA 

### Ejercicio 5: Describa las características más relevantes de Ada, referida a: 
> - *Tipos de datos*:  Es un lenguaje fuertemente tipado. Incluye tipos escalares (enteros, reales, enumerativos), tipos de acceso (punteros controlados) y tipos compuestos (arrays y registros). 
> - *Tipos abstractos de datos – paquetes*:  Los paquetes permiten separar la especificación (interfaz pública) de la implementación (cuerpo privado), facilitando la ocultación de información.
> - *Estructuras de datos*: Ofrece arrays restringidos y no restringidos (unconstrained), registros variantes para uniones discriminadas y una rica jerarquía de tipos.
> - *Manejo de excepciones*: Provee un mecanismo robusto para interceptar errores en tiempo de ejecución () y definir manejadores específicos () para continuar la ejecución de forma seguraraisewhen.
> - *Manejo de concurrencia*: Introduce las tareas () como unidades que se ejecutan en paralelo, tipos protegidos para exclusión mutua y el mecanismo de  cita () para la sincronización entre procesos `tasks` `rendezvous`.

## Lenguajes    -    JAVA

### Ejercicio 6: Diga para qué fue, básicamente, creado Java.¿Qué cambios le introdujo a la Web? ¿Java es un lenguaje dependiente de la plataforma en dónde se ejecuta? ¿Por qué?

> ***Origen:*** Java fue creado originalmente por James Gosling y su equipo en Sun Microsystems como un lenguaje para sistemas embebidos en electrodomésticos (como hornos microondas).
> ***Cambios en la Web:*** Introdujo el concepto de "escribir una vez, ejecutar en cualquier lugar" (write once, run anywhere), lo cual fue ideal para el crecimiento de Internet y redes, permitiendo la distribución de software a través de arquitecturas diversas.
> ***Independencia de plataforma:*** Java no es dependiente de la plataforma física. Esto se debe a que el compilador traduce el código fuente a un código intermedio llamado byte code, el cual es independiente de la máquina. Este byte code es ejecutado por una Máquina Virtual Java (JVM) específica para cada sistema operativo, que actúa como intérprete.

### Ejercicio 7: ¿Sobre qué lenguajes está basado? 

> **Java** está basado fundamentalmente en la sintaxis de C++ para atraer a una amplia base de programadores. Además, adoptó muchas características de Smalltalk, como la recolección automática de basura y el uso de referencias en lugar de punteros explícitos.

### Ejercicio 8: ¿Qué son los applets? ¿Qué son los servlets?  

> Los ***Applets*** son pequeñas aplicaciones Java que se ejecutan en el navegador del cliente,, permitiendo la creación de contenido interactivo como gráficos, animaciones y juegos. Mientras que los ***Servlets*** son componentes que se ejecutan en el servidor para generar contenido dinámico, interactuar con el cliente a través de un modelo de solicitud-respuesta.


## Lenguajes    -    C

### Ejercicio 9: ¿Cómo es la estructura de un programa escrito en C? ¿Existe anidamiento de funciones? 

> **Estructura:** Un programa en C consiste en uno o varios archivos. Se organiza mediante directivas de preprocesador (), declaraciones externas o globales y definiciones de funciones#include. Todo programa debe tener una función llamada  para iniciar su ejecuciónmain.
> **Anidamiento:** En C no existe el anidamiento de funciones (no se puede definir una función dentro de otra). Solo se permite el anidamiento de sentencias compuestas o bloques dentro de las funciones.


### Ejercicio 10: Describa el manejo de expresiones que brinda el lenguaje.

> En ***C***, la distinción entre sentencias de asignación y expresiones es ***tenue***; una asignación es en sí misma una expresión que devuelve el valor asignado como resultado. Permite asignaciones múltiples en una sola línea (ej. a = b = c = 0). Permite que cualquier expresión que devuelva un l-value (una dirección de memoria modificable) aparezca a la izquierda de un operador de asignación.


## Lenguajes - Python, RUBY, PHP

### Ejercicio 11: ¿Qué tipo de programas se pueden escribir con cada uno de estos lenguajes? ¿A qué paradigma responde cada uno? ¿Qué características determinan la pertenencia a cada paradigma?  

> - **Python:** Se utiliza para scripting de propósito general, experimentación rápida y enseñanza. Responde al paradigma Orientado a Objetos y soporta un estilo imperativo.
> - **Ruby:** Muy utilizado en aplicaciones cliente/servidor web y dispositivos móviles. Es un lenguaje puramente Orientado a Objetos.
> - **PHP:** Mencionado como un lenguaje interpretado ideal para aplicaciones web.
> - **Determinación de paradigma:** La pertenencia se determina por la unidad de modularización (clases en OO, funciones en funcional) y el modelo de cómputo (cambio de estado en imperativo, evaluación de funciones en funcional).

### Ejercicio 12: Cite otras características importantes de Python, Ruby, PHP, Gobstone y Processing. Por ejemplo: tipado de datos,  cómo se organizan los programas, etc. 

> - ***Python***: Utiliza identación para definir bloques de código. Posee tipado dinámico fuerte (los tipos se verifican en tiempo de ejecución pero no se permiten operaciones inválidas entre tipos). Tiene recolección de basura automática.
> - ***Ruby:*** Se caracteriza por su ortogonalidad, ya que casi todo es un objeto y toda sentencia es una expresión. Su sintaxis se describe como simple, elegante y concisa.
> - ***PHP*** es un lenguaje de programación de código abierto, multiplatafórmico, se integra bien con HTML, lo que le permite crear páginas webs dinámicas.
> - ***Gobstones*** se destaca por su entorno visual y intuitivo.
> - ***Processing*** es un lenguaje de desarrollo integrado de código abierto que se basa en *Java*.


## Lenguaje - JAVASCRIPT

### Ejercicio 13: ¿A qué tipo de paradigma corresponde este lenguajes? ¿A qué tipo de Lenguaje pertenece? 

> ***Javascript*** se utiliza principalmente para aplicaciones basadas en la Web. Se sitúa junto a Java y Python como lenguajes que han incorporado características que los alejan de C y los acercan a conceptos de Lisp (paradigma funcional/dinámico).

### Ejercicio 14: Cite otras características importantes de javascript. Tipado de datos, excepciones, variables, etc.

> **JavaScript** es un lenguaje ***débilmente tipado y dinámico***, lo que significa que no se define el tipo de una variable al instanciarla. El tipo de la variable se asigna atendiendo al valor que le asignemos. 
> - Es un ***lenguaje imperativo***, lo que significa que las sentencias se ejecutan de manera secuencial, no realiza un proceso de compilación a código máquina, sino que necesita de un interprete para obtener el lenguaje máquina. 
> - Es un ***lenguaje sencillo y extensible***, lo que significa que no hace falta tener amplios conocimientos de programación para desarrollar programas. 
> - Es un lenguaje ***multiplataforma***, lo que significa que puede ser ejecutado en diferentes sistemas operativos y plataformas.
> - Es un lenguaje ***orientado a objetos***, lo que significa que se basa en la creación de objetos y la programación orientada a objetos. Esto permite una gran flexibilidad en la creación de objetos y su manipulación.






