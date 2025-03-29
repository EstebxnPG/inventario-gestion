from sqlalchemy.orm import Session
from src.models.producto import Producto

# Función para agregar un nuevo producto
def agregar_producto(db: Session, nombre: str, descripcion: str, precio: float, cantidad: int):
    nuevo_producto = Producto(nombre=nombre, descripcion=descripcion, precio=precio, cantidad=cantidad)
    db.add(nuevo_producto) # Agregar el producto a la sesión
    db.commit() # Guardar los cambios en la base de datos.
    db.refresh(nuevo_producto) # Actualizar el objeto con la información guardada.
    return nuevo_producto


def obtener_productos(db: Session):
    return db.query(Producto).all()

def obtener_producto_por_id(db: Session, producto_id: int):
    return db.query(Producto).filter(Producto.id == producto_id).first()
