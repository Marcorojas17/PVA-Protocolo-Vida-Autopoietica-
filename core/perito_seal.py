def generar_sello_kronos(folio: str, hash_genesis: str = "") -> str:
    return f"KRONOS-TRACE-PVA-{folio}-{hash_genesis[:8] if hash_genesis else 'GENESIS'}"
