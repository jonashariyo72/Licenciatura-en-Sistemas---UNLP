# SISTEMAS OPERATIVOS -  Práctica 3



## Requisitos 
Para realizar esta práctica se puede usar la misma máquina virtual de la práctica 1 o una de su 
elección si resulta más cómodo (por ejemplo una VM con interfaz gráfica y un IDE). 

## Threading (ULT y KLT) 

### Conceptos Generales

### 1. ¿Cuál es la diferencia fundamental entre un proceso y un thread? 
> Un ***proceso*** es una unidad de ejecución independiente que tiene su propio espacio de direcciones y recursos (no comparten memoria por defecto).

> Un ***thread (hilo)*** es una unidad de ejecución dentro de un proceso que comparte el mismo espacio de direcciones y recursos con otros hilos del mismo proceso.

> La creación y el cambio de contexto entre hilos es mucho más rápido que entre procesos, por eso se los llama "procesos de peso ligero" (LWP).
### 2. ¿Qué son los User-Level Threads (ULT) y cómo se diferencian de los Kernel-Level Threads (KLT)?
> - ***ULT (User-Level Threads):*** Son gestionados íntegramente por una biblioteca de hilos en el espacio de usuario, sin que el kernel sepa de su existencia.

> - ***KLT (Kernel-Level Threads):*** Son gestionados directamente por el sistema operativo. El kernel mantiene una tabla de hilos y decide su planificación.

> Si un ULT realiza una llamada al sistema que bloquea, se bloquea todo el proceso; en cambio, si un KLT se bloquea, el kernel puede planificar otro hilo del mismo proceso para que siga ejecutando.

### 3. ¿Quién es responsable de la planificación de los ULT? ¿y los KLT? ¿Cómo afecta esto al rendimiento en sistemas con múltiples núcleos? 

> - ***Planificación de ULT:*** Es responsabilidad de la biblioteca de hilos (en espacio de usuario).

> - ***Planificación de KLT:*** Es responsabilidad del scheduler del sistema operativo.

> Impacto en multinúcleo: Los KLT pueden ejecutarse en paralelo en distintos núcleos de la CPU, aprovechando realmente el hardware. Los ULT, al ser vistos por el kernel como un único proceso, no pueden aprovechar el paralelismo real de múltiples núcleos por sí solos.
### 4. ¿Cómo maneja el sistema operativo los KLT y en qué se diferencian de los procesos? 
> El SO maneja los KLT mediante estructuras de datos en el kernel (como un TCB - Thread Control Block) para realizar el despacho y la planificación. A diferencia de los procesos, los KLT de un mismo proceso comparten la mayoría de sus recursos (archivos abiertos, señales, memoria compartida), mientras que cada proceso tiene su propio PCB (Process Control Block) y aislamiento total.
### 5. ¿Qué ventajas tienen los KLT sobre los ULT? ¿Cuáles son sus desventajas?
> - **Ventajas:** El kernel puede planificar hilos en múltiples procesadores y no bloquea todo el proceso si un hilo se detiene.

> - **Desventajas:** El cambio de contexto entre KLT requiere pasar al modo kernel, lo cual es más lento que el cambio entre ULT.

### 6. Qué retornan las siguientes funciones: 
    a. getpid() : Retorna el identificador del proceso actual (PID).
    b. getppid() : Retorna el identificador del proceso padre.
    c. gettid() : Retorna el identificador del hilo actual dentro del sistema.
    d. pthread_self(): Retorna el identificador del hilo según la biblioteca POSIX Threads.
    e. pth_self() : Retorna el identificador del hilo según la biblioteca GNU Pth
### 7. ¿Qué mecanismos de sincronización se pueden usar? ¿Es necesario usar mecanismos de  sincronización si se usan ULT? 
> Se pueden usar *mutex (exclusión mutua), semáforos, variables de condición y barreras.*
> Sí, sigue siendo necesario con ULT. Aunque los ULT no se ejecutan en paralelo real (en diferentes núcleos), el planificador de la biblioteca de hilos puede suspender un hilo en medio de una actualización de datos compartidos para darle tiempo a otro (concurrencia), lo que causaría condiciones de carrera si no hay sincronización.

### 8. Procesos 
#### a. ¿Qué utilidad tiene ejecutar fork() sin ejecutar exec()? 
> Sirve para crear una copia exacta del proceso padre que colabore en una tarea distribuida, permitiendo que ambos compartan el código y el estado inicial de las variables.
#### b. ¿Qué utilidad tiene ejecutar fork() + exec()?
>   Es la forma estándar de lanzar un programa nuevo. El fork() crea el proceso y el exec() reemplaza el código y la memoria del hijo con un binario distinto. 
#### c. ¿Cuál de las 2 asigna un nuevo PID fork() o exec()? 
> El fork() es quien asigna un nuevo PID al proceso hijo. El exec() mantiene el mismo PID que ya tenía el proceso.
#### d. ¿Qué implica el uso de Copy-On-Write (COW) cuando se hace fork()? 
> Implica que al hacer fork(), el padre y el hijo comparten las mismas páginas físicas de memoria inicialmente. Solo si uno de los dos intenta escribir en una página, el SO crea una copia física de esa página específica para ese proceso, ahorrando tiempo y memoria.
#### e. ¿Qué consecuencias tiene no hacer wait() sobre un proceso hijo?
> El proceso hijo, al terminar, se convierte en un proceso zombie. Ocupa un lugar en la tabla de procesos del sistema hasta que el padre recoja su estado de finalización.
#### f. ¿Quién tendrá la responsabilidad de hacer el wait() si el proceso padre termina sin hacer wait()? 
> Si el padre muere, el proceso hijo es "adoptado" por el proceso init (o systemd, con PID 1), quien se encarga de hacer el wait() y limpiar al hijo cuando este termine.

### 9. Kernel Level Threads 
#### a. ¿Qué elementos del espacio de direcciones comparten los threads creados con pthread_create()? 
> Los hilos creados con pthread_create() comparten el segmento de código, los datos globales (heap), las variables estáticas, los archivos abiertos y las señales. Cada hilo mantiene su propio stack (pila) y registros.
#### b. ¿Qué relaciones hay entre getpid() y gettid() en los KLT?
> En un KLT, getpid() devolverá el mismo valor para todos los hilos del proceso (el PID del proceso líder). gettid() devolverá un identificador único para cada hilo a nivel de kernel (Thread ID).
#### c. ¿Por qué pthread_join() es importante en programas que usan múltiples hilos? ¿Cuándo se liberan los recursos de un hilo zombie? 
> Es importante porque permite al hilo principal esperar a que otro termine, sincronizando los resultados. Los recursos de un hilo "zombie" (terminado pero no unido) se liberan cuando se invoca pthread_join() sobre él o cuando el proceso completo termina.
#### d. ¿Qué pasaría si un hilo del proceso bloquea en read()? ¿Afecta a los demás hilos?
> En KLT, si un hilo se bloquea en una operación de E/S, no afecta a los demás hilos. El kernel puede poner ese hilo en espera y planificar otro hilo del mismo proceso para que siga ejecutando en la CPU.
#### e. Describí qué ocurre a nivel de sistema operativo cuando se invoca pthread_create() (¿es syscall? ¿usa clone?). 
> pthread_create() es una función de la biblioteca, pero por debajo invoca a la syscall clone() en Linux. A diferencia de un fork() simple, clone() recibe flags que le indican al kernel que el nuevo flujo de ejecución debe compartir el espacio de memoria y otros recursos con el creador.

### 10. User Level Threads
#### a. ¿Por qué los ULTs no se pueden ejecutar en paralelo sobre múltiples núcleos?
> Porque para el Sistema Operativo, el proceso que contiene los ULTs es una sola unidad de ejecución. El Kernel no conoce la existencia de los hilos internos, por lo que solo asigna el proceso a un único núcleo de la CPU a la vez. No hay forma de que el Kernel "reparta" los hilos en distintos cores si no sabe que existen.
#### b. ¿Qué ventajas tiene el uso de ULTs respecto de los KLTs? 
> - ***Velocidad***: El cambio de contexto entre ULTs es mucho más rápido porque no requiere una llamada al sistema (syscall) ni cambiar al modo Kernel.

> - ***Personalización***: Podés usar un algoritmo de planificación (scheduling) específico para tu aplicación, sin depender del scheduler del SO.

> - ***Portabilidad***: Funcionan en sistemas operativos que no tienen soporte nativo para hilos.
#### c. ¿Qué relaciones hay entre getpid(), gettid() y pth_self() (en GNU Pth)? 
> - En ULTs, `getpid()` y `gettid()` devolverán el mismo valor para todos los hilos, ya que todos pertenecen al mismo hilo de ejecución del Kernel (LWP).

> -` pth_self()` es el único que devolverá un identificador único para cada hilo, pero este ID es gestionado únicamente por la biblioteca GNU Pth en el espacio de usuario.
#### d. ¿Qué pasaría si un ULT realiza una syscall bloqueante como read()?
>  Se bloquea todo el proceso. Como el Kernel cree que el proceso es un único hilo, si ese hilo pide algo y se queda esperando, el Kernel pone a dormir a todo el proceso, dejando a los demás ULTs sin poder ejecutar aunque estuvieran listos para trabajar.
#### e. ¿Qué tipos de scheduling pueden tener los ULTs? ¿Cuál es el más común? 

> Pueden ser apropiativos (el scheduler quita la CPU al hilo) o no apropiativos/cooperativos (el hilo debe ceder la CPU voluntariamente). El más común en bibliotecas de ULT es el cooperativo, ya que simplifica la sincronización al no haber interrupciones inesperadas

### 11. Global Interpreter Lock 
#### a. ¿Qué es el GIL (Global Interpreter Lock)? ¿Qué impacto tiene sobre programas multi-thread en Python y Ruby?
> El ***GIL*** es un mecanismo (un "candado" global) que asegura que solo un hilo de ejecución pueda controlar el intérprete de Python/Ruby a la vez. Aunque se tenga una CPU de 16 núcleos y se use 16 hilos, el GIL hará que solo uno ejecute código a la vez. Esto convierte al multi-threading en una ejecución concurrente pero no paralela (se van turnando muy rápido, pero no corren al mismo tiempo).

#### b. ¿Por qué en CPython o MRI se recomienda usar procesos en vez de hilos para tareas intensivas en CPU?
> Para saltarse el GIL. Como cada proceso tiene su propio intérprete y su propio GIL independiente, el Sistema Operativo sí puede repartir los procesos en diferentes núcleos de la CPU. Si la tarea es CPU-Bound (mucho cálculo), con procesos vas a usar el 100% de tus núcleos. Con hilos, solo usarás el equivalente a un solo núcleo por culpa del bloqueo del GIL.

## Práctica guiada 
### 1. Instale las dependencias necesarias para la práctica (strace, git, gcc, make, libc6-dev, libpth-dev, python3, htop y podman): 
    apt update 
    apt install build-essential libpth-dev python3 python3-venv strace git 
    htop podman 

### 2. Clone el repositorio con el código a usar en la práctica  
    git clone https://gitlab.com/unlp-so/codigo-para-practicas.git 

### 3. Resuelva y responda utilizando el contenido del directorio `practica3/01-strace`: 
### a. Compile los 3 programas C usando el comando make. 

### b. Ejecute cada programa individualmente, observe las diferencias y similitudes del PID y THREAD_ID en cada caso. Conteste en qué mecanismo de concurrencia las distintas tareas: 
#### i. Comparten el mismo PID y THREAD_ID 
#### ii. Comparten el mismo PID pero con diferente THREAD_ID 
#### iii. Tienen distinto PID 
> 1) Comparten el mismo PID y THREAD_ID: (Fijate cuál de los tres te da exactamente el mismo número en ambas columnas para todas las tareas). Es el mecanismo de ULT.

> 2) Comparten el mismo PID pero con diferente THREAD_ID: (Buscá el que mantiene el PID fijo pero el TID va cambiando). Es el mecanismo de KLT.

> 3) Tienen distinto PID: (Acá vas a ver que cada tarea tiene un PID totalmente diferente).Es el mecanismo de Procesos.


### c. Ejecute cada programa usando strace (strace ./nombre_programa > /dev/null) y responda: 
#### i. ¿En qué casos se invoca a la systemcall clone o clone3 y en cuál no? ¿Por qué?
> No se invoca en UL. Porque los ULT son gestionados totalmente por una biblioteca en espacio de usuario; la biblioteca simplemente alterna entre funciones usando la misma "unidad de ejecución" que ya le dio el Kernel al proceso original.
#### ii. Observe los flags que se pasan al invocar a clone o clone3 y verifique en qué caso se usan los flags CLONE_THREAD y CLONE_VM. 
#### iii. Investigue qué significan los flags CLONE_THREAD y CLONE_VM usando la manpage de clone y explique cómo se relacionan con las diferencias entre procesos e hilos. 
> - **CLONE_VM:** Indica que el proceso llamador y el nuevo comparten el mismo espacio de memoria virtual. Si uno cambia una variable, el otro ve el cambio.

> - **CLONE_THREAD:** Indica que el nuevo proceso se coloca en el mismo grupo de hilos que el llamador (comparten el PID).

> - **Relación procesos/hilos:** Un hilo se define técnicamente en Linux como un proceso que comparte memoria (CLONE_VM) y grupo de hilos (CLONE_THREAD) con su padre. Un proceso hijo, al no tener estos flags, nace con su propia memoria independiente y un PID nuevo.
#### iv. printf() eventualmente invoca la syscall write (con primer argumento 1, indicando que el file descriptor donde se escribirá el texto es STDOUT). Vea la salida de strace y verifique qué invocaciones a write(1, ...) ocurren en cada caso.
#### v. Pruebe invocar de nuevo strace con la opción -f y vea qué sucede respecto a las invocaciones a write(1, …). Investigue qué es esa opción en la manpage de strace. ¿Por qué en el caso del ULT se puede ver la invocación a write(1, …) por parte del thread hijo aún sin usar -f?
> Porque en el caso de los ULT no hay hijos reales para el Kernel. Como no se invocó a clone, no hay un segundo flujo que seguir; todo el código (incluyendo el de los "hilos" de usuario) se ejecuta dentro del mismo y único proceso que strace ya está monitoreando.

### 4. Resuelva y responda utilizando el contenido del directorio practica3/02-memory: 
### a. Compile los 3 programas C usando el comando make. 
### b. Ejecute los 3 programas. 
### c. Observe qué pasa con la modificación a la variable number en cada caso. ¿Por qué suceden cosas distintas en cada caso? 

> - ***Procesos***: number no cambia para el padre porque la memoria es privada (aislamiento).

> - ***KLT***: number cambia pero el resultado es impredecible (como tu 84) porque comparten memoria y hay paralelismo real, lo que provoca una condición de carrera.

> - ***ULT***: number cambia y suele ser exacto porque comparten memoria pero no hay paralelismo real; se ejecutan de a uno por vez.

### 5. El directorio practica3/03-cpu-bound contiene programas en C y en Python que ejecutan una tarea CPU-Bound (calcular el enésimo número primo). 
### a. Ejecute htop en una terminal separada para monitorear el uso de CPU en los siguientes incisos. 
### b. Ejecute los distintos ejemplos con make (usar make help para ver cómo) y observe cómo aparecen los resultados, cuánto tarda cada thread y cuanto tarda el programa completo en finalizar. 
### c. ¿Cuántos threads se crean en cada caso? 
### d. ¿Cómo se comparan los tiempos de ejecución de los programas escritos en C (ult y klt)? 
### e. ¿Cómo se comparan los tiempos de ejecución de los programas escritos en Python (ult.py y klt.py)? 
### f. Modifique la cantidad de threads en los scripts Python con la variable NUM_THREADS para que en ambos casos se creen solamente 2 threads, vuelva a ejecutar y comparar los tiempos. ¿Nota algún cambio? ¿A qué se debe?


 

