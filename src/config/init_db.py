import sys # Para modificaar el sys.path que es la lista de rutas donde Python busca los móduls cuando hacemos import.
import os # Ayuda para manejar rutas de archivos.

# Agregar la carpeta raíz al path de Python
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from src.config.database import engine, Base # Importanod los modulos necesarios
from src.models.producto import Producto

# Crear las tablas de la base de datos
Base.metadata.create_all(bind=engine) # Creand las tablas en la base de datos.
print("Base de datos y tablas creadas correctamente.") # Mensaje de confirmación.