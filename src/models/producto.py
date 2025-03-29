from sqlalchemy import Column, Integer, String, Float
from src.config.database import Base

class Producto(Base):
    __tablename__ = "productos"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    descripcion = Column(String)
    precio = Column(float, nullable=False)
    cantidad = Column(Integer, nullable=False)

    def __init__(self, nombre, descripcion, precio, cantidad):
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio = precio
        self.cantidad = cantidad

    def __repr__(self):
        return f"<Producto(nombre={self.nombre}, precio={self.precio}, cantidad={self.cantidad}>)"