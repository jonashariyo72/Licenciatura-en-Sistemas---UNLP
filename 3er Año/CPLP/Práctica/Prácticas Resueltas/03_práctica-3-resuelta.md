# Conceptos y Paradigmas de Lenguajes de Programación  2026 
# Práctica Nro 3 - Semántica 


### Objetivo:  Interpretar el concepto de semántica de los lenguajes de programación.  


### Ejercicio 1: ¿Qué define la semántica? 

> La ***semántica*** describe el significado de los símbolos, palabras y frases de un lenguaje, ya sea natural o informático. En el contexto de la programación, define específicamente el significado de los programas que ya son sintácticamente válidos o correctos. Mientras que la *sintaxis* se ocupa de la "forma" o estructura (cómo se compone el código), la ***semántica*** se encarga de determinar qué es lo que el programa realmente hace o cómo se comporta.

### Ejercicio 2:  
### a. ¿Qué significa compilar un programa? 
> Compilar consiste en traducir un programa escrito en un lenguaje de alto nivel (llamado lenguaje fuente) a un lenguaje que entienda la computadora, generalmente lenguaje de máquina (llamado programa objeto). Este proceso de traducción se realiza de manera completa antes de la ejecución del programa.

### b. Describa brevemente cada uno de los pasos necesarios para compilar un programa. 

> 1. ***Análisis Léxico (Scanner):*** Lee el programa fuente carácter por carácter y agrupa las secuencias en componentes léxicos llamados tokens (palabras clave, identificadores, operadores).

> 2. ***Análisis Sintáctico (Parser):*** Toma los tokens y verifica si cumplen con las reglas gramaticales del lenguaje, construyendo un árbol sintáctico o de derivación.

> 3. ***Análisis Semántico:*** Verifica que el programa tenga un significado válido (ej. tipos compatibles, variables declaradas) y genera un árbol sintáctico atribuido.

> 4. ***Generación de Código Intermedio:*** Traduce el programa a una representación independiente de la arquitectura (como el código de tres direcciones) para facilitar la optimización.

> 5. ***Optimización de Código: (Opcional)*** Mejora el código intermedio para que sea más rápido o ocupe menos memoria.

> 6. ***Generación de Código Final (Objeto):*** Produce las instrucciones específicas para la máquina destino.

> 7. ***Enlace (Linker) y Carga (Loader):*** Combina distintos módulos compilados y bibliotecas en un ejecutable y lo carga en memoria para su uso.

### c.¿En qué paso interviene la semántica y cual es su importancia dentro de la compilación?

>   La semántica interviene en la fase de ***Análisis Semántico (Semántica Estática)***. Su importancia radica en que es el "puente" que asegura que las estructuras sintácticamente correctas tengan realmente sentido y consistencia según las reglas del lenguaje, detectando errores que el análisis sintáctico no puede ver, como el uso de variables no declaradas o la incompatibilidad de tipos de datos.

### Ejercicio 3: Con respecto al punto anterior ¿es lo mismo compilar un programa que interpretarlo? Justifique su respuesta mostrando las diferencias básicas, ventajas y desventajas de cada uno. 

> No es lo mismo. Un ***intérprete*** traduce y ejecuta el programa sentencia por sentencia durante el tiempo de ejecución, mientras que un ***compilador*** traduce todo el programa a código objeto antes de ejecutarlo.

| Característica | ***Compilación*** | ***Interpretación***| 
| :--- | :---: | :---: | 
| **Momento de traducción** | Previo a la ejecución | Durante la ejecución |
| **Velocidad de ejecución** | Más rápida, ya que el hardware lee directamente lenguaje objeto | Más lenta, debido a la decodificación constante de sentencias |
| **Detección de errores**|  Muchos errores se detectan antes de correr el programa | Los errores aparecen en el momento en que se ejecuta la sentencia errónea | 
| **Uso de memoria**| 	Solo requiere el ejecutable en memoria durante la ejecución| Requiere el intérprete, el código fuente y las estructuras dinámicas simultáneamente | 
| **Privacidad del código** | El código fuente no necesita ser público |  El código fuente suele ser público para poder interpretarse  |

### Ejercicio 4: Explique claramente la diferencia entre un error sintáctico y uno semántico. Ejemplifique cada caso. 

> ***Error Sintáctico:*** Es un error en la ***forma o estructura*** del programa. Ocurre cuando el código no respeta las reglas gramaticales (BNF/EBNF) del lenguaje. **Ejemplo**: En C, olvidar un punto y coma al final de una sentencia (x = 5) o dejar un paréntesis sin cerrar en un if.

>***Error Semántico:*** Es un error en el ***significado o lógica*** del uso de las construcciones, a pesar de que la estructura escrita sea "correcta" gramaticalmente. **Ejemplo**: Intentar sumar un entero con una cadena de texto en un lenguaje fuertemente tipado como Java (int x = 5 + "hola";) o intentar usar una variable y que nunca fue declarada previamente.

### Ejercicio 5: Sean los siguientes ejemplos de programas. Analice y diga qué tipo de error se produce (Semántico o Sintáctico) y en qué momento se detectan dichos errores (Compilación o Ejecución). Aclaración: Los valores de la ayuda pueden ser mayores.

### a)  Pascal 

    Program P 

    var 5: integer; 
    var a: char; 

    Begin 
    
    for i:=5 to 10 do begin 
    
    write(a); 
    
    a=a+1; 
    
    end; 

    End. 
 
Ayuda: Sintáctico 2, Semántico 3

> - El `a=a+1;` es un ***error semántico*** porque hace una operación aritmética y `a` es un `char`. Es un error de *compilación*
> - Además, el `a=a+1;` es un ***error sintáctico*** porque la asignación es con `:=`. Es un error de *compilación*.
> `var 5: integer;` no es válido, es un ***error sintáctico***, no se le puede asignar un número a un nombre de variable. Es un error de *compilación*.
> - `write(a);`quiere imprimir `a` pero no `a` no está inicializada, es un ***error semántico***. Es un error de *ejecución*.
> - La variable `i` del for no está inicializada, es un ***error semántico***. Es un error de *compilación*

### b) Java: 


    public String tabla(int numero, arrayList <Boolean> listado)  { 
        
        String result = null; 
        
        for(i = 1; i < 11; i--) { 
            
            result += numero + "x" + i + "=" + (i*numero) + "\n";  
            
            listado.get(listado.size()-1)=(BOOLEAN) numero>i;  
        } 
     
     return true; 
    
    } 

Ayuda: Sintácticos 4, Semánticos 3, Lógico 1

> - Devuelve `true` y debería devolver un `string`, es un ***error semántico***. Es un error en *compilación.*
> - `for(i = 1; i < 11; i--)` es un error ***lógico*** por quedaría en un bucle infinito. Es un error en *ejecución*.
> - El `i`del for no está inicializado. Es un ***error semántico***. Es un error de *compilación*.
> - `String result = null;` es un ***error sintáctico***. Es un error de *ejecución*.
> - `listado.get(listado.size()-1)=` le quiere asignar algo a un getter, es un ***error sintáctico***. Es un error de *compilación*.
> - `(listado.size()-1)` le pide el size en la posición -1 , que puede terminar dándole la posición -1 si la lista está vacía, es error ***semántico***. Es un error en *ejecución*.
> - `(BOOLEAN)` debería ir en minúscula, es un error ***sintáctico***. Se ve en *compilación*.
> - En `arrayList` la a de array debería ser A. Es un error ***sintáctico*** y de *compilación*.

### c) C 

    # include <stdio.h> 
    int suma; /* Esta es una variable global */ 
    int main() 
    {  int indice; 
        encabezado; 
        for (indice = 1 ; indice <= 7 ; indice ++) 
        cuadrado (indice); 
        final(); Llama a la función final */ 
        return 0; 
    }

    cuadrado (numero) 
    int numero; 
    {   int numero_cuadrado; 
        numero_cuadrado == numero * numero; 
        suma += numero_cuadrado; 
        printf("El cuadrado de %d es %d\n", 
        numero, numero_cuadrado); 
    } 
 
Ayuda: Sintácticos 2, Semánticos 6 

> - `Llama a la función final */` es un error ***sintáctico***, no abre el comentario. Es un error en *compilación*.
> - `encabezado;` está suelto y no se entiende. Es un error ***sintáctico***. Error en *compilación*.
> - `cuadrado()` y `final()` deberían estar declarados como funciones arriba del main. Es un error ***sintáctico*** y de *compilación*.
> - `numero_cuadrado == numero * numero;` es un error ***sintáctico*** porque hace la comparación y no hay ningún condicional. Es error en *compilación*.
> - `numero` está en la función cuadrado como variable local y como parámetro de la función, es un error ***sintáctico*** y de *ejecución*.
> - `final()` se lo llama en el main y no está ni declarado ni definida. Error ***semántico*** y de *ejecución*.
> - la función `cuadrado (numero)` está mal definida, falta el tipo que retorna y los tipos de los parámetros. Error ***sintáctico*** y de *compilación*.




### d)Python 

    #!/usr/bin/python 
    print "\nDEFINICION DE NUMEROS PRIMOS" 
    r = 1      
    while r = True:      
        N = input("\nDame el numero a analizar: ") 
        i = 3 
        fact = 0 
        if (N mod 2 == 0) and (N != 2):  
            print "\nEl numero %d NO es primo\n" % N 
        else: 
            while i <= (N^0.5): 
                if (N % i) == 0: 
                    mensaje="\nEl numero ingresado NO es primo\n" % N 
                    msg = mensaje[4:6]  
                    print msg 
                    fact = 1 
                i+=2 
            if fact == 0: 
                print "\nEl numero %d SI es primo\n" % N 
        
        r = input("Consultar otro número? SI (1) o NO (0)--->> ")

Ayuda: Sintácticos 2, Semánticos 3

> - El `print msg` es un error ***sintáctico***, faltaría las comillas o que sea una variable (). Es un error de *compilación*.
> - El `(N mod 2 == 0)`es un error ***sintáctico***, no existe el mod en Python como palabra reservada. Es un error de *compilación*.
> - El `print "\nEl numero %d NO es primo\n" % N` es un error ***semántico***, utiliza `%N` como placeholder y no hay `%d. Es un error en *ejecución*.
> - `N = input("\nDame el numero a analizar: ")` es un error ***semántico***, no pide en el input el tipo int para que no ponga otro tipo. Error en *ejecución*.
> - `while i <= (N^0.5):` es un error ***sintáctico*** porque no existe el operador `^`. Error en *compilación*.

### e) Ruby 

    def ej1 
    Puts 'Hola, ¿Cuál es tu nombre?' 
    nom = gets.chomp 
    puts 'Mi nombre es ', + nom 
    puts 'Mi sobrenombre es 'Juan'' 
    puts 'Tengo 10 años' 
    meses = edad*12    
    dias = 'meses' *30                                          
    hs= 'dias * 24' 
    puts 'Eso es: meses + ' meses o ' + dias + ' días o ' + hs + ' horas' 
    puts 'vos cuántos años tenés' 
    edad2 = gets.chomp 
    edad = edad + edad2.to_i 
    puts 'entre ambos tenemos ' + edad + ' años'    
    puts '¿Sabes que hay ' + name.length.to_s + ' caracteres en tu nombre, ' + name + '?' 
    end 
 
Ayuda: Semánticos +4 

> - `Puts` debería ir con minúscula. Error ***sintáctico*** y de *compilación*.
> -  `puts 'Mi nombre es ', + nom` No se puede concatenar teniendo `+` y  `,` juntos, es un error ***sintáctico*** y de *compilación*.
> - `puts 'Mi sobrenombre es 'Juan''` están mal usadas las comillas, es un error ***semántico*** y de *compilación*.
> -  La variable `name` no está definida. Es un error ***semántico*** y de *ejecución*.

### Ejercicio 5: Dado el siguiente código escrito en pascal. Transcriba la misma funcionalidad de acuerdo al lenguaje que haya cursado en años anteriores. Defina brevemente la sintaxis (sin hacer la gramática) y semántica para la utilización de arreglos y estructuras de control del ejemplo.

    Procedure ordenar_arreglo(var arreglo: arreglo_de_caracteres;cont:integer); 
    var 
        i:integer; ordenado:boolean; 
        aux:char; 
    begin 
        repeat 
        ordenado:=true; 
        for i:=1 to cont-1 do 
        if ord(arreglo[i])>ord(arreglo[i+1]) 
            then begin 
                aux:=arreglo[i]; 
                arreglo[i]:=arreglo[i+1]; 
                arreglo[i+1]:=aux; ordenado:=false 
                end; 
        until ordenado; 
    end;

**Observación: Aquí sólo se debe definir la instrucción y qué es lo que hace cada una; detallando alguna particularidad del lenguaje respecto de ella. Por ejemplo el for de java necesita definir una variable entera, una condición y un incremento para dicha variable.**

> **Lenguaje: Python**

    def ordenar_arreglo (arreglo ,cont):
        cond = True
        while (cond):
            ordenado = True
            for i in range (cont-1): 
                if arreglo[i] > arreglo[i+1]:
                    aux = arreglo[i]
                    arreglo[i] = arreglo[i+1]
                    arreglo[i+1] = aux
                    ordenado = False  
        if (ordenado):
            break

> - **Sintaxis en Python:**
> - ***Arreglos (Listas):*** Se definen entre corchetes []. El acceso a elementos se realiza mediante un índice entero entre corchetes: lista[indice].
> - ***Estructuras de Control:***
>   - ***while:*** Palabra reservada seguida de una condición y dos puntos :. El bloque de código debe estar indentado.
>   - ***for..in range():*** Estructura para iterar sobre una secuencia de números.
>   - ***if:*** Condición seguida de : y bloque indentado.

> - **Semántica en Python:**
> - ***Arreglos:*** Las listas son mutables y dinámicas. El pasaje de listas a funciones es por referencia (similar al var de Pascal), por lo que los cambios dentro de la función afectan a la lista original.
> - ***Estructuras de Control:***
>   - ***while:*** Ejecuta el bloque mientras la condición sea verdadera.
>   - ***break:*** Finaliza la ejecución del bucle más cercano de forma inmediata.
>   - ***range(n)***: Genera una secuencia desde 0 hasta n-1. Es fundamental para evitar errores de semántica dinámica por acceso a índices inexistentes.

### Ejercicio 6: Explique cuál es la semántica para las variables predefinidas en lenguaje Ruby self y nil. ¿Qué valor toman; cómo son usadas por el lenguaje?

> La variable `self` hace referencia al ***objeto receptor actual.*** Actúa como un identificador especial que permite a un objeto referenciarse a sí mismo para acceder a sus propias variables de instancia o invocar sus propios métodos desde su interior.

> La variable `nil` representa la ***ausencia de valor o un estado "nulo"***. Se utiliza como el ***valor por defecto*** para inicializr variables o posiciones en estructuras de datos que aún no han sido asignadas por el programador.

### Ejercicio 7: Determine la semántica de null y undefined para valores en javascript.¿Qué diferencia hay entre ellos?

> El `undefined` reperesenta el estado de una variable que ha sido declaada pero a la cual ***aún no se le ha asignado un valor*** por parte del programador. **JavaScript** utiliza  como su estrategia de inicialización por defecto `undefined`.

> `null` es un ***R-valor*** (valor codificado) que ***representa la ausencia intencional de un objeto o valor*** `null`. Se utiliza para indicar que una variable de tipo referencia no apunta a ningún objeto en el "heap" o memoria dinámica.

### Ejercicio 8: Determine la semántica de la sentencia break en C, PHP, javascript y Ruby. Cite las características más importantes de esta sentencia para cada lenguaje 

> La sentencia `break` es una estructura de control de ***salida prematura***. Según las fuentes, su comportamiento varía según el contexto, aunque los materiales se centran principalmente en el lenguaje C.

> - ***En C (y C++ / Java):***
>   - ***En estructuras de selección (switch):*** Se utiliza para finalizar una rama del caso. Sin el , la ejecución "cae" (fall-through) hacia el siguiente caso, lo que puede provocar ejecuciones no deseadas.
>   - ***En bucles (while, for, do):*** Termina completamente la ejecución del bucle más cercano que la contiene, transfiriendo el control a la instrucción inmediatamente posterior al bucle.
>   - ***Característica principal:*** Permite evitar el uso de banderas booleanas complejas para salir de una iteración.

> - ***En PHP, JavaScript y Ruby:***
> - Los fragmentos de las fuentes proporcionadas no detallan las particularidades semánticas del  para PHP, JavaScript o Ruby de forma específica. Sin embargo, mencionan que lenguajes como *Python y Java* (que comparten raíces con estos) utilizan el  para salir de bucles de forma similar a C. En Ada, una funcionalidad equivalente se logra con la sentencia `exit`.

### Ejercicio 9: Defina el concepto de ligadura y su importancia respecto de la  semántica de un programa. ¿Qué diferencias hay entre ligadura estática y dinámica? Cite ejemplos (proponer casos sencillos)

> La ***ligadura*** es el proceso de ***asociar un nombre*** (identificador) con un atributo o una entidad del programa (como su tipo, valor o ubicación de memoria). Es el momento exacto en que un atributo toma un valor determinado. Es el concepto central en la definición de la ***semántica*** de los lenguajes. Los programas trabajan con entidades que solo pueden utilizarse una vez que sus atributos han sido establecidos mediante una ligadura.

| Característica | ***Ligadura Estática*** | ***Ligadura Dinámica***| 
| :--- | :---: | :---: | 
| **Momento de atadura** | Ocurre antes de la ejecución | Durante la ejecución |
| **Estabilidad** | Una vez establecida, no se puede modificar| Es redefinible o modificable mientras corre el programa |

### Ejemplos

> - ***Ligadura Estática (Tipo en C):***
>   -  En la declaración , el atributo Tipo (entero) se liga al nombre  durante la compilación. Esta relación no puede cambiar durante la ejecución;  siempre será un enteroint x;xx.

> - ***Ligadura Dinámica (Valor en ejecución):***
>   - En la asignación , el atributo Valor (10) se liga a la variable  en tiempo de ejecución. Si luego el programa ejecuta, esa ligadura cambia dinámicamentex = 10;x = 15;.

> - ***Ligadura Dinámica de Métodos (Smalltalk/C++ virtual):***
>   - En lenguajes orientados a objetos, cuando se llama a un método de un objeto polimórfico, la decisión de qué código exacto ejecutar se toma en ejecución basándose en el tipo real del objeto en ese momento.