"""Test {{ cookiecutter.module_name }} module."""
from {{ cookiecutter.module_name }} import fib


def test_fib():
    """Test fib function."""
    assert fib(0) == 0
    assert fib(1) == 1
    assert fib(2) == 1
    assert fib(3) == 2
    assert fib(4) == 3
    assert fib(5) == 5
    assert fib(6) == 8
