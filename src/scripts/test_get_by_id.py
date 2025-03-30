import sys
import os

# Agregar la carpeta raíz al path de Python
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from src.config.session import get_db
from src.crud.producto_crud import obtener_producto_por_id

# Obtener una sesión de la base de datos
db = next(get_db())

# ID del producto que queremos buscar
producto_id = 1 # Asegurarnos de que exista el id

# Buscamos el producto 
producto = obtener_producto_por_id(db, producto_id)

# Mostrar el resultado
if producto:
    print(f"Producto encontrado: {producto}")
else:
    print(f"No se encontró un producto con ID: {producto_id}")  
