from unittest import TestCase, main
from calculator import calculator


class CalculatorTest(TestCase):

    def test_plus(self):
        self.assertEqual(calculator('5+5'), 10)

    def test_minus(self):
        self.assertEqual(calculator('9-2'), 7)

    def test_multiplication(self):
        self.assertEqual(calculator('5*5'), 25)

    def test_division(self):
        self.assertEqual(calculator('10/2'), 5.0)

    def test_no_sign(self):
        with self.assertRaises(ValueError) as ex:
            calculator('abcdefg')
        self.assertEqual('Expression should contain at least one sign +-*/', ex.exception.args[0])


if __name__ == '__main__':
    main()
