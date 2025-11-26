FROM python:3.10-slim

# 2. Evitar que Python escriba archivos .pyc y habilitar logs en tiempo real
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# 3. Establecer el directorio de trabajo dentro del contenedor
WORKDIR /code

# 4. Instalar dependencias del sistema necesarias para compilar librerías (opcional pero recomendado para asyncpg)
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# 5. Copiar primero el requirements.txt para aprovechar el caché de Docker
COPY requirements.txt /code/

# 6. Instalar las dependencias de Python
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# 7. Copiar el resto del código de la aplicación
COPY ./app /code/app

# 8. Exponer el puerto donde correrá Uvicorn
EXPOSE 8000

# 9. Comando para arrancar la API
# Usamos "0.0.0.0" para aceptar conexiones externas al contenedor
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]