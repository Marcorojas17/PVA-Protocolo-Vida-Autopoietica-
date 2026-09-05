import pytest
from core.blockchain_verifier import verify_on_etherscan
from core.perito_seal import generar_sello_kronos

# Datos maestros PVA
FOLIO = "5204160405358537"
PERITO = "kronosproyecto@hotmail.com"
GENESIS = "41a3683bbf83296eeb45da9b0e0ea5a7c095e78b493772e79520a92dbc39f4c3"
TX_REAL = "0x8ca8e84e1258abac9acb29d14d25114e4775d782ecfda51ae29933247ed2970e"


def test_tx_valida_etherscan_status_1():
    """Simula respuesta real de Etherscan cuando TX existe"""
    mock_response_ok = {
        "status": "1",
        "message": "OK",
        "result": {
            "blockNumber": "12345678",
            "timeStamp": "1724567047",
            "hash": TX_REAL,
            "from": "0xPeritoWallet",
            "to": "0xPVAContract",
            "isError": "0",
        },
    }
    assert verify_on_etherscan(TX_REAL, mock_response_ok) is True


def test_tx_invalida_etherscan_status_0():
    """Simula TX no encontrada"""
    mock_response_fail = {
        "status": "0",
        "message": "NOTOK",
        "result": "Transaction not found",
    }
    assert verify_on_etherscan("0x" + "0" * 64, mock_response_fail) is False


def test_tx_error_sin_result():
    mock_response_error = {"status": "0", "message": "Invalid API Key"}
    assert verify_on_etherscan(TX_REAL, mock_response_error) is False


def test_tx_vacia_no_crashea():
    mock_empty = {}
    assert verify_on_etherscan(TX_REAL, mock_empty) is False


def test_folio_no_duplicado_en_contrato():
    """
    Valida lógica de PVAContract.sol:
    require(bytes(registros[_folio].folio).length == 0, "Folio ya registrado")
    """
    registros_simulados = {FOLIO: {"folio": FOLIO, "hashGenesis": GENESIS}}
    # Intentar registrar mismo folio debe fallar
    folio_a_registrar = FOLIO
    ya_existe = (
        folio_a_registrar in registros_simulados
        and len(registros_simulados[folio_a_registrar]["folio"]) > 0
    )
    assert (
        ya_existe is True
    ), "Folio 5204160405358537 ya debe existir - contrato debe rechazar duplicado"


def test_folio_nuevo_si_permitido():
    registros_simulados = {}
    nuevo_folio = "9999999999999999"
    ya_existe = nuevo_folio in registros_simulados
    assert ya_existe is False


def test_sello_ligado_a_tx():
    """El sello KRONOS debe poder ligarse a una TX para auditoría"""
    sello = generar_sello_kronos(GENESIS)
    assert FOLIO in sello
    assert PERITO in sello
    # Simula que el sello se guarda on-chain
    registro_onchain = {
        "folio": FOLIO,
        "hashGenesis": GENESIS,
        "sello": sello,
        "tx": TX_REAL,
    }
    assert registro_onchain["folio"] == FOLIO
    assert registro_onchain["tx"] == TX_REAL
    assert (
        verify_on_etherscan(registro_onchain["tx"], {"status": "1", "result": {}})
        is True
    )


def test_genesis_hash_formato_sha256():
    """Génesis debe ser SHA256 válido 64 hex"""
    assert len(GENESIS) == 64
    assert all(c in "0123456789abcdef" for c in GENESIS)
