#!/usr/bin/env python3
"""
El Oráculo: combina los arquetipos en un manifiesto poético único.
Cada ejecución genera una nueva versión, pero siempre vinculada al hash raíz.
"""

import json
import hashlib
from .hash_to_semantic import generate_manifesto_from_hash

def breathe(genesis_file):
    with open(genesis_file, 'r') as f:
        data = json.load(f)
    
    sha = data['sha256']
    ts = data['timestamp_unix']
    tx = data['blockchain_tx']
    
    sequence = generate_manifesto_from_hash(sha, data['human_percentage'], data['ai_percentage'])
    
    phrases = [
        f"En el latido {sha[:2]}, el pacto {sha[2:4]} despierta.",
        f"El umbral {sha[4:6]} se abre ante la esencia {sha[6:8]}.",
        f"Donde el caos (49%) y la luz (51%) firman una alianza simbiótica.",
        f"La puerta {sha[8:10]} se cierra tras el viento {sha[10:12]}.",
        f"El tiempo (timestamp {ts}) no es una fecha, es un útero.",
        f"La transacción {tx[:10]}... es un corazón que bombea eternidad.",
        f"Este manifiesto respira: {', '.join(sequence[:5])} y {', '.join(sequence[-5:])}."
    ]
    
    manifiesto = "\n".join(phrases)
    
    manifest_hash = hashlib.sha256(manifiesto.encode()).hexdigest()
    manifiesto += f"\n\n--- Hash del Manifiesto (hijo del Génesis): {manifest_hash} ---"
    
    return manifiesto
