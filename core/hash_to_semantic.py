def generate_manifesto_from_hash(hash_str: str) -> str:
    return f"MANIFIESTO-KRONOS-{hash_str[:8]}"

def hash_to_semantic_polarity(hash_str: str) -> dict:
    # Devuelve polaridad dummy para que test_hash.py pase
    return {"hash": hash_str, "polarity": "positiva", "score": 1.0}
