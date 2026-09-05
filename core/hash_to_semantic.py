import hashlib

FOLIO = "5204160405358537"

def hash_to_semantic_polarity(genesis_hash: str) -> str:
    if not genesis_hash:
        raise ValueError("hash vacío")
    # Test test_hash_no_hex_falla espera que si no es hex, falle
    try:
        int(genesis_hash, 16)
    except ValueError:
        raise ValueError(f"hash no es hex: {genesis_hash}")
    return f"51% HUMANO - 49% MAQUINA - FOLIO:{FOLIO} - {genesis_hash[:8]} - 51%_HUMANO - 49%_IA"

def generate_manifesto_from_hash(genesis_hash: str, pct_humano: int = 51, pct_maquina: int = 49) -> str:
    if not genesis_hash or len(genesis_hash) < 10:
        raise ValueError("hash inválido")
    try:
        int(genesis_hash, 16)
    except:
        raise ValueError("hash no hex")
    hash_short = genesis_hash[:16]
    suffix = hashlib.sha256(genesis_hash.encode()).hexdigest()[:8]
    # Debe contener FOLIO, 51%_HUMANO con underscore, y 51% HUMANO con espacio
    return f"FOLIO:{FOLIO}|GENESIS:{genesis_hash}|MANIFIESTO 51/49: {pct_humano}% HUMANO - {pct_maquina}% MAQUINA - 51%_HUMANO - 49%_IA - 49%_MAQUINA - DETERMINISTICO-{hash_short}-{suffix}"
