from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Conexión a la base de datos SQLite
DATABASE_URL = "sqlite:///src/config/inventario.db"
engine = create_engine(DATABASE_URL, echo=True)

# Base para definir modelos
Base = declarative_base()

# Crear sesión
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
