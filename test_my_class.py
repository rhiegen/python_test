import unittest

from src.my_class import Calculadora, Oper


class MyTestCase(unittest.TestCase):
    # caso a operação seja divisão, arg2 não poderá ser zero
    def setUp(self):
        self.calc = Calculadora(1, 0, Oper.MULT.value)
        # self.calc = Calculadora(1, 0, 'div')
        self.calc.sum()
        self.calc.subtract()

    def tearDown(self):
        if self.calc.arg3 == 'div' and self.calc.arg2 == 0:
            print('Não é possível divisão por zero')

    def test_if_arguments_are_not_none(self):
        self.assertIsNotNone(self.calc.arg1)
        self.assertIsNotNone(self.calc.arg2)
        self.assertIsNotNone(self.calc.arg3)

    def test_if_argument_type_is_correct(self):
        self.assertIsInstance(self.calc.arg1, float)
        self.assertIsInstance(self.calc.arg2, float)
        self.assertIsInstance(self.calc.arg3, str)

    def test_if_operations_are_valid(self):
        self.assertIn(self.calc.arg3, ['add', 'sub', 'mult', 'div'])

    # def test_if_second_argument_is_different_from_zero_on_div(self):
    #     self.assertEqual(self.calc.arg3, 'div')
    #     self.assertNotEqual(self.calc.arg2, 0)


if __name__ == '__main__':
    unittest.main()
