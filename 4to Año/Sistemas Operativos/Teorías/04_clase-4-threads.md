# Hilos

Los  nuevos  sistemas  operativos  (por  ejemplo  W2000,  Solaris,  Linux)  cuentan  con  un 
mecanismo para proveer concurrencia dentro del mismo espacio de direcciones. A este 
tipo  de  “proceso”  se  le  llama  ***hilo***  (thread). Es la unidad básica de utilización de la CPU.
Se ejecuta secuencialmente y es interrumpible para que el procesador pase a otro hilo. Permite que 
el programador pueda ejercer la modularidad. Un proceso puede verse como una colección de uno o más hilos.


## Estados de un hilo

Un hilo puede estar en estado de ready, blocked, running ó exiting, como los procesos 
tradicionales. 
Hay cuatro operaciones que provocan los cambios de estado: la creación, el bloqueo, el 
desbloqueo y la terminación. 
 
Al  crearse  un  proceso,  se  crea  un  hilo  (que  puede  crear  otros  hilos,  cada  uno  con  su 
nuevo contexto y pilas) y pasará al estado de listo. 
 
Cuando el hilo debe esperar por un evento se bloquea. Según las diferentes 
implementaciones, puede ocurrir que quede todo el proceso bloqueado, o solo ese hilo. 
En este último caso se le puede dar el control a otro hilo de ese proceso.  
 
Cuando  se  produce  el  evento  por  el  que  estaba  esperando,  el  hilo  bloqueado  se 
desbloquea, pasando al estado de listo. 
 
Al terminar, el hilo libera su contexto y sus pilas.

## Tipos de hilos 
 
Hay hilos a nivel de usuario (**ULT**, *user level thread*) e hilos a nivel de núcleo (**KLT**, 
*kernel level thread*). 
 
En  los  ULT,  la  administración  de  los  hilos  lo  hace  la  aplicación  sin  intervención  del 
kernel.  Es  más:  el  kernel  ni  se  entera  de  su  existencia.  El  kernel  no  ve  el  hilo:  ve  un 
proceso haciendo un requerimiento. LA creación de los hilos y operaciones se hacen en 
a nivel de usuario y por lo tanto son más rápidos de crear y utilizar. 
 
En estos casos se trabaja con una biblioteca de hilos que son funciones para 
implementar ULT invocadas desde la aplicación (crear y destruir hilos, intercambio de 
mensajes  y  datos  entre  hilos,  planificación  de  ejecución,  salvado  y  restauración  de 
contexto). 
Todo esto se realiza dentro del mismo proceso, en su espacio de direcciones. 
 
Ejemplos  de  bibliotecas  de  Hilos  son  POSIX  Pthreads,  Mach  C-Threads  y  Solaris 
Threads.

## Modelos multihilos 
 
Como  algunos  sistemas  proveen  tanto  KLT  como  ULT,  tenemos  diferentes  modelos 
multihilo: varios a uno, uno a uno y varios a varios 
 
### Modelo varios a uno 
 
Este modelo relaciona varios hilos a nivel de usuario con un hilo de kernel. 
Si bien toda la operación entre hilos se hace en el espacio de usuario, si uno de ellos se 
bloquea,  se  bloquea  todo  el  proceso.  Por  ejemplo,  ante  un  system  call  que  realice  un 
hilo, se bloqueará  todo el proceso. 
Al kernel acceden de a un hilo, asi que este modelo no es util en ambiente 
multiprocesador. 
 
### Modelo uno a uno 
 
En este modelo cada hilo de usuario se relaciona con uno de kernel.  
En  este  caso,  si  un  hilo  se  bloquea,  puede  ejecutarse  otro  hilo  del  mismo  proceso.  Lo 
que si garantiza este modelo es la concurrencia pues en un proceso formado por varios 
hilos, en un ambiente multiprocesador puede correr cada uno en un procesador distinto. 
No  obstante  se  debe  tener  en  cuenta  que  cada  vez  que  necesito  un  hilo  de  usuario  se 
debe crear uno de kernel con el gasto que eso significa. 
 
### Modelo de varios a varios 
 
Este  modelo  combina  o  “multiplexa”  muchos  hilos  a  nivel  de  usuario  con  un  número 
menor o igual de hilos a nivel de kernel. 
Se pueden crear tantos hilos de usuario como sea necesario y los hilos a nivel de kernel 
correspondientes se ejecutan en paraleo si es un ambiente multiprocesador. 
En el modelo uno a uno si bien premite mayor concurrencia, hay que ser cuidadoso con 
no crear demasiados hilos, pues en algunos casos este número se limita.  
Si es un modelo varios a varios se crearan un número de hilos kernel que se permita y se 
multiplexan los hilos de usuario en esos hilos de kernel. 

## Hilos en Solaris  
Solaris es una versión de Unix. Es un sistema operativo moderno que soporta threads a 
nivel de usuario y de kernel, SMP, planificación en tiempo real. 
 
Los ULT son soportados por una librería y el kernel no los reconoce. 
 
Entre los hilos a nivel de usuario y los a nivel de kernel, hay un nivel intermedio, LWP 
(Light Weight Process). 
Cada  proceso  tiene  como  mínimo  un  LWP.  La  biblioteca  de  hilos  se  encarga  de 
combinar hilos ULT con respecto a un LWP. 
 
Los  ULT  se  multiplexan  en  los  LWPs  del  proceso  y  solamente  trabajan  los  ULT  del 
LWP corriente. El resto espera por un LWP que se ejecute o están bloqueados.

