def is_positive(numero):
    return numero > 0

def test_is_positive():
    assert is_positive(5) is True
    assert is_positive(-5) is False

def test_is_positive2():
    assert is_positive(5) is True
    assert is_positive(-5) is False