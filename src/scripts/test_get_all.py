import sys
import os

# Agregar la carpeta raíz al path de Python
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from src.config.session import get_db
from src.crud.producto_crud import obtener_productos

# Obtener una sesión de la base de datos
db = next(get_db())

# Obtener todos los productos
productos = obtener_productos(db)

# Mostrar los productos obtenidos
for producto in productos:
    print(producto)