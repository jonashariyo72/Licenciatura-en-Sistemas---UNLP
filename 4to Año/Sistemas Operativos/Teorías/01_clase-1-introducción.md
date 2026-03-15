## Clase 1 - Introducción

# Sistema Operativo

Software intermediario entre el usuario de una computadora y su Hardware. El software necesita procesador y memoria para poder ejecutarse. 

- El SO controla la ejecución de los procesos 
- SO competirá casi de igual a igual con los otros procesos que se estén ejecutando
- El SO puede definirse desde dos perspectivas, la **del usuario** (la más linda) y la **del hardware** (manejador de los recursos y proveedor de abstracciones)
- Desde el lado del usuario queremos que el SO nos proveea abstracción con respecto a la arquitectura de HW 

>Arquitectura
>>Conjunto de instrucciones, organización de memoria, E/S, estructura de bus

- Los programas de aplicación son los "clientes" del SO

***Perspectiva desde la administración de recursos***

- Administra los recursos de HW de uno o más procesos
- Provee un conjutno de servicios a los usuarios del sistema
- Maneja la memoria secundaria y los dispositivos S/O
- Ejecución simultánea de procesos 
- Multiplexación en tiempo (CPU) y en espacio (memoria)

### Objetivos del SO
- Comodidad
	- facilitar el uso del HW
- Eficiencia
	- uso más eficiente de los recursos
- Evolución
	- permitir la introducción de nuevas funciones al sistema sin interferir con funciones anteriores
	- normalmente controlada por los desarrolladores de HW y SW


>>El SO le da razón de ser al HW

Componentes del SO

- Kernel
	- Actúa como una API entre el HW y las aplicaciones
- Shell
	- GUI/CLI
- Herramientas
	- editores, compiladores, librerías, etc.


Normalmente cuando hablamos de SO, hablamos del **Kernel**

---
## Kernel

- Es una porción de código
	- Se encuentra en memoria
	- Se encarga de la administración de los recursos
- Implementa servicios esenciales
	- Manejo de memoria
	- Manejo de la CPU
	- Administración de procesos
	- Comunicación y Concurrencia
	- Gestión de E/S

### ¿Qué es el Kernel Linux?

- Programa que ejecuta programas y gestiona dispositivos de HW
- Sus funciones principales son la administración de la memoria principal y el uso de la CPU
- Es de código abierto a los usuarios (`Kernel/sched.c`)
- En una misma estructura de código fuente se da soporte a todas las arquitecturas
- En un sentido estricto es el SO

Solo con un kernel no hacemos nada. Para comunicarnos con el kernel necesitamos el shell

El código fuente del kernel linux está pensado para poder correr en cualquier arquitectura

- Para facilitar a los procesos acceso seguro al HW se utiliza la interfaz conocida como "llamadas al sistema" (es como una API)
- Cualquier proceso que necesite algo más aparte de lo que tiene en su espacio de direcciones, se lo pedirá al SO, mediante la "API" **system call**
- El kernel gestiona y atiende los requerimientos de los distintos procesos siguiendo un criterio de "equidad"

El Kernel se ejecuta en modo supervisor o privilegiado
- se tiene acceso al conjunto completo de instrucciones que permiten..
	- acceder al HW
	- direccionar la memoria
	- programar la CPU
	- etc..

Los procesos se ejecutan en **modo usuario**
- cuando un proceso requiere acceso al HW, lo hace a través de una llamada al SO


>Un proceso de usuario no puede hacer nada por su propia cuenta

>La capacidad de ejecutar código en modo supervisor o usuario, es provista por el HW que trabaja en conjunto con el SO. 


## Modos de Ejecución

- Define limitaciones en el conjunto de instrucciones que se puede ejecutar en cada modo
	- Cada vez que entra un proceso a la CPU pasa de modo supervisor a usuario
		- acá aparece el concepto de instrucciones privilegiadas (solo en modo supervisor)
	- El bit en la CPU indica el modo actual 
- Interrupción de Clock
	- Se debe evitar que un proceso se apropie de la CPU
	- Por cada interrupción se despierta al Kernel para que determine como seguir
- Protección de memoria
	- Se deben definir límites de memoria a los que puede acceder cada proceso (registro base y límite, paginación, segmentación)
	- De esto se encarga la MMU (traducción de direcciones lógicas a físicas)

>El Kernel delega en el HW algunas funciones, instruyendo al HW diciéndole como debe funcionar

Cuando ocurre algun problema, el HW dispara una interrupción para avisar al Kernel de la ocurrencia de un evento. Se accede al vector de interrupciones y se ejecuta la función correspondiente. El HW introduce en un registro determinado el nro de instrucción que ocurrió y el Kernel determina en base a eso que hacer, llama a la función correspondiente al nro

> Bit de modo
>- Cuando se arranque el sistema, arranca con el bit en modo supervisor
>- Cada vez que comienza la ejecución de un proceso, este bit se DEBE PONER en modo usuario antes de ceder el control al proceso
>- Cuando hay un trap o una interrupción, el bit de modo se pone en modo Kernel 
>	- Son la única forma de pasar a modo Kernel

## Caracterizaciones del Kernel

De acuerdo a su arquitectura de desarrollo podemos caracterizarlos en distintos tipos
- ***Monolíticos***
	- todos los servicios del SO en un solo bloque de código que se ejecutan en modo supervisor
		- por esto es más complejo 
	- posee distintos subsistemas y la funcionalidad de cada uno es accedida directamente desde otro a través de funciones públicas
- ***Microkernel***
	- minimiza la cantidad de código que se ejecuta en modo supervisor con el fin de hacerlo más liviano respecto a un monolítico
	- el kernel solo se encarga gestión de procesos, memoria y dispositivos E/S. El resto ocurre en el espacio de direcciones de los procesos 
- ***Híbrido***
	- combinación entre monolíticos y microkernels
	- tiene el modelo minimalista pero le puedo anexar módulos que no se ejecutarán en modo usuario, sino en modo kernel 
	- se puede cargar y descargar funcionalidad a medida que es necesario
- ***Exokernel*** (kernel de exoesqueleto)
	- ...
- ***Kernel de tiempo real***
	- Están pensados para ejecutar aplicaciones de ejecución crítica
	- ej: si aprieto el botón se lanza un misil
	- ya casi ni se usan