# Dockerfile - PVA Protocolo
FROM python:3.11-slim

WORKDIR /app

# Instalar dependencias del sistema necesarias para reportlab y qrcode
RUN apt-get update && apt-get install -y \
    libcairo2 \
    libpango-1.0-0 \
    libpangocairo-1.0-0 \
    libgdk-pixbuf2.0-0 \
    && rm -rf /var/lib/apt/lists/*

# Copiar requirements e instalar
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el resto del código
COPY . .

# Exponer puerto para Flask (si usas)
EXPOSE 5000

# Comando de ejecución (por defecto: pruebas, pero puedes cambiarlo)
CMD ["python", "-m", "pytest", "tests/"]
