import pytest
import time

def soma(a,b):
    return a+b

def multiplica(a,b):
    return a*b

@pytest.mark.lento
def test_soma_lenta():
    time.sleep(2)
    assert soma(2,2) == 4

@pytest.mark.rapido
def test_soma_rapida():
    assert soma(2,3) == 5

@pytest.mark.lento
def test_multiplicacao_lenta():
    time.sleep(2)
    assert multiplica(2,5) == 10

@pytest.mark.rapido
def test_multiplica_rapida():
    assert multiplica(3,5) == 15