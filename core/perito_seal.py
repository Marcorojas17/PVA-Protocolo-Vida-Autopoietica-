FOLIO = "5204160405358537"
PERITO = "kronosproyecto@hotmail.com"

def generar_sello_kronos(genesis_hash: str, folio: str = None, perito: str = None) -> str:
    f = folio or FOLIO
    p = perito or PERITO
    g = genesis_hash
    # Formato EXACTO exigido por test_sello_formato_kronos: 3 partes
    # FOLIO:xxx|PERITO:xxx|GENESIS:xxx
    return f"FOLIO:{f}|PERITO:{p}|GENESIS:{g}"
