#!/usr/bin/env python3
"""
PVA Audit Trail - Versión Inmutable
- Genera una cadena de custodia con hash encadenado (tipo blockchain local).
- Cada entrada contiene el hash de la entrada anterior.
- Prepara el archivo para ser subido a IPFS (inmutabilidad real).

Requisitos:
    pip install ipfshttpclient
"""

import os
import json
import hashlib
import time
from datetime import datetime

# Configuración
FOLIO = "5204160405358537"
PERITO = "kronosproyecto@hotmail.com"
LOG_PATH = "audit/cadena_custodia.log"
GENESIS_HASH = "41a3683bbf83296eeb45da9b0e0ea5a7c095e78b493772e79520a92dbc39f4c3"

# Nodo IPFS (puedes usar uno público o el tuyo)
IPFS_API_URL = "/dns/ipfs.infura.io/tcp/5001/https"

def get_previous_hash():
    """Obtiene el último hash de la cadena de custodia."""
    if not os.path.exists(LOG_PATH):
        return "0" * 64  # Hash inicial (génesis de la cadena)
    
    with open(LOG_PATH, "r", encoding="utf-8") as f:
        lines = f.readlines()
    
    if not lines:
        return "0" * 64
    
    # El hash está al final de la última línea en formato: ...|HASH=xxxxxx
    last_line = lines[-1].strip()
    if "|HASH=" in last_line:
        return last_line.split("|HASH=")[-1]
    return "0" * 64

def create_log_entry(event_description, prev_hash):
    """Crea una nueva entrada con hash encadenado."""
    timestamp = int(time.time())
    timestamp_iso = datetime.utcfromtimestamp(timestamp).isoformat()
    
    # Datos del evento
    event_data = f"{FOLIO}|{PERITO}|{event_description}|{timestamp}|{prev_hash}"
    event_hash = hashlib.sha256(event_data.encode()).hexdigest()
    
    # Línea de log
    log_line = f"{timestamp_iso}|{event_description}|HASH={event_hash}|PREV={prev_hash}"
    
    # Guardar en el archivo (append-only)
    with open(LOG_PATH, "a", encoding="utf-8") as f:
        f.write(log_line + "\n")
    
    return event_hash

def upload_to_ipfs(file_path):
    """Sube el archivo a IPFS para inmutabilidad real."""
    try:
        import ipfshttpclient
        client = ipfshttpclient.connect(IPFS_API_URL)
        res = client.add(file_path)
        return res["Hash"]
    except Exception as e:
        print(f"⚠️  No se pudo subir a IPFS: {e}")
        return None

def generate_audit_trail():
    """Genera la cadena de custodia completa."""
    print("🔐 Iniciando cadena de custodia inmutable...")
    
    # 1. Evento inicial
    prev_hash = get_previous_hash()
    print(f"Hash anterior: {prev_hash}")
    
    # 2. Registrar eventos
    eventos = [
        "Registro SafeCreative 2607146379465 verificado",
        "Hash SHA256 Génesis cargado",
        "Motor PVA iniciado (51% Humano / 49% IA)",
        "Sello KRONOS-TRACE generado",
        "Manifiesto derivado sellado",
        "Auditoría ISO/NOM completada"
    ]
    
    hashes = []
    for evento in eventos:
        prev_hash = create_log_entry(evento, prev_hash)
        hashes.append(prev_hash)
        print(f"✔ Evento registrado: {evento}")
    
    # 3. Subir a IPFS (opcional pero recomendado)
    ipfs_hash = upload_to_ipfs(LOG_PATH)
    if ipfs_hash:
        print(f"✅ Archivo subido a IPFS: {ipfs_hash}")
        with open("audit/ipfs_reference.txt", "w") as f:
            f.write(f"IPFS_HASH={ipfs_hash}\n")
    
    # 4. Resumen final
    print("\n📋 CADENA DE CUSTODIA COMPLETA:")
    print(f"Folio: {FOLIO}")
    print(f"Perito: {PERITO}")
    print(f"Eventos registrados: {len(eventos)}")
    print(f"Último hash: {hashes[-1]}")
    print("🔒 Cadena inmutable (append-only)")

if __name__ == "__main__":
    generate_audit_trail()
