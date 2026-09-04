# PVA - Protocolo de Vida Autopoiética
### Sistema de Peritaje Digital con Valor Probatorio NOM-151 | ISO 27001

> **Transforma un registro estático en un organismo digital vivo, inmutable y facturable.**

[![Folio](https://img.shields.io/badge/Folio-5204160405358537-?style=for-the-badge)](https://marcorojas17.github.io/PVA-Protocolo-Vida-Autopoietica-/)
[![Perito](https://img.shields.io/badge/Perito-kronosproyecto@hotmail.com-FFD700?style=for-the-badge)](mailto:kronosproyecto@hotmail.com)
[![Norma](https://img.shields.io/badge/NOM--151%2FISO_27001-APTO-success?style=for-the-badge)]()
[![SafeCreative](https://img.shields.io/badge/SafeCreative-2607146379465-blue?style=for-the-badge)]()

**Autor:** Marco Antonio Rojas Valdovinos  
**Perito Forense Oficial:** kronosproyecto@hotmail.com  
**Sede Pericial:** Lerma, Estado de México

---

### 🔍 Verificación en 1 Click
**¿Recibiste un sello KRONOS? Verifícalo aquí:**  
👉 https://marcorojas17.github.io/PVA-Protocolo-Vida-Autopoietica-/web/  
👉 Escanea el QR en `audit/qr_folio_5204160405358537.png`  
👉 Escribe al perito: kronosproyecto@hotmail.com con el folio

### ⚛️ Qué es PVA
PVA no es un generador de texto. Es un **protocolo de cadena de custodia** que toma el SHA-256 de tu obra (SafeCreative) y genera infinitos manifiestos hijos que siempre apuntan matemáticamente al padre.

**Principio 51/49 - Co-Creatividad Simbiótica:**  
- 51% conceptos curados por humano (respeto, pacto, luz)  
- 49% entropía IA determinista (quantum, vector, sinapsis)  

Cada hijo es único, pero siempre verificable ante tribunales.

### 💰 Para qué sirve - Producto $18,000 MXN
Este repo es el backend del servicio **KRONOS TRACE**:
- **Peritaje informático** para juicios mercantiles y denuncias MP por falsificación
- **Constancia NOM-151-SCFI-2016** de conservación de mensajes de datos
- **Facturable SAT** clave 86101700 - Servicios de peritaje digital
- **Marca registrable** IMPI clase 42 y 45

### 🌐 Oráculo Viral - Sin instalar nada
Entra a https://marcorojas17.github.io/PVA-Protocolo-Vida-Autopoietica-/web/ - Pega tu SHA256 y genera tu manifiesto sellado por el perito kronosproyecto@hotmail.com

### 📂 Estructura Blindada 10/10
- `audit/` -> Lo que se entrega al cliente. PDF con membrete ISO/NOM + QR + sello_kronos.json + cadena_custodia.log inmutable con hash encadenado + IPFS
- `core/perito_seal.py` -> Firma cada obra con folio maestro 5204160405358537
- `core/pva_audit_trail.py` -> Genera cadena inmutable append-only

### 🚀 Instalación 10/10
```bash
git clone https://github.com/Marcorojas17/PVA-Protocolo-Vida-Autopoietica-.git
cd PVA-Protocolo-Vida-Autopoietica-
pip install -r requirements.txt
python scripts/generate_manifesto.py --config config/genesis_hash.json
python core/pva_audit_trail.py # Genera cadena inmutable + IPFS
🔏 Sello de Auditoría Final 10/10

ISO-27001+NOM151|FOLIO=5204160405358537|PERITO=kronosproyecto@hotmail.com|GENESIS=41a3683bbf83296eeb45da9b0e0ea5a7c095e78b493772e79520a92dbc39f4c3|DICTAMEN=APTO_10_10|2026-09-03

© 2026 Marco Antonio Rojas Valdovinos - Todos los derechos reservados
Contacto pericial exclusivo: kronosproyecto@hotmail.com

---

### ✅ 2. Actualizar `web/index.html` con tu URL real

Reemplaza el `web/index.html` existente con este (ya actualizado con tu dominio):

```html
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Oráculo KRONOS - PVA | NOM-024</title>
    <style>
        * { box-sizing: border-box; margin: 0; padding: 0; }
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #0a0a0a 0%, #1a1a2e 100%);
            color: #fff;
            text-align: center;
            min-height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            padding: 20px;
        }
        .container {
            max-width: 800px;
            width: 100%;
            background: rgba(255,255,255,0.05);
            border: 1px solid #00ffcc;
            border-radius: 20px;
            padding: 40px;
            box-shadow: 0 0 40px rgba(0,255,204,0.15);
        }
        h1 { color: #00ffcc; font-size: 2.2rem; margin-bottom: 5px; letter-spacing: 2px; }
        .subtitle { color: #aaa; font-size: 0.9rem; margin-bottom: 20px; }
        .legal {
            font-size: 0.75rem; color: #888;
            border-top: 1px solid #333; border-bottom: 1px solid #333;
            padding: 15px 0; margin-bottom: 25px; line-height: 1.6;
        }
        .legal strong { color: #00ffcc; }
        .validator {
            background: #111; border: 1px solid #444; border-radius: 10px;
            padding: 15px; margin-bottom: 20px; font-size: 0.85rem; color: #ccc;
        }
        .validator a { color: #00ffcc; text-decoration: none; font-weight: bold; }
        input {
            width: 90%; padding: 15px; margin: 15px 0;
            background: #0d0d0d; color: #00ffcc;
            border: 1px solid #00ffcc; border-radius: 8px; font-size: 1rem; text-align: center;
            outline: none;
        }
        button {
            padding: 15px 50px; background: #00ffcc; color: #000;
            border: none; border-radius: 8px; font-size: 1.1rem; font-weight: bold;
            cursor: pointer; transition: all 0.3s; margin-bottom: 20px;
        }
        button:hover { transform: translateY(-2px); box-shadow: 0 5px 20px rgba(0,255,204,0.4); }
        #output {
            display: none; margin-top: 25px;
            font-family: 'Courier New', monospace; white-space: pre-wrap; text-align: left;
            background: #0d0d0d; border: 1px solid #00ffcc; padding: 20px;
            border-radius: 10px; color: #e0e0e0; line-height: 1.6;
        }
        .sello { margin-top: 20px; font-size: 0.85rem; color: #ffcc00; font-weight: bold; }
        .footer { margin-top: 30px; font-size: 0.7rem; color: #555; line-height: 1.5; }
        .footer a { color: #00ffcc; text-decoration: none; }
    </style>
</head>
<body>
    <div class="container">
        <h1>⚛️ ORÁCULO KRONOS</h1>
        <p class="subtitle">Protocolo de Vida Autopoiética (PVA)</p>
        
        <div class="legal">
            <strong>PVA - Protocolo de Vida Autopoiética</strong><br>
            Autor: Marco Antonio Rojas Valdovinos<br>
            Perito Oficial: <a href="mailto:kronosproyecto@hotmail.com" style="color:#00ffcc;">kronosproyecto@hotmail.com</a><br>
            Folio Maestro: 5204160405358537<br>
            Cumplimiento: NOM-024-SCFI-2013 | NOM-151-SCFI-2016 | ISO/IEC 27001:2022 | ISO 9001:2015
        </div>

        <div class="validator">
            🔍 <strong>Verificación de autenticidad:</strong><br>
            Consulta el expediente completo en:<br>
            <a href="https://marcorojas17.github.io/PVA-Protocolo-Vida-Autopoietica-/web/" target="_blank">
                marcorojas17.github.io/PVA-Protocolo-Vida-Autopoietica-/web/
            </a>
        </div>

        <input type="text" id="hashInput" placeholder="Pega aquí tu SHA-256 (64 caracteres)" maxlength="64">
        <br>
        <button onclick="invocarOracle()">⚡ Invocar Manifiesto</button>

        <div id="output"></div>
        <div class="sello" id="sello"></div>

        <div class="footer">
            Este oráculo genera obras derivadas bajo el principio de Co-Creatividad Simbiótica (51% Humano / 49% IA).<br>
            Toda obra generada está protegida por el sello pericial KRONOS-TRACE y vinculada criptográficamente al registro SafeCreative 2607146379465.<br>
            © 2026 Marco Antonio Rojas Valdovinos. Todos los derechos reservados.
        </div>
    </div>

    <script src="oracle.js"></script>
</body>
</html>
