from src.config.database import SessionLocal

# función para obtener una sesión de base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db # La sesion se mantiene abierta mientras se use
    finally:
        db.close()
            