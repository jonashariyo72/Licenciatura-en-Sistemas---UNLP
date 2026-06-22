# SISTEMAS OPERATIVOS -  Práctica 4B - Docker y Docker Compose 

## Docker 

### 1. Utilizando sus palabras, describa qué es Docker y enumere al menos dos beneficios que encuentre para el concepto de contenedores. 
>   *Docker* es una plataforma de código abierto diseñada para empaquetar y ejecutar aplicaciones dentro de contenedores livianos. Sus beneficios pueden ser: 
> **Eficiencia de recursos:** A diferencia de las máquinas virtuales (VM), los contenedores no requieren un sistema operativo invitado (Guest OS) completo, sino que comparten el kernel del anfitrión, lo que permite correr más servicios en un mismo equipo.  
> **Aislamiento:** Utiliza características del kernel como Namespaces para proporcionar un espacio de trabajo aislado (red, procesos, montajes) por cada contenedor.

### 2. ¿Qué es una imagen? ¿Y un contenedor? ¿Cuál es la principal diferencia entre ambos? 
> Una **imagen** es un "molde" o template de solo lectura que contiene todas las instrucciones necesarias para construir un contenedor.

> Un **contenedor** es una instancia en ejecución de una imagen.

> La diferencia principal es que los contenedores añaden una capa escribible (R/W) sobre las capas de solo lectura de la imagen; cuando el contenedor se elimina, esta capa desaparece, pero la imagen original permanece intacta.

### 3. ¿Qué es Union Filesystem? ¿Cómo lo utiliza Docker?
> Es un mecanismo que permite montar varios directorios (capas) en un único punto de montaje, haciendo que parezcan un solo sistema de archivos.  Docker lo utiliza para apilar las capas de una imagen una sobre otra. Al ejecutar un contenedor, se establece este sistema de archivos como el directorio raíz mediante chroot.  

### 4. ¿Qué rango de direcciones IP utilizan los contenedores cuando se crean? ¿De dónde la obtiene? 
> Los contenedores tienen redes habilitadas por defecto y pueden realizar conexiones salientes. Pueden comunicarse entre sí utilizando direcciones IP o nombres dentro de una misma red definida por el usuario. Generalmente, las obtienen de un puente virtual (bridge) gestionado por Docker.  

### 5. ¿De qué manera puede lograrse que las datos sean persistentes en Docker? ¿Qué dos maneras hay de hacerlo? ¿Cuáles son las diferencias entre ellas?
> Los datos creados dentro de la capa escribible de un contenedor no persisten si este es destruido. Para evitar esto, existen dos métodos:  

> **Volumes:** Son gestionados íntegramente por Docker (normalmente en /var/lib/docker/volumes) y ofrecen mejor portabilidad.  
> **Bind Mounts:** Pueden estar en cualquier ubicación del sistema de archivos del anfitrión y pueden ser modificados por procesos externos a Docker.