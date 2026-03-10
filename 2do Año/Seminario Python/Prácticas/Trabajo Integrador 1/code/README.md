# Integrantes del equipo:
VALENTIN SENESSI, PEDRO FERNANDEZ OLIVER, JONÁS HARIYO, MARIA LILA GANDINI, JOSEMARIA NICORA.


## Requisitos
Para ejecutar este proyecto, necesitarás tener las siguientes bibliotecas instaladas:
Antes de instalar Streamlit y Jupyter Notebook, asegurate de tener:

Python 3.7 o superior: descargalo desde python.org

pip: el instalador de paquetes de Python (ya viene con Python en la mayoría de los casos)

Verificá que estén instalados con:
python --version
pip --version

# Streamlit
# Como instalar streamlit
Instalación en Windows
1- Abrí PowerShell 
2- Crea un entorno virtual:
python -m venv env
env\Scripts\activate
3-Instalá Streamlit con pip:
pip install streamlit
4- Verificá que se instaló correctamente: 
streamlit hello


Instalación en Linux (Debian, Ubuntu, Fedora, etc.):
1- Abrí una terminal.
2- Crea un entorno virtual:
python3 -m venv env
source env/bin/activate
3-Instalá Streamlit con pip:
pip install streamlit
4- Verificá que se instaló correctamente: 
streamlit hello

Instalación en macOS:
1-Abrí la Terminal.
2- Creá un entorno virtual:
python3 -m venv env
source env/bin/activate
3-Instalá Streamlit con pip:
pip install streamlit
4- Verificá que se instaló correctamente: 
streamlit hello

# Jupyter Notebook
Jupyter Notebook es un entorno de trabajo interactivo que permite desarrollar código en Python. Es utilizado ampliamente para análisis numéricos, estadísticas y machine learning, entre otros campos de la informática.

Algunas de las principales funciones y beneficios que provee:
Permite editar el código desde el navegador, resaltando la sintaxis, indentación y también provee funciones de autocompletado.
Permite ejecutar código desde el navegador, mostrando los resultados de esta ejecución.
Provee facilidades para la documentación y visualización del código.
No solo permite escribir código Python sino también permite visualizar otro tipo de extensiones como Markdown y HTML.
Permite iniciar una sesión de una terminal de bash para ejecutar comandos desde el mismo navegador.
Se puede agregar cualquier archivo .py o .ipynb simplemente arrastrandolos hasta la interfaz de la herramienta.
Los archivos que genera son de extensión "ipynb", con lo que podemos compartirlos con nuestros compañeros.
# Como instalar jupyter notebook
Instalación en Windows
1-Abrí CMD o PowerShell.
2-Creá y activá un entorno virtual:
python -m venv env
env\Scripts\activate
3-Instalá Jupyter Notebook:
pip install notebook
4-Ejecutalo:
jupyter notebook

Instalación en Linux (Ubuntu, Debian, Fedora, etc.):
1-Abrí una terminal.
2-Creá y activá un entorno virtual:
python3 -m venv env
source env/bin/activate
3-Instalá Jupyter Notebook:
pip install notebook
4-Ejecutalo:
jupyter notebook

Instalación en macOS:
1-Abrí una terminal.
2-Creá y activá un entorno virtual:
python3 -m venv env
source env/bin/activate
3-Instalá Jupyter Notebook:
pip install notebook
4-Ejecutalo:
jupyter notebook
 # Que hago luego de la instalación?
 Una vez instalado, para poder comenzar a utilizarlo es necesario iniciar el servidor de Jupyter Notebook. Este servidor se ejecutará en "localhost", es decir que nuestra computadora creará un servidor local ejecutando la herramienta. Para esto se debe ejecutar el siguiente comando:
jupyter notebook
Una vez iniciado el servidor, nuestra computadora abrirá automáticamente el navegador web visualizando la interfaz gráfica de la herramienta. En caso de que esto no suceda automáticamente, abrir un navegador web e ingresar la siguiente url: http://localhost:8888/ Por defecto el servidor se ejecuta utilizando el puerto 8888 de nuestra computadora.

Para terminar la sesión del servidor basta simplemente con ir nuevamente a la terminal donde se ejecuto el comando anterior y presionar las teclas CTRL + C. La herramienta le pedirá una confimación y luego apagará el servidor. Importante: Guardar todos los cambios antes de apagar el servidor. De esta forma, al iniciarlo nuevamente, todos los archivos de la sesión anterior seguirán estando disponibles.

# Primeros pasos:
Para comenzar a utilizar Jupyter Notebook, primero debemos crear un archivo de código Python o "notebook". Para esto simplemente debemos hacer click en el botón "New" y seleccionar el intérprete de Python.
Una vez creado nuestro archivo notebook, solo basta con escribir código Python en él y darle click al botón "Play" para ejecutarlo y ver su resultado.

# Licencia
Este proyecto está licenciado bajo la licencia MIT. Ver el archivo [LICENSE](LICENSE) para más detalles.




