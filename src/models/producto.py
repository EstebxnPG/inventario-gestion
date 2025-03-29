# Importación de los modulos
from sqlalchemy import Column, Integer, String, Float
from src.config.database import Base

class Producto(Base): # Definiendo el nombre de la clase, hereda de Base.
    __tablename__ = "productos" # Definiendo el nombre de la tabla.

    # Definiendo las columnas de la tabla.
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    descripcion = Column(String)
    precio = Column(Float, nullable=False)
    cantidad = Column(Integer, nullable=False)

    def __init__(self, nombre, descripcion, precio, cantidad): # Definiendo el constructor.
        self.nombre = nombre 
        self.descripcion = descripcion
        self.precio = precio
        self.cantidad = cantidad

    def __repr__(self): # Representación del objeto.
        return f"<Producto(nombre={self.nombre}, precio={self.precio}, cantidad={self.cantidad})>"
