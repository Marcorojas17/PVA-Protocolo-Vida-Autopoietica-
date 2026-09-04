#!/usr/bin/env python3
"""
Verificador de la existencia en Ethereum (etherscan.io).
Solo funciona si la transacción ya está minada.
"""

import urllib.request
import json

def verify_on_etherscan(tx_hash):
    url = f"https://api.etherscan.io/api?module=proxy&action=eth_getTransactionByHash&txhash={tx_hash}"
    try:
        with urllib.request.urlopen(url) as response:
            data = json.loads(response.read())
            if data['result'] is not None:
                return True, data['result']['blockNumber']
            else:
                return False, None
    except Exception as e:
        return False, str(e)
