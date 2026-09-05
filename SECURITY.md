# SECURITY.md - PVA Protocolo Vida Autopoietica
**FOLIO PERICIAL:** KRONOS-MT01JAAF  
**FOLIO MAESTRO:** 5204160405358537  
**SHA GENESIS:** a4ff808e  
**HASH GENESIS:** 41a3683bbf83296eeb45da9b0e0ea5a7c095e78b493772e79520a92dbc39f4c3  
**FECHA:** 2024-11-03 02:17:44 UTC  
**MODO:** LUZ PRENDIDA OFFLINE - 100/10

## 1. Política de Seguridad 51/49 - Regla Inquebrantable
El sistema opera bajo principio **51% humano / 49% algorítmico**.

- **51% Humano:** Intención, revisión, validación final, firma pericial, decisión de sellado.
- **49% Algorítmico:** Generación, hash SHA-256, render PDF, envío SMTP, verificación HMAC.

**REGLA 0:** Ningún dictamen, PDF, ni hash se emite sin `validar_firma()` + validación humana del perito. La IA es herramienta, no perito.

## 2. Cadena de Custodia ISO 27037 / NOM-151 / eIDAS
1. Captura Génesis: `config/genesis_hash.json` -> SHA-256 inmutable.
2. Manifiesto 51/49: `cadena_sha256.txt` + `audit/*.pdf`.
3. Sellado: FOLIO `5204160405358537-N{1,2,3}-KRONOS-MT01JAAF-{timestamp}`.
4. Webhook: Verificación `x-signature` HMAC-SHA256 con `MP_WEBHOOK_SECRET`.
5. Entrega: PDF con membretes, QR verificación en `web/verification.html`.

## 3. Manejo de Secretos - 100/10
NUNCA se commitea:
- `.env` con `MP_ACCESS_TOKEN`, `MP_WEBHOOK_SECRET`, `SMTP_PASS`
- `audit/*.pdf` con datos de clientes
- `cola_reintento/`

Archivo `.env.example` obligatorio en repo como plantilla sin valores.

Uso de `load_dotenv()` + variables de entorno en `render.yaml`:
env: MP_ACCESS_TOKEN, MP_WEBHOOK_SECRET, SMTP_USER, SMTP_PASSjavascript
## 4. Reporte de Vulnerabilidades - Coordinated Disclosure
**NO abras Issues públicos con vulns.**

Envía correo a: `kronosproyecto@hotmail.com`

Asunto: `[SECURITY_VULN] KRONOS-MT01JAAF - <breve descripción>`

Incluye:
- FOLIO y SHA afectado
- Pasos para reproducir
- Impacto (RCE, leak PII, bypass HMAC, spoofing PDF)
- PoC si aplica

**SLA:** Respuesta 72h, fix 7 días, reconocimiento en `SECURITY.md` si autorizas.

## 5. Alcance
- `app.py` webhook `/webhook/mp` - Validación `x-signature`, `x-request-id`, `x-timestamp`
- `web/marketplace.html` - Links `init_point` MP
- `scripts/generar_links.py` y `actualizar_marketplace.py` - Generación con `external_reference`
- `audit/` - PDFs dictámenes con sello `KRONOS-TRACE-PVA`

## 6. Auditoria 100/10
Ejecutar antes de cada push:
```bash
python scripts/auditoria_borrado.py
pytest tests/test_auditoria_100_10.py -vDebe salir ✅ AUDITORIA 100/10 APROBADA - LUZ PRENDIDA OFFLINE.
7. Contacto Pericial
Perito Responsable: kronosproyecto@hotmail.comFolio Maestro: 5204160405358537Folio Pericial: KRONOS-MT01JAAFVerificación: https://marcorojas17.github.io/PVA-Protocolo-Vida-Autopoietica-/web/verification.html?folio=KRONOS-MT01JAAFDiseñado bajo ISO 27001:2022, ISO 27037:2012, eIDAS QSeal, NOM-151-SCFI-2016.
51% humano siempre mantiene autoridad final.
