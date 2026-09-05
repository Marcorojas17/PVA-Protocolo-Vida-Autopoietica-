import os, hmac, hashlib, smtplib, json
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from flask import Flask, request, jsonify
from dotenv import load_dotenv
import mercadopago
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.colors import HexColor
load_dotenv()
app=Flask(__name__)
MP_ACCESS_TOKEN=os.getenv("MP_ACCESS_TOKEN")
MP_WEBHOOK_SECRET=os.getenv("MP_WEBHOOK_SECRET")
sdk=mercadopago.SDK(MP_ACCESS_TOKEN) if MP_ACCESS_TOKEN else None
FOLIO_BASE="5204160405358537"
HASH_GENESIS="41a3683bbf83296eeb45da9b0e0ea5a7c095e78b493772e79520a92dbc39f4c3"
def generar_pdf(folio, op_id, email):
    os.makedirs("audit", exist_ok=True)
    path=f"audit/DICTAMEN-{folio}-{op_id}.pdf"
    c=canvas.Canvas(path, pagesize=letter)
    w,h=letter
    c.setFillColor(HexColor("#0a0a0a")); c.rect(0,0,w,h,fill=1,stroke=0)
    c.setFillColor(HexColor("#00ffcc")); c.setFont("Helvetica-Bold",20); c.drawString(50,h-80,"KRONOS 360 - DICTAMEN PERICIAL")
    c.setFillColor(HexColor("#ffffff")); c.setFont("Helvetica",12)
    c.drawString(50,h-120,f"Folio: {folio}"); c.drawString(50,h-140,f"Op MP: {op_id}"); c.drawString(50,h-160,f"Hash: {HASH_GENESIS}"); c.drawString(50,h-180,f"Cliente: {email}")
    c.save(); return path
def validar(req):
    try:
        xs=req.headers.get("x-signature",""); xr=req.headers.get("x-request-id",""); did=req.args.get("data.id","")
        if not MP_WEBHOOK_SECRET or not xs: return False
        parts=dict(p.split("=",1) for p in xs.split(",") if "=" in p)
        manifest=f"id:{did};request-id:{xr};ts:{parts.get('ts','')};"
        exp=hmac.new(MP_WEBHOOK_SECRET.encode(), manifest.encode(), hashlib.sha256).hexdigest()
        return hmac.compare_digest(parts.get("v1",""), exp)
    except: return False
@app.route("/webhook/mp", methods=["POST"])
def webhook():
    if not validar(request): return jsonify({"error":"Invalid signature"}),401
    data=request.get_json(silent=True)
    if data and data.get("type")=="payment":
        try:
            pid=data["data"]["id"]
            info=sdk.payment().get(pid).get("response",{})
            if info.get("status")=="approved":
                email=info.get("payer",{}).get("email")
                folio=f"{FOLIO_BASE}-{pid}"
                pdf=generar_pdf(folio,pid,email)
                print(f"💰 Pago {pid} aprobado {email} {folio}")
        except Exception as e: print(f"Webhook error {e}")
    return jsonify({"status":"ok"}),200
@app.route("/")
def health(): return jsonify({"KRONOS":"V18 100/10","FOLIO":FOLIO_BASE,"SHA":"a4ff808e","STATUS":"LUZ PRENDIDA OFFLINE"})
if __name__=="__main__": app.run(host="0.0.0.0", port=int(os.getenv("PORT",8080)))
