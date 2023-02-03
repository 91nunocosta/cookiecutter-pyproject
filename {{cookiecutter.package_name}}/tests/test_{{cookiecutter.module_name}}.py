"""Test {{ cookiecutter.module_name }} module."""
from {{ cookiecutter.module_name }} import (
    Calculator,
    add,
    divide,
    fib,
    multiply,
    power,
    subtract,
)


def test_add():
    """Test add function."""
    assert add(0, 0) == 0
    assert add(1, 2) == 3


def test_subtract():
    """Test subtract function."""
    assert subtract(5, 3) == 2


def test_multiply():
    """Test multiply function."""
    assert multiply(2, 2) == 4


def test_power():
    """Test power function."""
    assert power(2, 2) == 4


def test_division():
    """Test divide function."""
    assert divide(4, 2) == 2


def test_fib():
    """Test fib function."""
    assert fib(0) == 0
    assert fib(1) == 1
    assert fib(2) == 1
    assert fib(3) == 2
    assert fib(4) == 3
    assert fib(5) == 5
    assert fib(6) == 8


def test_calculator():
    """Test calculator class."""
    calculator = Calculator()
    assert calculator.state == 0

    calculator.add(50)
    assert calculator.state == 50

    calculator.add(100)
    assert calculator.state == 150
