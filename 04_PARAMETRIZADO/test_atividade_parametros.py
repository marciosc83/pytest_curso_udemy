import pytest

@pytest.mark.parametrize("n,resultado_esperado",[
    (0,1),
    (1,1),
    (2,2),
    (3,6)
])
def test_fatorial(n,resultado_esperado):
    assert fatorial(n) == resultado_esperado

@pytest.mark.parametrize("valor_negativo",[-1, -10, -15])
def test_fatorial_negativo(valor_negativo):
    with pytest.raises(RecursionError) as excinfo:
        assert fatorial(valor_negativo)

def fatorial(n):
    if n == 0:
        return 1
    else:
        return n * fatorial(n-1)
    
