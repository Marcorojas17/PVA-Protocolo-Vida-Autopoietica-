#!/usr/bin/env python3
"""
Genera el Dictamen Pericial PDF con membrete ISO/NOM y QR de verificación.
Instala: pip install reportlab qrcode[pil]
"""

import qrcode
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor, white
from reportlab.lib.utils import ImageReader
import io
import time

# Datos oficiales
FOLIO = "5204160405358537"
PERITO = "kronosproyecto@hotmail.com"
AUTOR = "Marco Antonio Rojas Valdovinos"
FECHA = "03/09/2026 - Lerma, EdoMex"
SAFE_ID = "2607146379465"
SHA_GENESIS = "41a3683bbf83296eeb45da9b0e0ea5a7c095e78b493772e79520a92dbc39f4c3"

# Crear QR de verificación (mailto directo al perito)
qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_H, box_size=10, border=2)
qr.add_data(f"mailto:{PERITO}?subject=Verificación Folio {FOLIO}")
qr.make(fit=True)
img_qr = qr.make_image(fill_color="#0a0a0a", back_color="#ffffff")

# Guardar QR en buffer
buffer = io.BytesIO()
img_qr.save(buffer, format="PNG")
buffer.seek(0)

# Generar PDF
archivo_pdf = f"audit/dictamen_PVA_{FOLIO}.pdf"
c = canvas.Canvas(archivo_pdf, pagesize=letter)
w, h = letter

# Fondo y membrete
c.setFillColor(HexColor("#0a0a0a"))
c.rect(0, h - 150, w, 150, fill=1, stroke=0)
c.setFillColor(white)
c.setFont("Helvetica-Bold", 24)
c.drawString(30, h - 60, "DICTAMEN PERICIAL PROTOCOLO PVA")
c.setFont("Helvetica", 10)
c.drawString(30, h - 80, f"Normas: ISO/IEC 27001:2022 / ISO 9001:2015 / NOM-151-SCFI-2016 / NOM-024-SCFI-2013")
c.drawString(30, h - 100, f"Perito Oficial: {PERITO}")
c.drawString(30, h - 115, f"Folio: {FOLIO} | SafeCreative: {SAFE_ID}")

# Cuerpo del documento
c.setFillColor(HexColor("#000000"))
c.setFont("Helvetica-Bold", 14)
c.drawString(30, h - 170, "1. IDENTIDAD Y AUTORÍA (ISO 9001:2015)")
c.setFont("Helvetica", 11)
c.drawString(30, h - 190, f"Autor: {AUTOR}")
c.drawString(30, h - 205, "Documentación controlada en llms.txt y sello_kronos.json.")

c.setFont("Helvetica-Bold", 14)
c.drawString(30, h - 240, "2. SEGURIDAD DE LA INFORMACIÓN (ISO 27001:2022)")
c.setFont("Helvetica", 11)
c.drawString(30, h - 260, f"SHA256 Génesis: {SHA_GENESIS}")
c.drawString(30, h - 275, "Control A8.12: División 51% Humano / 49% IA (semilla determinista151).")
c.drawString(30, h - 290, "Control A8.28: Firma KRONOS-TRACE en cada salida.")
c.drawString(30, h - 305, "Control A5.33: Registro Ethereum TX: 0x8ca8e84e1258abac9acb29d14d25114e4775d782ecfda51ae29933247ed2970e")

c.setFont("Helvetica-Bold", 14)
c.drawString(30, h - 350, "3. CONSERVACIÓN DE MENSAJES (NOM--SCFI-2016)")
c.setFont("Helvetica", 11)
c.drawString(30, h - 370, "Art. 5 - Integridad: Evidencia inalterable por hash criptográfico.")
c.drawString(30, h - 385, "Art. 8 - Constancia: Registro en cadena_custodia.log con timestamp 1783497302.")

c.setFont("Helvetica-Bold", 14)
c.drawString(30, h - 430, "4. INFORMACIÓN COMERCIAL (NOM-024-SCFI-2013)")
c.setFont("Helvetica", 11)
c.drawString(30, h - 450, "Nombre: PVA - Protocolo de Vida Autopoiética")
c.drawString(30, h - 465, f"Perito: {PERITO} | Folio: {FOLIO}")

# Sello de tiempo
c.setFont("Helvetica-Bold", 14)
c.drawString(30, h - 510, "5. DICTAMEN FINAL")
c.setFont("Helvetica", 11)
c.drawString(30, h - 530, "El sistema PVA es APTO para:")
c.drawString(40, h - 550, "• Emitir dictámenes periciales informáticos (NOM-151)")
c.drawString(40, h - 565, "• Operar bajo SGSI ISO 27001 como evidencia inmutable")
c.drawString(40, h - 580, "• Comercializarse como SaaS de autenticidad (KRONOS TRACE)")

# Sello KRONOS
c.setFillColor(HexColor("#00ffcc"))
c.setFont("Helvetica-Bold", 8)
sello = f"ISO-27001+NOM151|FOLIO={FOLIO}|PERITO={PERITO}|GENESIS={SHA_GENESIS}|DICTAMEN=APTO|2026-09-03"
c.drawString(30, 100, sello)

# Insertar QR
c.drawImage(ImageReader(buffer), w - 150, 120, width=120, height=120)

# Firma del perito
c.setFillColor(HexColor("#000000"))
c.setFont("Helvetica", 10)
c.drawString(30, 80, "Firma digital del perito:")
c.setFont("Helvetica-Bold", 10)
c.drawString(30, 65, PERITO)
c.drawString(30, 50, f"Fecha: {FECHA}")

c.save()
print(f"✅ PDF generado exitosamente: {archivo_pdf}")
