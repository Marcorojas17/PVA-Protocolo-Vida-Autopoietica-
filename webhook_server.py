#!/usr/bin/env python3
import os
import threading
from flask import Flask, request
from mercadopago.webhook import WebhookSignatureValidator, InvalidWebhookSignatureError
from dotenv import load_dotenv

load_dotenv()

MP_ACCESS_TOKEN = os.getenv("MP_ACCESS_TOKEN")
MP_WEBHOOK_SECRET = os.getenv("MP_WEBHOOK_SECRET")

app = Flask(__name__)

def procesar_evento(data_id: str):
    print(f"[WEBHOOK] Procesando pago {data_id}...")
    try:
        if not MP_ACCESS_TOKEN:
            print("[WEBHOOK] MP_ACCESS_TOKEN no configurado; omitiendo consulta.")
            return
        import mercadopago
        sdk = mercadopago.SDK(MP_ACCESS_TOKEN)
        payment_info = sdk.payment().get(data_id)
        payment_status = payment_info["response"]["status"]
        if payment_status == "approved":
            import sys
            sys.path.append('/workspaces/PVA-Protocolo-Vida-Autopoietica-/KRONOS/agentes')
            from enjambre_autopoietico import Enjambre
            enjambre = Enjambre()
            enjambre.ciclo()
            print(f"[WEBHOOK] Pago {data_id} aprobado. Enjambre ejecutado.")
        else:
            print(f"[WEBHOOK] Pago {data_id} estado: {payment_status}")
    except Exception as e:
        print(f"[WEBHOOK] Error procesando {data_id}: {e}")

@app.route('/webhook', methods=['POST'])
def webhook():
    data_id = request.args.get("data.id")
    if not data_id:
        return ("missing data.id", 400)
    if not MP_WEBHOOK_SECRET:
        return ("missing webhook secret", 500)
    x_signature = request.headers.get("x-signature")
    x_request_id = request.headers.get("x-request-id")
    if not x_signature or not x_request_id:
        return ("missing signature headers", 400)
    try:
        WebhookSignatureValidator.validate(
            x_signature,
            x_request_id,
            data_id,
            MP_WEBHOOK_SECRET,
        )
    except InvalidWebhookSignatureError:
        return ("", 401)
    threading.Thread(target=procesar_evento, args=(data_id,), daemon=True).start()
    return ("", 200)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8081, debug=True)
