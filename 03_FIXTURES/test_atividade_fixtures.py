import pytest

@pytest.fixture(scope="function")
def lista_numeros():
    return [1,2,3,4,5]

def test_soma_dobro(lista_numeros):
    assert soma_dobro(lista_numeros) == 30, "A soma do dobro dos números deve ser 30"

def test_soma_dobro_lista_vazia(lista_numeros):
    lista_numeros.clear()
    assert soma_dobro(lista_numeros) == 0, "A soma do dobro dos números da lista vazia deve ser 0"

def soma_dobro(numeros):
    return sum(x * 2 for x in numeros)
    