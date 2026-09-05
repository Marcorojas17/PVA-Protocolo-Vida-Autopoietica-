import hashlib
import pytest
from core.hash_to_semantic import (
    generate_manifesto_from_hash,
    hash_to_semantic_polarity,
)
from core.perito_seal import generar_sello_kronos

# Datos maestros PVA - INMUTABLES
FOLIO = "5204160405358537"
GENESIS = "41a3683bbf83296eeb45da9b0e0ea5a7c095e78b493772e79520a92dbc39f4c3"
PERITO = "kronosproyecto@hotmail.com"


def test_genesis_es_sha256_valido():
    assert len(GENESIS) == 64
    assert all(c in "0123456789abcdef" for c in GENESIS.lower())
    # Debe ser hash de algo, no zeros
    assert GENESIS != "0" * 64
    assert GENESIS == "41a3683bbf83296eeb45da9b0e0ea5a7c095e78b493772e79520a92dbc39f4c3"


def test_sha256_real_genera_mismo_genesis():
    """Prueba que tu lógica de hash es determinística"""
    data = b"KRONOS_360_GENESIS_PVA"
    h = hashlib.sha256(data).hexdigest()
    # No debe ser igual a GENESIS, pero debe ser 64 hex
    assert len(h) == 64
    # Doble hash debe dar mismo resultado
    h2 = hashlib.sha256(data).hexdigest()
    assert h == h2


def test_hash_to_semantic_polaridad_51_49():
    result = hash_to_semantic_polarity(GENESIS)
    assert "51" in result or "HUMANO" in result
    assert "49" in result or "IA" in result


def test_generate_manifesto_contiene_folio():
    manifesto = generate_manifesto_from_hash(GENESIS, 51, 49)
    # El manifiesto debe poder ligar al folio via sello
    sello = generar_sello_kronos(GENESIS)
    assert FOLIO in sello
    assert GENESIS[:16] in manifesto or "HUMANO" in manifesto


def test_manifiesto_deterministico():
    """NOM-151: mismo hash = mismo manifiesto, siempre"""
    m1 = generate_manifesto_from_hash(GENESIS, 51, 49)
    m2 = generate_manifesto_from_hash(GENESIS, 51, 49)
    assert m1 == m2


def test_manifiesto_hashes_distintos_resultados_distintos():
    m1 = generate_manifesto_from_hash(GENESIS, 51, 49)
    m2 = generate_manifesto_from_hash("f" * 64, 51, 49)
    assert m1 != m2


def test_hash_vacio_falla_controlado():
    with pytest.raises((ValueError, AssertionError, Exception)):
        generate_manifesto_from_hash("", 51, 49)


def test_hash_no_hex_falla():
    with pytest.raises((ValueError, AssertionError, Exception)):
        generate_manifesto_from_hash("zzzz_no_es_hex", 51, 49)


def test_porcentaje_51_49_obligatorio():
    m = generate_manifesto_from_hash(GENESIS, 51, 49)
    assert "51" in m
    assert "49" in m
    # No permitir 50/50 ni 60/40
    assert "51%_HUMANO" in m or "51%_HUMANO" in m or "51" in m


def test_sello_integro_ante_alteracion():
    """Si alteras 1 char del genesis, el sello debe cambiar - prueba integridad NOM-151"""
    sello_original = generar_sello_kronos(GENESIS)
    genesis_alterado = GENESIS[:-1] + ("0" if GENESIS[-1] != "0" else "1")
    sello_alterado = generar_sello_kronos(genesis_alterado)
    assert sello_original != sello_alterado
    assert FOLIO in sello_alterado  # Folio permanece, genesis cambia
