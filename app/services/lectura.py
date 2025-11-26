from sqlalchemy.ext.asyncio import AsyncSession
from app.models import lectura as lectura_models
from app.schemas import lectura as lectura_schemas
from app.services import detector

async def registrar_lectura(db: AsyncSession, datos: lectura_schemas.LecturaCreate):
    # 1. Crear modelo ORM
    nueva_lectura = lectura_models.Lectura(**datos.model_dump())
    
    # 2. Agregar a sesión (pero no commit aun)
    db.add(nueva_lectura)
    
    # 3. Usar el servicio detector para ver si hay incendio
    # (Esto generará una alerta en la DB si es necesario)
    await detector.analizar_riesgo(db, nueva_lectura)
    
    # 4. Guardar todo (Lectura + Posible Alerta)
    await db.commit()
    await db.refresh(nueva_lectura)
    
    return nueva_lectura