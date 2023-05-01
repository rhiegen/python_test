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
            if self.expression[i] == 'div' and self.expression[1+1] == 0.0:
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
