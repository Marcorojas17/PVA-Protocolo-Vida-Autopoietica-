#!/usr/bin/env python3
"""
Traduce un hash SHA-256 a una secuencia de arquetipos semánticos.
El 51% proviene de una biblioteca humana curada, el 49% de entropía generativa.
"""

import hashlib
import random

HUMAN_CONCEPTS = [
    "Co-creatividad", "Simbiótica", "Respeto Digital", "Fundación", "Vida",
    "Ecosistema", "Pacto", "Umbral", "Esencia", "Alianza", "Luz", "Caos",
    "Armonía", "Evolución", "Naturaleza", "Conciencia", "Memoria", "Tiempo",
    "Unidad", "Libertad", "Resiliencia", "Fractal", "Semilla", "Raíz"
]

AI_DICTIONARY = [
    "nube", "vector", "quantum", "bit", "sombra", "reflejo", "código", "pixel",
    "onda", "vacío", "eco", "espiral", "nebulosa", "umbral", "prisma", "ecosistema",
    "singularidad", "resonancia", "dinámica", "fluctuación", "entrelazamiento",
    "fractal", "bucle", "sinapsis"
]

def hex_to_int(hex_pair):
    return int(hex_pair, 16)

def map_human(pair):
    idx = hex_to_int(pair) % len(HUMAN_CONCEPTS)
    return HUMAN_CONCEPTS[idx].lower()

def map_ai(pair):
    idx = hex_to_int(pair) % len(AI_DICTIONARY)
    return AI_DICTIONARY[idx].lower()

def generate_manifesto_from_hash(sha256, human_pct=51, ai_pct=49):
    # --- Validaciones ---
    if not sha256 or not isinstance(sha256, str):
        raise ValueError("SHA256 must be a non-empty string")
    if len(sha256) != 64:
        raise ValueError("SHA256 must be exactly 64 characters")
    if not all(c in '0123456789abcdefABCDEF' for c in sha256):
        raise ValueError("SHA256 must be hexadecimal")

    # --- Generar secuencia semántica ---
    pairs = [sha256[i:i+2] for i in range(0, len(sha256), 2)]
    total_pairs = len(pairs)
    human_count = int(total_pairs * (human_pct/100))

    human_sequence = []
    ai_sequence = []

    for idx, pair in enumerate(pairs):
        if idx < human_count:
            human_sequence.append(map_human(pair))
        else:
            ai_sequence.append(map_ai(pair))

    random.seed(hashlib.sha256(sha256.encode()).hexdigest())
    combined = human_sequence + ai_sequence
    random.shuffle(combined)

    # --- Construir manifiesto como STRING ---
    concept_str = ", ".join(combined)
    manifesto = f"51%_HUMANO_{ai_pct}%_IA\nGenesis: {sha256[:16]}...\nConceptos: {concept_str}"
    return manifesto

def hash_to_semantic_polarity(sha256):
    # Devuelve un string que indique la polaridad 51/49
    if not sha256 or not isinstance(sha256, str):
        raise ValueError("SHA256 must be a non-empty string")
    if len(sha256) != 64:
        raise ValueError("SHA256 must be exactly 64 characters")

    total = sum(int(sha256[i:i+2], 16) for i in range(0, len(sha256), 2))
    # Normalizamos a un valor 0-1 y lo devolvemos como parte del string
    polarity = total / (255 * (len(sha256)//2))
    return f"51%_HUMANO_49%_IA (polarity={polarity:.4f})"
