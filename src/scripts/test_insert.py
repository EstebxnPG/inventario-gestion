import sys
import os

# Agregar la carpeta raíz al path de Python
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))
from src.config.session import get_db
from src.crud.producto_crud import agregar_producto

# Obtener una sesión de la base de datos
db = next(get_db())

# Insertar un producto de prueba
producto = agregar_producto(db, "Mouse Gamer", "Mouse con luces RGB", 35.99, 15)

print(f"Producto agregado: {producto}")