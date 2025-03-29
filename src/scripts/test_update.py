import sys
import os

# Agregar la carpeta raíz al path de Python
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from  src.config.session import get_db
from src.crud.producto_crud import actualizar_producto

# Obtener una sesión de la base de datos
db = next(get_db())

# Id del producto a actualizar
producto_id = 1

# NUevos datos del producto
nuevo_nombre = "Mouse Gamer Pro"
nueva_descripcion = " Mouse con luces RGb, y DPi ajustable"
nuevo_precio = 49.99
nueva_cantidad = 10

# Actualizar el prodcuto
producto_actualizado = actualizar_producto(db, producto_id, nuevo_nombre, nueva_descripcion, nuevo_precio, nueva_cantidad)

if producto_actualizado:
    print(f"Producto actuallizado: {producto_actualizado}")
else:
    print(f"No se encontro un producto con ID {producto_id}")