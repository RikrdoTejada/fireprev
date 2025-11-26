from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.database import get_db
from app.schemas import lectura as lectura_schemas
from app.services import lectura as lectura_service 

router = APIRouter()

@router.post("/", response_model=lectura_schemas.LecturaResponse)
async def recibir_lectura(
    datos: lectura_schemas.LecturaCreate, 
    db: AsyncSession = Depends(get_db)
):
    return await lectura_service.registrar_lectura(db, datos)