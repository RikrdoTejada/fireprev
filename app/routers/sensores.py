from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List

from app.core.database import get_db
from app.schemas import sensor as sensor_schemas
from app.services import sensor as sensor_service

router = APIRouter()

@router.post("/zonas/", response_model=sensor_schemas.ZonaResponse)
async def crear_zona(zona: sensor_schemas.ZonaCreate, db: AsyncSession = Depends(get_db)):
    db_zona = await sensor_service.get_zona_by_nombre(db, nombre=zona.nombre)
    if db_zona:
        raise HTTPException(status_code=400, detail="La zona ya existe")
    return await sensor_service.create_zona(db=db, zona=zona)

@router.post("/", response_model=sensor_schemas.SensorResponse)
async def registrar_sensor(sensor: sensor_schemas.SensorCreate, db: AsyncSession = Depends(get_db)):
    db_sensor = await sensor_service.get_sensor_by_codigo(db, codigo=sensor.codigo)
    if db_sensor:
        raise HTTPException(status_code=400, detail="Sensor ya registrado")
    return await sensor_service.create_sensor(db=db, sensor=sensor)

@router.get("/", response_model=List[sensor_schemas.SensorResponse])
async def listar_sensores(skip: int = 0, limit: int = 100, db: AsyncSession = Depends(get_db)):
    return await sensor_service.get_sensores(db, skip=skip, limit=limit)