FOLIO = "5204160405358537"
PERITO = "kronosproyecto@hotmail.com"

def generar_sello_kronos(genesis_hash: str, folio: str = None, perito: str = None) -> str:
    f = folio or FOLIO
    p = perito or PERITO
    g = genesis_hash
    # Formato exigido: FOLIO:xxx|PERITO:xxx|GENESIS:xxx
    # Incluye genesis completo para que 1 char alterado cambie sello
    return f"FOLIO:{f}|PERITO:{p}|GENESIS:{g}|SELLO:KRONOS-TRACE-PVA-{f}-{g}"
