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


class Calculadora:

    def __init__(self, arg1: float, arg2: float, arg3: str) -> None:
        self.arg1 = arg1 if arg1 is not None else 1.0
        self.arg2 = arg2 if arg2 is not None and arg2 == 0.0 else 1.0
        self.arg3 = arg3 if arg3 in ['add', 'sub', 'mult', 'div', 'power'] else 'add'
        if self.arg3 == 'div' and self.arg2 == 0.0:
            print('Não é possível divisão por zero')
        self.arg1 = arg1 if isinstance(arg1, float) else 1.0
        self.arg2 = arg2 if isinstance(arg2, float) else 1.0

    def sum(self) -> float:
        return self.arg1 + self.arg2 if self.arg3 == 'add' else None

    def subtract(self) -> float:
        return self.arg1 - self.arg2 if self.arg3 == 'sub' else None

    def multiply(self) -> float:
        return self.arg1 * self.arg2 if self.arg3 == 'mult' else None

    def divide(self) -> float:
        return self.arg1 / self.arg2 if self.arg3 == 'div' and self.arg2 != 0 else None

    def power(self) -> float:
        return self.arg1 ** self.arg2 if self.arg3 == 'power' else None


class CalculadoraFactory:
    def get_operation(cls, code_operation):
        return {
            Oper.ADD.value: Calculadora.sum,
            Oper.SUB.value: Calculadora.subtract,
            Oper.MULT.value: Calculadora.multiply,
            Oper.DIV.value: Calculadora.divide,
            Oper.POWER.value: Calculadora.power
        }[code_operation](cls)


if __name__ == '__main__':
    calc = Calculadora(15.0, 20.0, Oper.DIV.value)
    resultado = CalculadoraFactory.get_operation(calc, calc.arg3)
    print(f'{calc.arg1}{Oper.get_symbol(calc.arg3)}{calc.arg2} = '
          f'{resultado:10.4f} ')
