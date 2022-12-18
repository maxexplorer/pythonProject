import pytest

from calculator import calculator


def test_plus():
    assert calculator('5+5') == 10


def test_minus():
    assert calculator('9-2') == 7


def test_multiplication():
    assert calculator('5*5') == 25


def test_division():
    assert calculator('10/2') == 5.0


def test_no_sign():
    with pytest.raises(ValueError) as ex:
        calculator('abcdefg')
    assert 'Expression should contain at least one sign +-*/' == ex.value.args[0]


if __name__ == '__main__':
    pytest.main()
