# Conceptos y Paradigmas de Lenguajes de Programación  2026 
# Práctica Nro 9 - Excepciones


## Objetivo:  Conocer e interpretar los distintos modelos de excepciones que implementan los lenguajes de programación. 

### Ejercicio 1: Explique claramente a qué se denomina excepción
> Es una condición inesperada, inusual o anómala que ocurre durante la ejecución de un programa y que no puede ser manejada en el contexto local donde se genera.

### Ejercicio 2: ¿Qué debería proveer un lenguaje para el manejo de las excepciones? ¿Todos los lenguajes lo proveen? 
> Si un lenguaje da soporte formal a las excepciones, debe definir sintáctica y semánticamente: cómo se declaran/definen, cómo se lanzan de forma explícita, bajo qué ámbito se capturan mediante controladores (handlers), cómo se propagan si no hay un manejador local y a dónde regresa el flujo de control una vez atendidas.

### Ejercicio 3: ¿Qué ocurre cuando un lenguaje no provee manejo de excepciones? ¿Se podría simular?  Explique cómo lo haría
> Simulación ante la ausencia de soporte: Cuando un lenguaje carece de un sistema nativo de excepciones (como el estándar clásico de C), los errores se deben mitigar de forma manual mediante efectos colaterales, tales como: Retornar códigos numéricos de estado especiales al finalizar cada función (ej. -1 o NULL) o Modificar variables o flags globales de error (como la variable estándar errno en C) que la rutina llamadora está obligada a inspeccionar de inmediato.

### Ejercicio 4: Cuando se termina de manejar la excepción, la acción que se toma luego es importante. Indique 
#### 01. ¿Qué modelos diferentes existen en este aspecto? 

> Existe el ***Modelo de Reasunción*** y ***Modelo de Terminación***.
#### 02. Dé ejemplos de lenguajes que utilizan cada uno de los modelos presentados anteriormente. Por cada uno responda respecto de la forma en que trabaja las excepciones. 
#### a. ¿Cómo se define? b. ¿Cómo se lanza? c. ¿Cómo se maneja? d. ¿Cuál es su criterio de continuación? 

***PL/I (Program Language One)***
- Modelo: Reasunción por defecto. 
- Sintaxis: Declaración del manejador mediante ON CONDITION (NombreExcepcion) BEGIN ... END;. Lanzamiento explícito con SIGNAL CONDITION (NombreExcepcion);.  - - Ligadura: Dinámica. Una excepción queda asociada de forma operativa al último manejador que se haya ejecutado en la línea temporal del programa (se gestiona mediante una pila de manejadores activos).  

***ADA***
- Modelo: Terminación.  Sintaxis: Declaración: e: exception;. Lanzamiento: raise e;. Captura: bloques exception when e => ... situados al final de las unidades.  
- Particularidades: La asociación entre una excepción y su manejador es estrictamente determinística (por coincidencia directa de nombres). Para simular un comportamiento similar al de reasunción, ADA obliga al programador a envolver la línea crítica dentro de un bloque interno explícito (declare begin exception end;), aislando así la destrucción del entorno.  
- Excepciones Built-in: Constraint_Error (límites de arrays, rangos de subtipos), Program_Error (violación de reglas como una función que no retorna valor), Storage_Error (falta de memoria en el heap), Tasking_Error (errores en hilos/concurrencia), y Name_Error (ficheros inexistentes).  

***C++*** 
- Modelo: Terminación.  
- Sintaxis: Bloques estructurados try { ... } catch (Tipo e) { ... }. Lanzamiento por medio de throw.  
- Especificación de Interfaz: Permite documentar qué excepciones propaga una rutina en su encabezado. Un bloque vacío en la firma (void rutina() throw()) garantiza semánticamente que la función no propagará ninguna excepción hacia el exterior. Si la cláusula se omite por completo, significa que la rutina puede propagar cualquier excepción sin restricciones. 

***CLU*** 
- Modelo: Terminación estricta.  
- Sintaxis: Los procedimientos declaran de forma obligatoria las excepciones que pueden emitir en su firma usando signals (error1). Se lanzan mediante signal error1 y se capturan externamente con la palabra clave when adherida a sentencias.  
- Error Global: Si ocurre una falla no interceptada en el entorno inmediato, se transforma en la excepción predefinida de colapso llamada failure. 

***Java***
- Modelo: Terminación.  
- Jerarquía de Objetos: Toda excepción es un objeto derivado de la clase raíz Throwable. Se subdivide principalmente en Error (fallos críticos del sistema e irrecuperables de la JVM) y Exception (anomalías de la lógica de la aplicación).  
- Sintaxis y Cláusulas: Utiliza el control quíntuple: try, catch, throw, throws y finally.  
- La cláusula throws en la firma del método es de carácter obligatorio para todas las excepciones de tipo comprobadas (checked exceptions).  
- El bloque finally garantiza la ejecución de sus líneas de código internas de forma mandatoria, independientemente de si el flujo del try fue exitoso o si se disparó y capturó una excepción en el catch.

***Python*** 
- Modelo: Terminación.  
- Sintaxis: Bloques flexibles try: y capturas mediante cláusulas except NombreExcepcion:.  
- Flujo: Si la excepción lanzada coincide en tipo con la declaración del except, se procesa su bloque interno y la ejecución continúa limpiamente debajo de toda la estructura try-except. Si no hay coincidencia, delega la resolución de forma dinámica hacia los bloques try externos.  

***PHP***
- Modelo: Terminación.  
- Sintaxis: Bloques tradicionales try { ... } catch (SubclaseException $e) { ... }.  
- Particularidad: Es de carácter obligatorio que cualquier objeto lanzado con throw sea una instancia directa o heredada de la interfaz/clase base Exception. Intentar lanzar un tipo primitivo o un objeto ajeno a esta jerarquía interrumpe el motor de ejecución provocando un Fatal Error de PHP.

***Rust***
- Modelo Alternativo: No implementa el sistema tradicional de excepciones basado en capturas try-catch ni bifurcaciones ocultas del flujo de ejecución.  
- Manejo de Errores Bicéfalo: Rust divide los problemas en dos naturalezas operacionales:  
- Errores Irrecuperables: Situaciones críticas que comprometen la seguridad del sistema (ej. acceder a un índice fuera de rango de un vector). Se gestionan mediante la macro panic!(), la cual imprime un mensaje detallado de error, limpia (unwind) la memoria de la pila y aborta el proceso de inmediato.  
- Errores Recuperables: Fallos predecibles y cotidianos de la lógica (ej. intentar abrir un archivo que no existe). En lugar de lanzar una excepción, las funciones devuelven de manera normal un tipo de dato enumerado genérico llamado Result<T, E>. Este contiene dos variantes posibles: Ok(T) que transporta el valor de éxito, o Err(E) que transporta el objeto con el detalle del error, obligando al programador a evaluar explícitamente ambas alternativas mediante pattern matching (match).

#### 03. ¿Cuál de esos modelos es más inseguro y por qué? 
> El ***Modelo de Terminación*** es considerado el enfoque más limpio y seguro en la ingeniería de software actual.  

### Ejercicio 5: La propagación de los errores, cuando no se encuentra ningún manejador asociado, no se implementa igual en todos los lenguajes. Realice la comparación entre el modelo de Java, Python y  PL/1, respecto a este tema. Defina la forma en que se implementa en un lenguaje conocido por Ud. 

***Java (Modelo de Terminación con Propagación Dinámica y Verificación Estática)***
Mecanismo: Java utiliza una propagación dinámica basada estrictamente en la pila de llamadas (call stack). Si el método actual no captura la excepción, su Registro de Activación (RA) se destruye de forma abrupta (Modelo de Terminación), liberando sus variables locales, y el control junto con el objeto de la excepción se transfieren al método llamador (el que invocó a la rutina actual). Este proceso se repite hacia atrás en la pila histórica de ejecuciones.4

***Python (Modelo de Terminación con Propagación Dinámica Pura)***
Mecanismo: Al igual que Java, Python propaga las excepciones de forma dinámica a través de la pila de llamadas en tiempo de ejecución. Cuando un error ocurre y no hay un bloque except local, el intérprete congela y destruye el entorno de la función actual, y busca un bloque try-except contenedor en la función que realizó la invocación.

***PL/1 (Modelo de Reasunción con Ligadura Dinámica de Manejadores)***
Mecanismo: El comportamiento de PL/1 difiere radicalmente de los dos anteriores porque implementa el Modelo de Reasunción y maneja una pila interna de manejadores activos.


### Ejercicio 6: Sea el siguiente programa escrito en Pascal 

    ... 
    Procedure Manejador; 
    Begin ...   end; 
    Procedure P(X:Proc); 
    begin 
    .... 
    if Error then X; 
    .... 
    end; 
    Procedure A; 
    begin 
    .... 
    P(Manejador); 
    …. 
    end; 
    .... 

### ¿Qué modelo de manejo de excepciones está simulando? ¿Qué necesitaría el programa para que encuadre con los lenguajes que no utilizan este modelo? Justifique la respuesta. 

> El programa está simulando el manejo de excepciones de tipo **Reasunción**. Se utiliza un manejador y luego de la excepción el programa sigue su curso normal. Para encuadrar con el modelo de **Terminación** debería por ejemplo colocar un `exit` para terminar el bloque que genera la excepción.

### Ejercicio 7: Sea el siguiente programa escrito en Pascal: 

    Program Principal; 
    var x:int;  b1,b2:boolean; 

    Procedure P (b1:boolean); 
            var x:int; 
            Procedure Manejador1 
                            begin 
    x:=x + 1;      
    end; 
                        begin 
    x:=1;   
    if b1=true then Manejador1;    
    x:=x+4; 
    end; 

    Procedure Manejador2; 
    begin 
    x:=x * 100; 
    end; 

    Begin 
    x:=4;    
    b2:=true;    
    b1:=false;  
    if b1=false then Manejador2;  
    P(b);  
    write (x); 
    End. 

### a) Implemente este ejercicio en PL/1 utilizando manejo de excepciones 

    PRINCIPAL: PROCEDURE OPTIONS (MAIN);
        DECLARE X FIXED BINARY;
        DECLARE (B1, B2) BIT(1);
        
        /* Declaración de las condiciones (excepciones) */
        DECLARE EXCEPCION1 CONDITION;
        DECLARE EXCEPCION2 CONDITION;

        P: PROCEDURE (B1_PARAM);
            DECLARE B1_PARAM BIT(1);
            DECLARE X FIXED BINARY; /* Oculta al X global */
            
            /* Se define el Manejador 1 asociado a la variable local X */
            ON CONDITION (EXCEPCION1) BEGIN
                X = X + 1;
            END;
            
            X = 1;   
            IF B1_PARAM = '1'B THEN 
                SIGNAL CONDITION (EXCEPCION1); /* Reasunción: vuelve a la línea siguiente */
            X = X + 4; 
        END P;

        /* Cuerpo del Programa Principal */
        /* Se define el Manejador 2 asociado a la variable global X */
        ON CONDITION (EXCEPCION2) BEGIN
            X = X * 100;
        END;

        X = 4;    
        B2 = '1'B;    
        B1 = '0'B;  
        
        IF B1 = '0'B THEN 
            SIGNAL CONDITION (EXCEPCION2); /* Reasunción: tras ejecutar el bloque, vuelve */
            
        /* Nota: El código original dice P(b); asumimos que pasa b2 o b1 según la lógica. 
        Pasamos B2 para mantener consistencia */
        CALL P(B2);  
        
        PUT LIST (X); 
    END PRINCIPAL;

### b) ¿Podría implementarlo en JAVA utilizando manejo de excepciones? En caso afirmativo, realícelo. 

    public class Principal {
        // Variable global (atributo de clase)
        static int x; 
        static boolean b1, b2;

        // Definición de excepciones a medida
        static class ExcepcionE1 extends Exception {}
        static class ExcepcionE2 extends Exception {}

        public static void p(boolean b1Param) {
            int xLocal = 0; // Equivalente al var x:int de P
            
            try {
                xLocal = 1;   
                if (b1Param) {
                    throw new ExcepcionE1(); // Dispara la excepción
                }
                // En Java, si entra al IF, esta línea de abajo se perdería en un try común.
                // Para simular que se ejecuta igual, el catch debe contener la lógica de continuación.
            } catch (ExcepcionE1 e) {
                // Manejador 1 ejecutándose en el entorno del xLocal
                xLocal = xLocal + 1; 
            }
            
            // Al ponerse fuera del bloque try-catch, garantizamos que se ejecute 
            // tanto si se lanzó la excepción (simulando reasunción) como si no.
            xLocal = xLocal + 4; 
        }

        public static void main(String[] args) {
            x = 4;    
            b2 = true;    
            b1 = false;  
            
            try {
                if (!b1) {
                    throw new ExcepcionE2();
                }
            } catch (ExcepcionE2 e) {
                // Manejador 2 ejecutándose sobre el X global
                x = x * 100; 
            }
            
            // El flujo continúa secuencialmente hacia abajo (Terminación limpia del bloque)
            p(b2);  
            
            System.out.println(x); // Imprimirá 400
        }
    }

### Ejercicio 8: Sean los siguientes, procedimientos de un programa escrito en JAVA: 

    Public static void main (String[] argos){ 
            Double array_doubles[]= new double[500]; 
            for (int i=0; i<500; i++){ 
                        array_doubles[i]=7*i; 
            } 
            for (int i=0 ; i<600 ; i=i+25){ 
                    try{ 
                            system.out.println(“El elemento en “+ i + ” es “ + acceso_por_indice (array_doubles,i)); 
                    }  
                    catch(ArrayIndexOutOfBoundsException e){ 
                            system.out.println(e.tostring()); 
                    }  
                    catch(Exception a){ 
                            system.out.println(a.tostring()); 
                    }    
                    finally{ 
                            system.out.println(“sentencia finally”); 
                    } 
            } 
    } 
    
    Public static double acceso_por_indice (double [] v, int indice) throws Exception; ArrayIndexOutOfBoundsException{ 
                if ((indice>=0) && (indice<v.length)){ 
                        Return v[indice]; 
                }  
                else{  
                        if (indice<0){ 
                            // caso excepcional 
                            Throw new ArrayIndexOutOfBoundsException(“ el índice” + indice + “ es un número negativo”);
                                         }  
                       else{ 
                         // caso excepcional 
                         Throw new Exception(“ el indice” + indice + “ no es una posición válida”); 
                         } 
               } 
    } 

### a) Analizar el ejemplo y decir qué manejadores ejecuta y en qué valores quedan las variables. JUSTIFIQUE LA RESPUESTA. 

> En primer lugar, hasta se ejecua el for de 25 en 25, hasta que llega al 475 se ejecuta normal entrando al try y devolviendo el índice.
> Para el 500, ya no cumple la condición de ser menor que el tamaño del vector, así que se ejecuta que no es una posición válida.
> Por último, del 525 al 600, tampoco se cumple la condición y se maneja como con el 500. 
> array_doubles: Queda guardado en el Heap de memoria con sus 500 elementos intactos (valores desde 0.0 hasta 3493.0).
> i (del bucle del main): El ciclo termina cuando i toma el valor de 600 (ya que la condición i < 600 da falso y rompe el bucle).

### b) La excepción se propaga o se maneja en el mismo método? ¿Qué instrucción se agrega para poder  propagarla y que lleve información?. 

> La excepción se propaga al programa principal. 
> Instrucciones utilizadas para la propagación:
> - **throw (Acción en ejecución)**: Es la instrucción que se agrega dentro del cuerpo del método para instanciar el objeto de error, inyectarle un mensaje descriptivo de texto como parámetro ("información") y disparar la propagación (ej. throw new Exception(...)).

> - **throws (Declaración en la firma)**: En la cabecera del método se utiliza la palabra clave throws Exception para avisarle obligatoriamente al compilador de Java que este método no resolverá ese error de forma local y delegará la responsabilidad a quien lo invoque.

### ) como modificaría el método “acceso_por_indice” para que  maneje él mismo la excepción. 

> Se le debería agregar un bloque try-catch para que el mismo método maneje la excepción.

### Ejercicio 9: Indique diferencias y similitudes entre Phyton y Java con respecto al manejo de excepciones. 
> - **Similitudes:** Ambos implementan estrictamente el Modelo de Terminación, las excepciones no son simples códigos numéricos ni cadenas de texto, sino objetos reales, Propagación Dinámica, Ambos proveen una estructura para asegurar la liberación de recursos (finally) 

> - **Diferencias:** 
>   - ***Control en compilación:*** Java divide las excepciones en Checked y Unchecked, en Python todas las excepciones son dinámicas 
>   - ***Firma de métodos:*** Java obliga a usar la cláusula throws en el encabezado, Python

### Ejercicio 10: ¿Qué modelo de excepciones implementa Ruby?. ¿Qué instrucciones específicas provee el lenguaje para manejo de excepciones y cómo se comportan cada una de ellas? 
> Ruby implementa el Modelo de Terminación por defecto. Sin embargo, posee una instrucción particular (retry) que le permite emular de manera controlada el Modelo de Reasunción, reiniciando el bloque entero desde el principio.

### Ejercicio 11: Indique el mecanismo de excepciones de javascript

> JavaScript maneja un esquema de excepciones síncronas muy dinámico y flexible, adaptado a su naturaleza de lenguaje interpretado y de tipado débil.
> - Estructura Clásica (try-catch-finally): Utiliza los bloques estructurados tradicionales. El código propenso a fallar se envuelve en un try {}, los errores se interceptan en el catch (error) {} y la liberación de recursos se ubica en un opcional finally {}.

> - Modelo de Continuación: Adopta firmemente el Modelo de Terminación combinando la Propagación Dinámica a través de la pila de llamadas.

> - Tipado Ultra-Dinamico en Lanzamientos (throw): A diferencia de Java o Python, donde estás obligado a lanzar un objeto que herede de una jerarquía de excepciones, el comando throw en JavaScript puede lanzar absolutamente cualquier tipo de dato. Podés lanzar un objeto nativo de error (throw new Error("error")), pero también es semánticamente válido lanzar un número, un String primitivo o un objeto literal a medida.

> - Ausencia de Multi-Catch por Sintaxis: JavaScript no permite definir múltiples bloques catch consecutivos para atrapar diferentes tipos de errores (como sí hace Java o C++). Existe un único bloque catch genérico que recibe el objeto lanzado. Si el programador desea aplicar un comportamiento diferente según el tipo de anomalía, debe discriminarlo manualmente adentro usando el operador instanceof o evaluando propiedades del objeto.