from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.models import lectura as lectura_models

async def get_alertas(db: AsyncSession, skip: int = 0, limit: int = 100, solo_no_atendidas: bool = False):
    """
    Recupera el historial de alertas generadas por el sistema.
    """
    query = select(lectura_models.Alerta).order_by(lectura_models.Alerta.fecha.desc())
    
    if solo_no_atendidas:
        query = query.where(lectura_models.Alerta.atendida == False)
        
    result = await db.execute(query.offset(skip).limit(limit))
    return result.scalars().all()