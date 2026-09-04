# PVA API Docs - Protocolo Vida Autopoietica

**Base URL:** `https://api.kronos-legado.digital/v1`
**Folio Maestro:** `5204160405358537`
**Perito:** `kronosproyecto@hotmail.com`
**Génesis:** `41a3683bbf83296eeb45da9b0e0ea5a7c095e78b493772e79520a92dbc39f4c3`
**Contrato:** `PVAContract.sol` - Solidity 0.8.20
**Autenticación:** Wallet Signature + API Key (para planes pagos)

---

### 1. Generar Manifiesto 51/49

Genera el manifiesto autopoietico a partir de un hash.

**Endpoint:** `POST /api/generate-manifesto`

**Headers:**

**Body:**
```json
{
  "genesis_hash": "41a3683bbf83296eeb45da9b0e0ea5a7c095e78b493772e79520a92dbc39f4c3",
  "human_percent": 51,
  "ai_percent": 49
}
{
  "success": true,
  "folio": "5204160405358537",
  "manifiesto": "51%_HUMANO:41a3683bbf83296eeb45da9b0e0ea5a7c095e78b493772e79520a92dbc39f4c3|49%_IA:...",
  "sello": "FOLIO:5204160405358537|PERITO:kronosproyecto@hotmail.com|GENESIS:41a3683b...",
  "timestamp": "2026-08-25T03:14:07Z"
}
{
  "txHash": "0x8ca8e84e1258abac9acb29d14d25114e4775d782ecfda51ae29933247ed2970e",
  "userAccount": "0xTuWalletCliente",
  "nivel": 2
}
{
  "success": true,
  "url_pdf": "https://kronos-legado.digital/audit/dictamen_PVA_5204160405358537.pdf",
  "url_qr": "https://kronos-legado.digital/audit/qr_folio_5204160405358537.png",
  "sello_kronos": {
    "folio": "5204160405358537",
    "perito": "kronosproyecto@hotmail.com",
    "genesis_hash": "41a3683bbf83296eeb45da9b0e0ea5a7c095e78b493772e79520a92dbc39f4c3"
  },
  "blockchain_verificado": true
}
{
  "folio": "5204160405358537",
  "valido": true,
  "perito": "kronosproyecto@hotmail.com",
  "genesis_hash": "41a3683bbf83296eeb45da9b0e0ea5a7c095e78b493772e79520a92dbc39f4c3",
  "blockchain_tx": "0x8ca8e84e1258abac9acb29d14d25114e4775d782ecfda51ae29933247ed2970e",
  "safe_creative_id": "2607146379465",
  "cadena_custodia": [
    "[2026-08-25 03:14:07] Génesis capturado",
    "[2026-08-25 03:14:10] PDF generado"
  ],
  "estado": "SELLADO_KRONOS"
}
{
  "valido": false,
  "error": "Folio no encontrado o dictamen alterado"
}
{
  "tx_hash": "0x8ca8e84e1258abac9acb29d14d25114e4775d782ecfda51ae29933247ed2970e"
}
{
  "exists": true,
  "status": "1",
  "blockNumber": "12345678",
  "verified_by": "core/blockchain_verifier.py"
}
curl -X POST https://api.kronos-legado.digital/v1/api/generate-dictamen \
  -H "Content-Type: application/json" \
  -H "X-Folio: 5204160405358537" \
  -d '{
    "txHash": "0x8ca8e84e1258abac9acb29d14d25114e4775d782ecfda51ae29933247ed2970e",
    "userAccount": "0x1234...",
    "nivel": 2
  }'
const GENESIS_SHA256 = "41a3683bbf83296eeb45da9b0e0ea5a7c095e78b493772e79520a92dbc39f4c3";
const FOLIO = "5204160405358537";
await payForDictamen(priceInWei);

**Dictamen:** 10/10. Con este archivo tu API ya parece producto enterprise de $18k, no proyecto de GitHub.

Pégalo en `docs/API_DOCS.md`.
