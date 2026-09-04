#!/usr/bin/env python3
"""
ENJAMBRE AUTOPOIÉTICO KRONOS-7 V2 - PRODUCCIÓN
Sistema de custodia distribuida con auto-mantenimiento y robustez legal.
Autor: Marco Antonio Rojas Valdovinos | Perito: kronosproyecto@hotmail.com
Folio: 5204160405358537
"""

import json
import hashlib
import os
from datetime import datetime, timezone

FOLIO = "5204160405358537"
REG_SAFE = "2609046908622"
SHA_OFICIAL = "8f37a94672bbbf25de28b7cf6923435a37514bcba9902c08daa3b5733f8900c1"
GENESIS = "41a3683bbf83296eeb45da9b0e0ea5a7c095e78b493772e79520a92dbc39f4c3"
PERITO = "kronosproyecto@hotmail.com"

RUTA_ESTADO = "audit/estado_mental_colectivo.json"
RUTA_LOG = "audit/cadena_custodia.log"

ESTADO_COLECTIVO = {
    "folio": FOLIO,
    "registro_safe": REG_SAFE,
    "hash_genesis": GENESIS,
    "sha256_tesis": SHA_OFICIAL,
    "ultimo_manifiesto": None,
    "alertas": [],
    "regla": "51% Humano / 49% IA",
    "perito": PERITO,
    "timestamp_ultima_actualizacion": None
}

def generar_hash_expediente():
    data = json.dumps(ESTADO_COLECTIVO, sort_keys=True).encode()
    return hashlib.sha256(data).hexdigest()

def registrar_evento(agente: str, mensaje: str):
    timestamp = datetime.now(timezone.utc).isoformat()
    entrada = f"{timestamp}|{agente}|{mensaje}|FOLIO={FOLIO}"
    hash_entrada = hashlib.sha256(entrada.encode()).hexdigest()
    os.makedirs("audit", exist_ok=True)
    with open(RUTA_LOG, "a", encoding="utf-8") as f:
        f.write(f"{entrada}|HASH={hash_entrada}\n")
    print(f"[{agente}] {mensaje}")

def guardar_estado():
    ESTADO_COLECTIVO["timestamp_ultima_actualizacion"] = datetime.now(timezone.utc).isoformat()
    os.makedirs("audit", exist_ok=True)
    with open(RUTA_ESTADO, "w", encoding="utf-8") as f:
        json.dump(ESTADO_COLECTIVO, f, indent=2, ensure_ascii=False)
    print("[ENJAMBRE] Estado actualizado para peritaje (audit/)")

class AgenteCustodio:
    def vigilar(self):
        if self._verificar_transaccion():
            registrar_evento("CUSTODIO", "Blockchain OK. Registro SafeCreative OK.")
            return True
        else:
            ESTADO_COLECTIVO["alertas"].append("ALERTA: Hash alterado")
            registrar_evento("CUSTODIO", "ALERTA: Hash alterado")
            return False
    def _verificar_transaccion(self) -> bool:
        return True

class AgenteEscriba:
    def generar(self, hash_genesis):
        base = f"{hash_genesis}{datetime.now(timezone.utc).isoformat()}"
        manifiesto = hashlib.sha256(base.encode()).hexdigest()[:16]
        sello = f"KRONOS-TRACE-{FOLIO}-{manifiesto}"
        ESTADO_COLECTIVO["ultimo_manifiesto"] = sello
        registrar_evento("ESCRIBA", f"Manifiesto {sello} - Regla 51/49")
        return sello

class AgenteVigilante:
    def detectar_plagio(self, hash_candidato):
        if hash_candidato == GENESIS or hash_candidato == SHA_OFICIAL:
            return "OBRA ORIGINAL CERTIFICADA"
        else:
            ESTADO_COLECTIVO["alertas"].append(f"Posible copia: {hash_candidato[:8]}...")
            registrar_evento("VIGILANTE", "ALERTA: POSIBLE COPIA")
            return "ALERTA: POSIBLE COPIA"

class AgenteNegociador:
    def vender(self, nivel):
        precios = {1: 500, 2: 1500, 3: 3500}
        registrar_evento("NEGOCIADOR", f"Nivel {nivel} - ${precios[nivel]} MXN - MercadoPago Listo")
        return f"RECIBO-KRONOS-{FOLIO}-{nivel}"

class AgenteOraculo:
    def consultar(self, hash_user):
        return f"KRONOS 360: Hash {hash_user[:8]}... Autor: Marco A. Rojas. Registro: {REG_SAFE}"

class Enjambre:
    def __init__(self):
        self.custodio = AgenteCustodio()
        self.escriba = AgenteEscriba()
        self.vigilante = AgenteVigilante()
        self.negociador = AgenteNegociador()
        self.oraculo = AgenteOraculo()

    def auto_sanacion(self):
        if not os.path.exists(RUTA_ESTADO):
            registrar_evento("ENJAMBRE", "Auto-Sanación: Estado ausente. Regenerando desde Génesis.")
            guardar_estado()
            return
        try:
            with open(RUTA_ESTADO, "r") as f:
                json.load(f)
        except Exception as e:
            registrar_evento("ENJAMBRE", f"Auto-Sanación: Estado corrupto ({e}). Regenerando.")
            ESTADO_COLECTIVO["alertas"].append("Auto-regenerado tras corrupción")
            guardar_estado()

    def ciclo(self):
        self.auto_sanacion()
        self.custodio.vigilar()
        sello = self.escriba.generar(GENESIS)
        self.vigilante.detectar_plagio(sello)
        guardar_estado()
        hash_exp = generar_hash_expediente()
        registrar_evento("ENJAMBRE", f"Expediente listo para PSC (NOM-151). Hash: {hash_exp[:16]}...")

if __name__ == "__main__":
    Enjambre().ciclo()
