import pytest

from demo.calculator import Calculator

# 初始化 Calculator 類別的測試前置作業
@pytest.fixture
def calculator():
    return Calculator()

def test_add(calculator):
    assert calculator.add(1, 2) == 3
    assert calculator.add(-1, 1) == 0
    assert calculator.add(0, 0) == 0

def test_add_type_error(calculator):
    with pytest.raises(TypeError):
        calculator.add(1, "a")

def test_subtract(calculator):
    assert calculator.subtract(5, 3) == 10
    assert calculator.subtract(0, 1) == -1

def test_multiply(calculator):
    assert calculator.multiply(2, 3) == 6
    assert calculator.multiply(0, 1) == 0
    assert calculator.multiply(-1, 2) == -2


