#!/usr/bin/env python3
"""
Sello de Peritaje KRONOS.
Añade la firma del perito y el folio a cualquier manifiesto generado.
"""

import hashlib
import time

PERITO_EMAIL = "kronosproyecto@hotmail.com"
FOLIO_PERITO = "5204160405358537"
SAFE_CREATIVE_ID = "2607146379465"

def generar_sello_kronos(hash_manifesto: str) -> str:
    timestamp = int(time.time())
    sello_hash = hashlib.sha256(f"{FOLIO_PERITO}-{hash_manifesto}-{timestamp}".encode()).hexdigest()
    
    sello = (
        f"--- SELLO DE PERITAJE KRONOS ---\n"
        f"Perito Responsable: {PERITO_EMAIL}\n"
        f"Folio de Peritaje: {FOLIO_PERITO}\n"
        f"ID SafeCreative: {SAFE_CREATIVE_ID}\n"
        f"Huella del Manifiesto: {hash_manifesto}\n"
        f"Sello KRONOS-TRACE-PVA: {sello_hash[:16].upper()}\n"
        f"Verificación: {PERITO_EMAIL}"
    )
    return sello
