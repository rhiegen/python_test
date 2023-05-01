import unittest

from src.expression import Expression
from src.my_class import Oper


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.expr = Expression(1.0, Oper.DIV.value, 10.0, Oper.POWER.value, 3.0)

    def test_correct_size_of_attributes(self):
        self.assertEqual(len(self.expr.expression) % 2, 1)

    def test_if_arguments_are_not_none(self):
        for arg in self.expr.expression:
            self.assertIsNotNone(arg, None)

    def test_if_argument_type_is_correct(self):
        for i in range(len(self.expr.expression)):
            if i % 2 == 1:
                self.assertIsInstance(self.expr.expression[i], str)
            else:
                self.assertIsInstance(self.expr.expression[i], float)

    def test_if_operators_values_are_valid(self):
        for i in range(len(self.expr.expression)):
            if i % 2 == 1:
                self.assertIn(self.expr.expression[i], ['add', 'sub', 'mult', 'div', 'power'])

    def test_if_there_is_division_by_zero(self):
        if self.expr.expression[1] == 'div':
            self.assertNotEqual(self.expr.expression[2], 0.0)


if __name__ == '__main__':
    unittest.main()
