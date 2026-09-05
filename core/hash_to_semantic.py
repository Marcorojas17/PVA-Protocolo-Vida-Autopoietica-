import hashlib

FOLIO = "5204160405358537"

def hash_to_semantic_polarity(genesis_hash: str) -> str:
    if not genesis_hash:
        raise ValueError("hash vacío")
    return f"51% HUMANO - 49% MAQUINA - POLARIDAD FOLIO:{FOLIO} - {genesis_hash[:8]} - HUMANO"

def generate_manifesto_from_hash(genesis_hash: str, pct_humano: int = 51, pct_maquina: int = 49) -> str:
    if not genesis_hash or len(genesis_hash) < 10:
        raise ValueError("hash inválido")
    hash_short = genesis_hash[:16]
    suffix = hashlib.sha256(genesis_hash.encode()).hexdigest()[:8]
    return f"FOLIO:{FOLIO}|GENESIS:{genesis_hash}|MANIFIESTO 51/49: {pct_humano}% HUMANO - {pct_maquina}% MAQUINA - DETERMINISTICO-{hash_short}-{suffix} - 51% HUMANO"
