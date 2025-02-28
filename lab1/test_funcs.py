def get_addition(a, b):
    return a + b

def get_subtraction(a, b):
    return a - b

def get_multiplication(a, b):
    return a * b

def test_get_addition():
    result = get_addition(3, 2)
    assert result == 5

def test_get_substraction():
    result = get_subtraction(3, 2)
    assert result == 1

def test_get_multiply():
    result = get_multiplication(3,2)
    assert result == 6