import pytest

def dividir(a, b):
    if b == 0:
        raise ValueError("O divisor não pode ser zero.")
    return a / b

def test_dividir_valores_validos():
    assert dividir(20,5) == 4
    assert dividir(100,6) == 16.666666666666668

def test_dividir_por_zero():
    with pytest.raises(ValueError) as exec_info:
        dividir(10,0)
    assert "O divisor não pode ser zero." in str(exec_info)