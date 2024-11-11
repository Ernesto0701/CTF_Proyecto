# Dockerfile para el servicio de Notificaciones

# Utiliza una imagen base de Python
FROM python:3.10-slim

# Establece el directorio de trabajo en el contenedor
WORKDIR /app

# Copia los archivos necesarios para el servicio
COPY . /app/

# Instala las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Exponer el puerto en el que correrá la API REST
EXPOSE 5003

# Define el comando para ejecutar la aplicación
CMD ["python", "notifications_service.py"]
