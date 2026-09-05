"""
hash_to_semantic - MT01JAAF SHA a4ff808e
"""

FOLIO_PERICIAL = "KRONOS-MT01JAAF"
SHA = "a4ff808e"

def generate_manifesto_from_hash(genesis: str, humano: int = 51, ia: int = 49) -> str:
    sha = genesis[:8] if genesis else SHA
    return f"{humano}%_HUMANO:{genesis[:32]}|{ia}%_IA:{genesis[32:]}|FOLIO_PERICIAL:{FOLIO_PERICIAL}|SHA:{sha}|MT01JAAF|TRACE:KRONOS-TRACE-PVA-5204160405358537-MT01JAAF|SC:2607146379465|POLARIDAD:{humano}/{ia}"
