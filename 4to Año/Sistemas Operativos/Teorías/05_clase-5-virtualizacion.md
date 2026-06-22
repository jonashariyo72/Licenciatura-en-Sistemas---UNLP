# Virtualización 

La virtualización es una técnica de abstracción de recursos de computación que desacopla el hardware físico del sistema operativo. Permite que una sola computadora física realice el trabajo de varias mediante la compartición de recursos.

### Tipos de Virtualización: 
Puede darse a nivel de proceso (ej. JVM), de almacenamiento (RAID, LVM), de red, de sistema operativo (contenedores) y de sistema completo (máquinas virtuales).

### Hipervisor (VMM): 
#### Es el software que crea y administra las máquinas virtuales (VM).
> - **Tipo 1 (Nativo/Bare-metal):** Se ejecuta directamente sobre el hardware (ej. Xen, VMware ESXi, Hyper-V, KVM).
> - **Tipo 2 (Hosted):** Se ejecuta como una aplicación sobre un sistema operativo anfitrión (ej. VMware Workstation, VirtualBox).

### Técnicas de Implementación

> - ***Emulación:*** Se simula todo el hardware por software; es lenta pero permite ejecutar software de una arquitectura en otra (ej. QEMU).

> - ***Virtualización Completa (Full Virtualization):*** El sistema operativo invitado (guest) no sabe que está virtualizado y no requiere modificaciones. Utiliza técnicas como traducción binaria para manejar instrucciones sensibles.

> - ***Paravirtualización:*** El sistema operativo invitado se modifica para que, en lugar de ejecutar instrucciones sensibles, realice llamadas directas al hipervisor (hypercalls), mejorando el rendimiento.

> - ***Asistida por Hardware:*** Utiliza extensiones de la CPU (como Intel VT o AMD-V) para manejar las transiciones entre el modo guest y el hipervisor de forma eficiente.

---

# cgroups, Namespaces y Contenedores

Este enfoque se conoce como virtualización a nivel de sistema operativo, donde el kernel permite la existencia de múltiples instancias aisladas de espacio de usuario.

### Pilares de los Contenedores en Linux

> - ***Namespaces (Espacios de Nombres):*** Es la tecnología que proporciona aislamiento. Permite que un proceso vea solo los recursos que le corresponden. Algunos tipos incluyen:
>   - **PID:** Aislamiento de IDs de procesos (un proceso tiene un PID en el contenedor y otro en el host)
>   - **.NET:** Aislamiento de interfaces de red
>   - **.MNT:** Puntos de montaje privados.

> - ***Control Groups (cgroups):*** Se encargan de la limitación y medición de recursos. Permiten definir cuánta CPU, memoria RAM o ancho de banda de red puede consumir un grupo de procesos.

> - ***chroot:*** Es el antecesor más antiguo (1979), que permite cambiar el directorio raíz aparente de un proceso, creando una "jail" o jaula de archivos.

### Contenedores
A diferencia de las máquinas virtuales que emulan hardware y cargan un kernel completo por cada VM, los contenedores:

> - Comparten el mismo kernel del sistema operativo host.

> - Son, desde el punto de vista del host, simplemente un proceso o conjunto de procesos.

> - Suelen utilizarse para microservicios, donde cada contenedor provee un único servicio.