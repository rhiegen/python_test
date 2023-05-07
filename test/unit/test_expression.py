import unittest

from enum import Enum


class Oper(Enum):
    ADD = 'add'
    SUB = 'sub'
    MULT = 'mult'
    DIV = 'div'
    POWER = 'power'

    @staticmethod
    def get_symbol(operation):
        return {Oper.ADD.value: ' + ',
                Oper.SUB.value: ' - ',
                Oper.MULT.value: ' * ',
                Oper.DIV.value: ' / ',
                Oper.POWER.value: '^'}[operation]


class Expression:

    def __init__(self, *arguments) -> None:
        self.expression = []
        for arg in arguments:
            self.expression.append(arg)

    def get_trash(self):
        trash = self.expression.pop(0)
        trash = self.expression.pop(0)

    def sum(self):
        resultado = self.expression[0] + self.expression[2]
        self.get_trash()
        self.expression[0] = resultado

    def subtract(self):
        resultado = self.expression[0] - self.expression[2]
        self.get_trash()
        self.expression[0] = resultado

    def multiply(self):
        resultado = self.expression[0] * self.expression[2]
        self.get_trash()
        self.expression[0] = resultado

    def divide(self):
        if self.expression[2] != 0:
            resultado = self.expression[0] / self.expression[2]
        self.get_trash()
        self.expression[0] = resultado

    def power(self):
        resultado = self.expression[0] ** self.expression[2]
        self.get_trash()
        self.expression[0] = resultado

    def process(self, expr):
        for i in range(len(self.expression)):
            if self.expression[i] == 'div' and self.expression[2] == 0.0:
                raise ZeroDivisionError

        ExpressionFactory.get_operation(expr, self.expression[1] if len(self.expression) > 1 else None)
        if len(self.expression) == 1:
            return
        self.process(expr)


class ExpressionFactory:
    def get_operation(cls, code_operation: str):
        return {
            Oper.ADD.value: Expression.sum,
            Oper.SUB.value: Expression.subtract,
            Oper.MULT.value: Expression.multiply,
            Oper.DIV.value: Expression.divide,
            Oper.POWER.value: Expression.power
        }[code_operation](cls) if code_operation is not None else None


if __name__ == '__main__':
    expr = Expression(15.0, Oper.DIV.value, 10.0, Oper.ADD.value, 14.2, Oper.POWER.value, 2)
    expr.process(expr)
    print(f'Resultado {expr.expression[0]: 10.4f} ')


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

    def test_subtract(self):
        expr = Expression(15.0, Oper.SUB.value, 10.0)
        expr.subtract()
        self.assertEqual(expr.expression[0], 5.0)

    def test_multiply(self):
        expr = Expression(15.0, Oper.MULT.value, 10.0)
        expr.multiply()
        self.assertEqual(expr.expression[0], 150.0)

    def test_process(self):
        expr = Expression(15.0, Oper.DIV.value, 0.0)
        with self.assertRaises(ZeroDivisionError):
            expr.process(expr)

    def test_get_symbol(self):
        self.assertEqual(Oper.get_symbol('add'), ' + ')


if __name__ == '__main__':
    unittest.main()
