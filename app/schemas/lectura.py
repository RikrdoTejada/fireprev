from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class LecturaBase(BaseModel):
    # Campos opcionales porque un sensor puede enviar solo parciales
    temperatura: Optional[float] = None
    humedad: Optional[float] = None
    humo_ppm: Optional[float] = None
    bateria_voltaje: Optional[float] = None

class LecturaCreate(LecturaBase):
    sensor_id: int
    # No pedimos 'tiempo' aquí, lo genera la DB automáticamente al recibirlo

class LecturaResponse(LecturaBase):
    tiempo: datetime
    sensor_id: int
    
    class Config:
        from_attributes = True

# Esquema para Alertas (lo usará el Dashboard)
class AlertaResponse(BaseModel):
    id: int
    sensor_id: int
    mensaje: str
    nivel: str
    fecha: datetime
    atendida: bool

    class Config:
        from_attributes = True