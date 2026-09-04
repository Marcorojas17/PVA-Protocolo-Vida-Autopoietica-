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
    sello = (
        f"FOLIO:{FOLIO_PERITO}|"
        f"PERITO:{PERITO_EMAIL}|"
        f"GENESIS:{hash_manifesto}"
    )
    return sello
