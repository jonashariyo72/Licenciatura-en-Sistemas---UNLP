# Conceptos y Paradigmas de Lenguajes de Programación  2026 
# Práctica Nro 1 - Historia, evolución y características de Leng. de Programación 


### Objetivo:  conocer como se define léxicamente un lenguaje de programación y cuales son las herramientas necesarias para hacerlo 


### Ejercicio 1: Complete el siguiente cuadro: 

| BNF | EBNF | Diagramas Sintácticos | Significado |
| :--- | :---: | :---: | :---: |
| palabra terminal | palabra terminal |   | **Definición de elemento terminal** |
| `<>` | `<>` | rectángulo | **Definición de  un elemento NO terminal** |
| `::=` |  `::=` | diagrama con rectángulos, óvalos y flechas | **Es un metasímbolo de como lo que está a la izquierda se define con lo de la derecha**|
| `/` | `(/)` (en ambas es recta pero MD no me deja) | flecha que se divide en dos o más caminos | **Indicador de un OR** |  
| `< p > < p1 > ` |  `{}` |  bucle, flecha de retorno   | **Repetición** |
|Usa recursión | `{}` |rectángulo del bucle como opción después|**Repetición de 0 o más veces** | 
|Usa recursión | `{}+` | flecha de retorno después del rectángulo del bucle| **Repetición de 1 o más veces**|
|Usa recursión | `[]` | rectángulo del bucle como opción antes| **Repetición opcional**|


### Ejercicio 2: ¿Cuál es la importancia de la sintaxis para un lenguaje? ¿Cuáles son sus elementos? 

> La ***sintaxis*** es vital porque establece las reglas formales para componer caracteres y formar programas válidos. Sus elementos principales incluyen el alfabeto, identificadores, operadores, palabras reservadas y comentarios



### Ejercicio 3: ¿Explique a qué se denomina regla lexicográfica y regla sintáctica? 

> Las ***reglas léxicas*** definen cómo se forman las palabras (tokens) a partir de caracteres (ej. cómo se escribe un número), mientras que las ***reglas sintácticas*** definen cómo se combinan esas palabras para formar sentencias (ej. la estructura de un if).

### Ejercicio 4:¿En la definición de un lenguaje, a qué se llama palabra reservadas? ¿A qué son equivalentes en la definición de una gramática? De un ejemplo de palabra reservada en el lenguaje que más conoce. (Ada,C,Ruby,Python,..)

> Una palabra reservada es una palabra clave que el programador no puede usar como identificador. En una gramática, equivalen a símbolos terminales. Ejemplos:  en C,  en Pascal,  en Python: `if` `begin` `def`.

### Ejercicio 5: Dada la siguiente gramática escrita en BNF:

### G= ( N, T, S, P) 
### N = {<numero_entero>, <digito> } 
### T = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9} 
### S = <numero_entero> 
### P = { 
### <numero_entero>::=<digito><numero_entero> | <numero_entero><digito> | 
### <digito> 
### <digito> ::= 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 
### } 
### a - Identifique las componentes de la misma 

> - ***N (Símbolos No Terminales):*** Son las "categorías" o "variables" de la gramática. No aparecen en el resultado final del programa; solo sirven para estructurar las reglas.En BNF se escriben entre ángulos: `<sentencia>`, `<variable>`, `<digito>`.En EBNF se suelen escribir en minúsculas: expresion, termino.
> - ***T (Símbolos Terminales):*** Son los elementos básicos y finales del lenguaje. Es el "alfabeto" real que el programador escribe en el código.Ejemplos: palabras reservadas (if, while), operadores (+, -), números (0, 1, 2) o signos de puntuación (;, {).Se llaman "terminales" porque una vez que llegas a ellos en una derivación, no puedes reemplazarlos por nada más.
> - ***S (Símbolo Inicial)***: Es un elemento especial que pertenece a $N$ ($S \in N$). Es el "punto de partida" de cualquier derivación. Toda estructura que quieras validar (por ejemplo, un programa completo o una expresión matemática) debe empezar a derivarse desde S.
> - ***P (Reglas de Producción):*** Es el conjunto de reglas que indican cómo se pueden transformar los símbolos. 

### b - Indique porqué es ambigua y corríjala 

Preguntar!
