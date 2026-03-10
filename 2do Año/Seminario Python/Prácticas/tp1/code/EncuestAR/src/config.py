from pathlib import Path

# ruta al proyecto (donde estn las carpetas /data, /notebooks, /src, /app)
PROJECT_PATH = Path(__file__).resolve().parent.parent

# ruta a la carpeta de datos
DATA_PATH = PROJECT_PATH / "data"

# ruta a la carpeta de notebooks
NOTEBOOKS_PATH = PROJECT_PATH / "notebooks"

# ruta a la carpeta de la app
APP_PATH = PROJECT_PATH / "app"

RESULTADOS_PATH = PROJECT_PATH / "resultados"

SRC_PATH = PROJECT_PATH / "src"