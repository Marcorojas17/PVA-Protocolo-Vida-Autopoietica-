# PVA - Protocolo Vida Autopoietica

**Sistema de certificación pericial con inteligencia artificial (51/49) y sellado blockchain.**

![Folio](https://img.shields.io/badge/Folio-5204160405358537-gold?style=for-the-badge)
![Perito](https://img.shields.io/badge/Perito-kronosproyecto%40hotmail.com-00A86B?style=for-the-badge)
![Genesis](https://img.shields.io/badge/Genesis-41a3683b-black?style=for-the-badge)
![SafeCreative](https://img.shields.io/badge/SafeCreative-2607146379465-blue?style=for-the-badge)
![PVA](https://img.shields.io/badge/PVA-51%25%20Humano%20%2F%2049%25%20IA-D4AF37)

PVA es un protocolo que combina criptografía, blockchain y un flujo de trabajo humano-IA para generar dictámenes periciales con validez legal ante normas internacionales como NOM-151 (México), eIDAS (Europa) y estándares ISO 27001.

> **Aviso:** Este sistema no sustituye la fe pública notarial. El dictamen generado es una prueba técnica criptográfica, respaldada por la firma FIEL del perito responsable y sellada en blockchain.

---

## ✨ Características principales

- **Generación de manifiestos 51/49:** El 51% del contenido es validado por un perito humano, y el 49% es generado por el motor algorítmico PVA.
- **Sellado pericial inmutable:** Cada dictamen lleva un folio único y es registrado en Ethereum (Red Sepolia/Mainnet) mediante un Smart Contract.
- **Auditoría transparente:** Todo el proceso queda documentado en `cadena_custodia.log` y puede verificarse mediante un código QR único.
- **Frontend Cyberpunk:** Interfaz web en JavaScript con estética KRONOS (verde #00A86B y oro #D4AF37) que se conecta a MetaMask para pagos y autenticación.
- **Pruebas automatizadas:** Pipeline CI/CD con `pytest`, `flake8` y `mypy` integrado.

---

## 🔎 Verificación pública

Valida cualquier dictamen en: **https://kronos-legado.digital/v/5204160405358537**

- SHA256 Génesis: `41a3683bbf83296eeb45da9b0e0ea5a7c095e78b493772e79520a92dbc39f4c3`
- TX Blockchain: `0x8ca8e84e1258abac9acb29d14d25114e4775d782ecfda51ae29933247ed2970e`
- SafeCreative: `2607146379465`

---

## 🚀 Instalación

### Opción 1: Clonar y usar localmente

```bash
git clone https://github.com/TU_USUARIO/PVA-Protocolo-Vida-Autopoietica.git
cd PVA-Protocolo-Vida-Autopoietica
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
pip install -r requirements.txt
pip install -e .
cp .env.example .env
PVA-Protocolo-Vida-Autopoietica/
├── core/           # Motor principal (hash, perito, blockchain)
├── web/            # Frontend Cyberpunk (HTML/CSS/JS)
├── scripts/        # Utilidades de generación y despliegue
├── contracts/      # Smart Contract Solidity
├── audit/          # Dictámenes generados (carpeta que se vende)
├── tests/          # Pruebas unitarias
├── docs/           # Documentación legal y técnica
└── ...
pytest tests/ -v
python scripts/generate_manifesto.py --hash "HASH_GENESIS" --folio "5204160405358537"
python scripts/generate_pdf_dictamen.py --input audit/sello_kronos.json
python scripts/deploy_contract.py

---

### ✅ Lo que sigue
Con este README tu repositorio ya tiene la cara comercial, el blindaje legal y el verificador público en la portada. Cuando lo hayas pegado, avísame y generamos el **`marketplace.html`** con Stripe para que empieces a cobrar. ¡Lo dejamos aquí o seguimos?
