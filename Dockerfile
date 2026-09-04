FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN mkdir -p /app/audit /app/logs

CMD ["python", "KRONOS/agentes/enjambre_autopoietico.py"]
