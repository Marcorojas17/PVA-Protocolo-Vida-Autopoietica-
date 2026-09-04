#!/usr/bin/env python3
"""
Webhook para Mercado Pago - PVA KRONOS 360
Valida firma, responde 200 inmediato, y procesa en background.
"""
import os
import threading
from flask import Flask, request, jsonify
from mercadopago.webhook import WebhookSignatureValidator, InvalidWebhookSignatureError

# Credenciales
MP_ACCESS_TOKEN = os.getenv("MP_ACCESS_TOKEN")
MP_WEBHOOK_SECRET = os.getenv("MP_WEBHOOK_SECRET")

# Importar Enjambre
import sys
sys.path.append('/workspaces/PVA-Protocolo-Vida-Autopoietica-/KRONOS/agentes')
from enjambre_autopoietico import Enjambre

app = Flask(__name__)

def procesar_evento(data_id: str):
    """Procesa el pago en segundo plano (después de responder 200)."""
    print(f"[WEBHOOK] Procesando pago {data_id}...")
    try:
        # 1. Consultar pago (con tu MP_ACCESS_TOKEN)
        import mercadopago
        sdk = mercadopago.SDK(MP_ACCESS_TOKEN)
        payment_info = sdk.payment().get(data_id)
        payment_status = payment_info["response"]["status"]
        external_reference = payment_info["response"]["external_reference"]

        # 2. Si está aprobado, ejecutar Enjambre
        if payment_status == "approved":
            enjambre = Enjambre()
            enjambre.ciclo()
            print(f"[WEBHOOK] Pago {data_id} aprobado. Enjambre ejecutado.")
        else:
            print(f"[WEBHOOK] Pago {data_id} estado: {payment_status}")

    except Exception as e:
        print(f"[WEBHOOK] Error procesando {data_id}: {e}")

@app.route('/webhook', methods=['POST'])
def webhook():
    # 1. Validar firma (usando SDK oficial)
    try:
        WebhookSignatureValidator.validate(
            request.headers.get("x-signature"),
            request.headers.get("x-request-id"),
            request.args.get("data.id"),
            MP_WEBHOOK_SECRET,
        )
    except InvalidWebhookSignatureError:
        return jsonify({"error": "invalid_signature"}), 401

    # 2. Obtener data.id desde query params
    data_id = request.args.get("data.id")
    if not data_id:
        return jsonify({"error": "missing_data_id"}), 400

    # 3. Responder 200 inmediato (dentro del timeout de 22 segundos)
    threading.Thread(target=procesar_evento, args=(data_id,), daemon=True).start()
    return ("", 200)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8081, debug=True)
