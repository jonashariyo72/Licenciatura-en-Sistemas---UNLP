# Conceptos y Paradigmas de Lenguajes de Programación  2026 
# Práctica Nro 8 - Estructuras de control y sentencias


### Objetivo:  reconocer las diferencias entre las implementaciones de las estructuras de control de los distintos lenguajes 

### Ejercicio 1: Sistemas de Tipos:

#### 1. Una sentencia puede ser simple o compuesta, ¿Cuál es la diferencia?

> Una **Sentencia Simple** es aquella que realiza una única acción atómica o de control de flujo, y no contiene estructuralmente a otras sentencias en su interior. En cambio, una **Sentencia Compuesta**, es una secuencia de cero o más sentencias agrupadas dentro de delimitadores sintácticos específicos que el compilador/intérprete trata como si fueran una única sentencia.

#### Ejercicio 2: Analice como C  implementa la asignación.

> En el lenguaje C, la asignación tiene una naturaleza particular: no es solo una sentencia, sino una expresión que produce un valor.

> - ***L-value y R-value:*** La sintaxis es L-value = R-value;. El L-value (Location value) debe ser una expresión que haga referencia a una posición de memoria modificable (ej. una variable o un elemento de un arreglo). El R-value (Read value) es cualquier expresión que produzca un valor asignable.
> - ***Retorno de valor:*** La expresión completa de asignación devuelve el mismo valor que se acaba de almacenar en el L-value.
> - ***Asignaciones encadenadas (múltiples):*** Debido a que la asignación devuelve un valor y tiene asociatividad de derecha a izquierda, C permite escribir cosas como: `a = b = c = 10;`
> - ***Operadores de asignación compuesta:*** C introduce operadores como +=, -=, *=, /=. La instrucción x += 5; equivale a x = x + 5;, con la sutil ventaja semántica de que la dirección de memoria de x (su L-value) se evalúa una sola vez, lo que resulta más eficiente.
> - ***Uso en estructuras de control:*** Al ser una expresión, puede embeberse dentro de otras condiciones, lo cual es muy común en C pero peligroso si se confunde con la igualdad (==):

#### Ejercicio 3: ¿Una expresión de asignación puede producir efectos laterales que afecten al resultado final, dependiendo de cómo se evalúe? De ejemplos. 

> Sí. Un efecto lateral (side effect) ocurre cuando la evaluación de una expresión modifica el estado de una variable en memoria. Si el lenguaje no define estrictamente el orden en el que se deben evaluar los operandos de una expresión mayor (por ejemplo, los operandos de una suma), el resultado final dependerá completamente de las decisiones de optimización del compilador.

#### Ejercicio 4: Qué significa que un lenguaje utilice circuito corto o circuito largo para la evaluación de una expresión. De un ejemplo en el cual por un circuito de error y por el otro no. 

> - ***Circuito Largo (Evaluación Completa):*** El procesador evalúa absolutamente todos los operandos de una expresión lógica (AND, OR), sin importar si el resultado ya quedó determinado por el primer operando.

> - ***Circuito Corto:*** La evaluación se detiene de forma inteligente tan pronto como el resultado final de la expresión booleana está garantizado.
>   - En un **AND** (A && B): Si A es falso, el resultado final será falso obligatoriamente. Por lo tanto, B no se evalúa.
>   - En un **OR** (A || B): Si A es verdadero, el resultado final será verdadero obligatoriamente. Por lo tanto, B no se evalúa.

#### Ejercicio 5: ¿Qué regla define Delphi, Ada y C para la asociación del else con el if correspondiente? ¿Cómo lo maneja Python?

> - **Solución en C y Delphi (Pascal):** Utilizan la regla de la cercanía léxica. El else se asocia automáticamente con el if más cercano físicamente que se encuentre "abierto" (es decir, que no tenga ya su propio else). Para romper esta regla en estos lenguajes, el programador debe usar obligatoriamente llaves {} o bloques begin/end.

> - **Solución en Ada:** Ada elimina la ambigüedad eliminando la posibilidad estructural de que quede colgado. Obliga a que cada estructura condicional se cierre explícitamente mediante la palabra clave end if;. Además, utiliza elsif para cadenas de selección mutuamente excluyentes.

> - **Solución en Python:** Python prescinde de palabras clave de cierre o llaves, y resuelve el problema mediante la indentación obligatoria. La alineación vertical exacta de la palabra clave else determina inequívocamente a qué nivel de if pertenece.

#### Ejercicio 6: ¿Cuál es la construcción para expresar múltiples selección que implementa C? ¿Trabaja de la misma manera que la de Pascal, ADA o Python? 

> Evalúa una expresión que obligatoriamente debe devolver un tipo ordinal (valores discretos con un orden claro, como enteros int, caracteres char o enumerados enum). No permite evaluar floats, strings ni estructuras complejas. Compara el resultado de la expresión secuencialmente con constantes literales definidas en cada cláusula case. 
> No, no trabajan de la misma manera. Cada uno de estos lenguajes introduce diferencias semánticas muy importantes, principalmente orientadas a mejorar la seguridad o la flexibilidad del flujo de control

#### Ejercicio 7: Sea el siguiente código: 

    var i, z:integer; 
    Procedure A; 
    begin 
    i:= i + 1; 
    end; 
    begin 
    z:=5; 
    for i:=1..5 do 
    begin 
        z:=z*5; 
        A; 
        z:=z + i; 
    end; 
    end;

#### a- Analice en las versiones estándar de ADA y Pascal, si este código puede llegar a traer problemas. Justifique la respuesta. 
> En **Pascal**, el estanda prohíbe explícitamente que la variable de control de un bucle for sea modificada dentro del cuerpo del mismo, ya sea de forma directa o indirecta (como ocurre acá a través de la llamada al procedimiento A). En **ADA**, No trae problemas de ejecución ni ciclos infinitos, pero no hace lo que un programador de Pascal esperaría. En Ada, la variable de control de un bucle for es implícitamente declarada por el propio bucle y nace con la propiedad de ser una constante inmutable dentro de ese bloque. Además, esta declaración local produce un fenómeno de ocultamiento (shadowing) sobre cualquier variable externa con el mismo nombre.

#### b- Comente qué sucedería con las versiones de Pascal y ADA, que Ud. utilizó. 

> - En **Pascal Like**, si se quisiera hacer i := i + 1 directamente dentro del bucle, el compilador lo frenaría con un error ("Illegal assignment to for-loop variable"). Sin embargo, al estar oculto dentro de A, el compilador no realiza un análisis estático inter-procedural completo y lo permite. 
> - En **ADA**, compila y ejecuta perfectamente siguiendo el estándar. El bucle iterará exactamente 5 veces porque GNAT protege la variable de control local del bucle aislando la modificación de la variable global.

#### Ejercicio 8: Sea el siguiente código en Pascal:

    var puntos: integer; 
    begin 
    ... 
    case puntos 
    1..5: write(“No puede continuar”); 
    10:write(“Trabajo terminado”) 
    end; 
    .. 
#### Analice, si esto mismo, con la sintaxis correspondiente, puede trasladarse así a los lenguajes ADA, C. ¿Provocaría error en algún caso? Diga cómo debería hacerse en cada lenguaje y explique el por qué. Codifíquelo.

> Sí,en ADA hay error de compilación. Ada exige de forma estricta la regla de Exhaustividad en su estructura case. 
> Si, en C hay error de sintaxis. El estándar de C (ANSI/ISO C) no soporta rangos usando la sintaxis 1..5 (ni ninguna otra nativa) dentro de un switch.

#### Ejercicio 9: Qué diferencia existe entre el generador YIELD de Python y el return de una función. De un ejemplo donde sería útil utilizarlo. 

> La diferencia fundamental radica en el manejo del flujo de control y en la persistencia del Registro de Activación (RA) en la memoria de ejecución.
> - `return` (Finalización Absoluta): Cuando una función ejecuta un return, esta termina definitivamente.
> - `yield` (Suspensión Temporal / Evaluación Perezosa): La palabra clave yield transforma a la función en un Generador. Cuando se alcanza un yield, la función devuelve el valor especificado al llamador, pero no se destruye.

#### Ejercicio 10: Describa brevemente la instrucción map en javascript y sus alternativas.

> `Array.prototype.map()` es un método de orden superior (higher-order function) fuertemente ligado al paradigma funcional. map itera sobre un arreglo y aplica una función de transformación (callback) a cada uno de sus elementos. Su característica semántica principal es que es una operación pura y no mutable: no altera el arreglo original, sino que genera y devuelve un nuevo arreglo con exactamente la misma longitud, pero con los valores modificados.

#### Ejercicio 11: Determine si el lenguaje que utiliza frecuentemente implementa instrucciones para el manejo de espacio de nombres. Mencione brevemente qué significa este concepto y enuncie la forma en que su lenguaje lo implementa. Enuncie las características más importantes de este concepto en lenguajes como PHP o Python.

> Un ***Espacio de Nombres*** es un contenedor abstracto (un contexto semántico) diseñado para agrupar e identificar un conjunto de identificadores (nombres de variables, funciones, clases, etc.). Su propósito principal es evitar colisiones de nombres en proyectos medianos o grandes, permitiendo que existan elementos con el mismo nombre en diferentes módulos sin que el compilador o intérprete los confunda.
> - ***Python*** sí implementa espacios de nombres de forma nativa y omnipresente. En Python, los espacios de nombres se modelan directamente mediante Módulos (archivos .py) y Paquetes (directorios que agrupan módulos).
> - A diferencia de Python, ***PHP*** utiliza una palabra clave específica (namespace) al inicio del archivo para definir lógicamente a qué espacio pertenece, independientemente de dónde esté guardado físicamente el archivo.