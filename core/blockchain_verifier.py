FOLIO = "5204160405358537"

def verify_on_etherscan(tx_hash: str, etherscan_response: dict) -> bool:
    try:
        if not etherscan_response or not isinstance(etherscan_response, dict):
            return False
        if etherscan_response.get("status") != "1":
            return False
        if etherscan_response.get("message") != "OK":
            return False
        result = etherscan_response.get("result")
        if not isinstance(result, dict):
            return False
        if result.get("isError") == "1":
            return False
        return True
    except:
        return False
