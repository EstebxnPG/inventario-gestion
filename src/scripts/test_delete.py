import sys
import os

# Agregar la carpeta raíz al path de Python
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from src.config.session import get_db
from src.crud.producto_crud import eliminar_producto

# Obtener una sesión de la base de datos
db = next(get_db())

# ID del producto a eliminar
producto_id  = 1

# Intentando eliminar el producto
producto_eliminado = eliminar_producto(db, producto_id)

# Mostrar el producto eliminadoi
if producto_eliminado:
    print(f"Producto con ID {producto_id} eliminado corectamente")
else:
    print(f"No se encontró un producto con ID {producto_id}")