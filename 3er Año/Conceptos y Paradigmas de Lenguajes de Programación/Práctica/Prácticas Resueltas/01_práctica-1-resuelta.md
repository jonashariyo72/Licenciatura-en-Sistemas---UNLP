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


## Lenguajes    -    ADA 

### Ejercicio 5: Describa las características más relevantes de Ada, referida a: 
    ● Tipos de datos 
    ● Tipos abstractos de datos – paquetes  
    ● Estructuras de datos 
    ● Manejo de excepciones 
    ● Manejo de concurrencia 