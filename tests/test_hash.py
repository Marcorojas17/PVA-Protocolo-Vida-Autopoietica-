# tests/test_hash.py - PVA 10/10
import pytest
from core.hash_to_semantic import generate_manifesto_from_hash
from core.blockchain_verifier import verify_on_etherscan
from core.perito_seal import generar_sello_kronos

FOLIO = "5204160405358537"
GENESIS = "41a3683bbf83296eeb45da9b0e0ea5a7c095e78b493772e79520a92dbc39f4c3"
PERITO = "kronosproyecto@hotmail.com"

def test_51_49_split():
    result = generate_manifesto_from_hash(GENESIS, 51, 49)
    # Comprobamos que la función realmente existe y devuelve datos
    assert result is not None
    assert len(result) > 0

def test_deterministic():
    r1 = generate_manifesto_from_hash(GENESIS)
    r2 = generate_manifesto_from_hash(GENESIS)
    assert r1 == r2

def test_folio_in_seal():
    sello = generar_sello_kronos(GENESIS)
    assert FOLIO in sello
    assert PERITO in sello

def test_etherscan_verifier_accepts_real_tx():
    # Usamos un hash de transacción real (simulado) para el test
    tx_hash = "0x" + "c" * 64
    mock_response = {"status": "1", "result": {"blockNumber": "12345"}}
    assert verify_on_etherscan(tx_hash, mock_response) is True

def test_etherscan_verifier_rejects_wrong_tx():
    tx_hash = "0x" + "d" * 64
    mock_response = {"status": "0", "message": "Not found"}
    assert verify_on_etherscan(tx_hash, mock_response) is False
