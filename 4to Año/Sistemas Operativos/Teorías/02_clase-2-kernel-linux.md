### Kernel Linux
***Gentileza de Mathe Lamiral***

Extrictamente el kernel de un SO es el SO en sí
- principalmente 
	- administración de CPU y memoria principal 

- Es de código abierto a los usuarios
- En una misma estructura de código fuente se da soporte a todas las arquitecturas
- Está escrito mayoritariamente en C, tiene instrucciones especiales y de bajo nivel en Assembler y oara implementar módulos, un poco de Rust
	- Rust se empezó a usar mas que nada en las últimas versiones 

El desarrollo del kernel es colaborativo, en el mismo participan empresas, universidades y desarrolladores independientes 

- Su ciclo de desarrollo se extiende generalmente en 3 a 4 meses, luego de los cuales se genera otro sprint que puede ser de 1 a 2 semanas para comitear código (merge Window) y posteriormente una ventana de correción de bugs
	- La discusión sobre el agregado de nuevas características ocurre solo en la merge window
	- En la merge window van apareciendo “release candidates”, los cuáles son identificados con las siglas rc1, rc2, etc. siguiendo el nombre de la versión. Generalmente no suele haber más de 4 release candidates, si estoy en la 4, probablemente estoy en la que será la próxima versión productiva 
- Linus Torvalds es quien mantiene el Kernel de GNU/Linux y quien aprueba o no los merge request de cada uno de los colaboradores 
	- El Kernel de Linux está dividido en subsistemas
	- Cada susbsistema es mantenido por uno o más responsables 
	- El responsable de cada subsistema acepta o no parches o pull requests de los desarrolladores. Luego el responsable interactúa con Linus para incluir las modificaciones en una versión candidata “rc”
	- Cada responsable (mantainer) tiene su propio tree para el desarrollo
		- Linus Torvalds: https://web.git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git
		- David Miller (networking): https://git.kernel.org/pub/scm/linux/kernel/git/netdev/net.git
		- Todos los repos poseen mucha actividad

#### Organización/Subsistemas del código fuente

![[Pasted image 20260318184103.png|458]]

#### Arquitectura típica

![[Pasted image 20260318184146.png|461]]

#### Núcleo monolítico híbrido

El núcleo del kernel GNU/Linux es híbrido monolítico
- Los drivers y el código del Kernel se ejecutan en modo privilegiado
- Lo que lo hace híbrido es la posibilidad de cargar y descargar funcionalidad a través de módulos 

#### Anatomía de una versión de Linux < 2.6

`X.Y.Z`
- **X** indicaba la serie principal. Cambiaba al agregar/quitar una funcionalidad muy importante
- **Y** indicaba si era una versión de producción o desarrollo
	- Números **Y** pares indicaban una versión de producción (estable)
	- Números **Y** impares indicaban una versión en desarrollo
- **Z** Bugfixes
#### Anatomía de una versión de Linux >= 2.6 y < 3.0

`A.B.C.[D]`
- **A** Denota Versión. Cambia con menor Frecuencia (cada varios años).
- **B** Denota revisión mayor.
- **C** Denota revisión menor. Solo cambia cuando hay nuevos drivers o caracterı́sticas.
- **D** Se utiliza cuando se corrige un grave error sin agregar nueva funcionalidad.

#### Anatomía de una versión de >= 3.0

`A.B.C[-rcX]`
- **A** Denota revisión mayor. Cambia con menor Frecuencia (cada varios años).
- **B** Denota revisión menor. Solo cambia cuando hay nuevos drivers o caracterı́sticas.
- **C** Número de revisión
- **rcX** Versiones de prueba

#### Por qué recompilar el Kernel?

- Soportar **nuevos dispositivos** como, por ejemplo, una placa de video
- Agregar **mayor funcionalidad** (soporte de nuevos filesystems)
- **Optimizar** funcionamiento de acuerdo al sistema en el que corre
- **Adaptarlo al sistema** donde corre (quitar soporte de hardware no utilizado)
- **Corrección de bugs** (problemas de seguridad o errores de programación)

#### Qué necesitamos para poder compilar el Kerner?
- gcc
	- Compilador de C
- make
	- ejecuta las directivas definidas en los Makefiles
- binutils
	- assembler, linker
- libc6
	- Archivos de encabezados y bibliotecas de desarrollo
- ncurses
	- bibliotecas de menú de ventanas (solo si usamos menuconfig)
- initrd-tools
	- Herramientas para crear discos RAM

>[!tip]
>En Debian y distribuciones derivadas, todo este software se encuentra empaquetado.
>Por ejemplo, para instalar el software requerido para hacer la práctica:
>`# apt-get install build-essential libncurses-dev kbuild flex bison libelf-dev bc`

#### Proceso de compilación de Linux

1. Obtener el código fuente.
2. Preparar el árbol de archivos del código fuente.
3. Configurar el kernel
4. Construir el kernel a partir del código fuente e instalar los módulos.
5. Reubicar el kernel.
6. Creación del initramfs
7. Configurar y ejecutar el gestor de arranque (GRUB en general).
8. Reiniciar el sistema y probar el nuevo kernel

>[!tip]
>Antes de modificar la configuracion (`.config`) me guardo una copia de la configuración original

