# Importacion de dependencias.
from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base # Se usa para crear una clase base que servira como padre para nuestros modelos
from sqlalchemy.orm import sessionmaker # Para crear sesiones, para interactuar con la base de datos.

# Conexión a la base de datos SQLite
DATABASE_URL = "sqlite:///src/config/inventario.db" # Definiendo ruta donde se almacenará la base de datos en SQLite
engine = create_engine(DATABASE_URL, echo=True) # Creaando el motor de la conexion a la base de datos. (echo=True, para ver los logs en la terminal.)

# Base para definir modelos
Base = declarative_base() # Creando una clase base de la que heredaran todos los modelos de la base de datos.

# Crear sesión
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
