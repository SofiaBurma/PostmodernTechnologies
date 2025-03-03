from funcs import get_addition, get_subtraction, get_multiplication
def test_get_addition():
    result = get_addition(3, 2)
    assert result == 5

def test_get_substraction():
    result = get_subtraction(3, 2)
    assert result == 1

def test_get_multiply():
    result = get_multiplication(3,2)
    assert result == 6