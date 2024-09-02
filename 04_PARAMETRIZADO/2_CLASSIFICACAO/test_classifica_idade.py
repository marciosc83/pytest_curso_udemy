import pytest
from classifica_idade import classifica_idade

@pytest.mark.parametrize("idade,categoria_esperada",
    [
        (10,"CRIANÇA"),
        (15,"ADOLESCENTE"),
        (30,"ADULTO"),
        (70,"IDOSO")
    ])
def test_classifica_idade(idade,categoria_esperada):
    assert classifica_idade(idade) == categoria_esperada