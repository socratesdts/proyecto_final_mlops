# Utiliza una imagen base oficial de Python
FROM python:3.11

# Establece el directorio de trabajo en el contenedor
WORKDIR /app

# Copia los archivos del proyecto al directorio de trabajo
COPY . /app

# Instala las dependencias del proyecto
RUN pip install --no-cache-dir -r requirements.txt

# Expone el puerto en el que corre la aplicación
EXPOSE 8000

# Comando para correr la aplicación con Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
