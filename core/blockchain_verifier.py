#!/usr/bin/env python3
"""
Verificador de transacciones en Ethereum (Etherscan).
Devuelve True si la transacción existe, False en caso contrario.
Acepta un parámetro opcional `mock_response` para facilitar tests unitarios.
"""
import urllib.request
import json

def verify_on_etherscan(tx_hash: str, mock_response: dict = None) -> bool:
    if mock_response is not None:
        return mock_response.get("status") == "1" and mock_response.get("result") is not None

    url = f"https://api.etherscan.io/api?module=proxy&action=eth_getTransactionByHash&txhash={tx_hash}"
    try:
        with urllib.request.urlopen(url) as response:
            data = json.loads(response.read())
            return data.get("result") is not None
    except Exception:
        return False
