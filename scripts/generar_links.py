#!/usr/bin/env python3
import os, json
from pathlib import Path
from dotenv import load_dotenv
import mercadopago

load_dotenv()

MP_ACCESS_TOKEN = os.getenv("MP_ACCESS_TOKEN")
MP_SUCCESS_URL = os.getenv("MP_SUCCESS_URL")
MP_FAILURE_URL = os.getenv("MP_FAILURE_URL")
MP_PENDING_URL = os.getenv("MP_PENDING_URL")
MP_NOTIFICATION_URL = os.getenv("MP_NOTIFICATION_URL")

if not MP_ACCESS_TOKEN:
    raise RuntimeError("Falta MP_ACCESS_TOKEN en.env - AUDITORIA 100/10 FALLIDA")

sdk = mercadopago.SDK(MP_ACCESS_TOKEN)

# FOLIOS PERICIALES 100/10
FOLIO_MAESTRO = "5204160405358537"
FOLIO_PERICIAL = "KRONOS-MT01JAAF"
SHA = "a4ff808e"
HASH_GENESIS = "41a3683bbf83296eeb45da9b0e0ea5a7c095e78b493772e79520a92dbc39f4c3"

niveles = {
    1: {"titulo": "Sello KRONOS Nivel 1 - Dictamen PDF + QR", "precio": 500.00},
    2: {"titulo": "Sello KRONOS Nivel 2 - Auditoría ISO + Blockchain", "precio": 1500.00},
    3: {"titulo": "Plan Enjambre - Protección 24/7 mensual", "precio": 3500.00},
}

links_output = {}

for nivel, datos in niveles.items():
    preference_data = {
        "items": [{
            "title": datos["titulo"],
            "quantity": 1,
            "unit_price": float(datos["precio"]),
            "currency_id": "MXN",
            "description": f"{FOLIO_PERICIAL} - {SHA} - ISO27037"
        }],
        "external_reference": f"{FOLIO_MAESTRO}-N{nivel}-{FOLIO_PERICIAL}",
        "metadata": {
            "folio_maestro": FOLIO_MAESTRO,
            "folio_pericial": FOLIO_PERICIAL,
            "sha": SHA,
            "hash_genesis": HASH_GENESIS,
            "nivel": nivel
        },
        "back_urls": {
            "success": MP_SUCCESS_URL,
            "failure": MP_FAILURE_URL,
            "pending": MP_PENDING_URL
        },
        "auto_return": "approved",
        "notification_url": MP_NOTIFICATION_URL,
        "statement_descriptor": f"KRONOS N{nivel}"
    }

    result = sdk.preference().create(preference_data)
    pref = result.get("response") or {}
    init_point = pref.get("init_point") or pref.get("sandbox_init_point")
    pref_id = pref.get("id")

    print(f"Nivel {nivel} - {datos['titulo']} - ${datos['precio']} MXN")
    print(f"External_ref: {preference_data['external_reference']}")
    print(f"Link: {init_point}")
    print(f"Preference ID: {pref_id}\n")

    links_output[nivel] = {
        "init_point": init_point,
        "pref_id": pref_id,
        "external_reference": preference_data["external_reference"]
    }

Path("web").mkdir(exist_ok=True)
Path("web/links_pago.json").write_text(json.dumps(links_output, indent=2), encoding="utf-8")
print("✅ web/links_pago.json actualizado - LUZ PRENDIDA OFFLINE")
