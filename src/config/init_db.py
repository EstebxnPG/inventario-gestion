import sys
import os

# Agregar la carpeta raíz al path de Python
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))
from src.config.database import engine, Base
from src.models.producto import Producto

# Crear las tablas de la base de datos
Base.metadata.create_all(bind=engine)
print("BAse de datos y tablas creadas correctamente.")