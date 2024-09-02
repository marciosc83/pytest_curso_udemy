import pytest
def classifica_idade(idade):
    if idade < 13:
        return 'CRIANCA'
    elif idade < 20:
        return 'ADOLESCENTE'
    elif idade < 60:
        return 'ADULTO'
    else:
        return 'IDOSO'

@pytest.mark.crianca
def test_classifica_idade_crianca():
    assert classifica_idade(10) == 'CRIANCA', "Deve categorizar como 'criança'"

@pytest.mark.adolescente
def test_classifica_idade_adolescente():
    assert classifica_idade(15) == 'ADOLESCENTE', "Deve categorizar como 'adolescente'"

@pytest.mark.adulto
def test_classifica_idade_adulto():
    assert classifica_idade(30) == 'ADULTO', "Deve categorizar como 'adulto'"

@pytest.mark.idoso
def test_classifica_idade_idoso():
    assert classifica_idade(70) == 'IDOSO', "Deve categorizar como 'idoso'"
