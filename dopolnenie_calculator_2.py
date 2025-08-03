import functools
import operator

class Calculator:
    def __init__(self, values=None):
        if values is None:
            values = []
        self.values = values

    def add_numbers(self):
        """Сумма всех чисел."""
        return functools.reduce(lambda x, y: x + y, self.values)

    def multiply_numbers(self):
        """Произведение всех чисел."""
        return functools.reduce(lambda x, y: x * y, self.values)

    def subtract_numbers(self):
        """Последовательное вычитание всех чисел."""
        return functools.reduce(lambda x, y: x - y, self.values)

    def divide_numbers(self):
        """Последовательное деление всех чисел."""
        try:
            return functools.reduce(lambda x, y: x / y, self.values)
        except ZeroDivisionError:
            print("Ошибка: делить на ноль нельзя!")
            return None

    def floor_divide_numbers(self):
        """Целочисленное последовательное деление всех чисел."""
        try:
            return functools.reduce(lambda x, y: x // y, self.values)
        except ZeroDivisionError:
            print("Ошибка: делить на ноль нельзя!")
            return None

    def mod_numbers(self):
        """Последовательный остаток от деления всех чисел."""
        try:
            return functools.reduce(lambda x, y: x % y, self.values)
        except ZeroDivisionError:
            print("Ошибка: делить на ноль нельзя!")
            return None

    def pow_numbers(self):
        """Последовательное возведение в степень всех чисел."""
        return functools.reduce(lambda x, y: x ** y, self.values)

    def lshift_numbers(self):
        """Последовательный левый битовый сдвиг всех чисел."""
        return functools.reduce(lambda x, y: x << y, map(int, self.values))

    def rshift_numbers(self):
        """Последовательный правый битовый сдвиг всех чисел."""
        return functools.reduce(lambda x, y: x >> y, map(int, self.values))

    def bit_and_numbers(self):
        """Битовая операция AND всех чисел."""
        return functools.reduce(lambda x, y: x & y, map(int, self.values))

    def bit_or_numbers(self):
        """Битовая операция OR всех чисел."""
        return functools.reduce(lambda x, y: x | y, map(int, self.values))

    def bit_xor_numbers(self):
        """Битовая операция XOR всех чисел."""
        return functools.reduce(lambda x, y: x ^ y, map(int, self.values))

# Функция для запуска калькулятора
def run_calculator():
    numbers_input = input("Введите числа через пробел: ").split()
    numbers = list(map(float, numbers_input))  # Преобразование строковых входных данных в числа

    operations = [
        ('+', 'сумма'),
        ('*', 'произведение'),
        ('-', 'разность'),
        ('/', 'деление'),
        ('//', 'целочисленное деление'),
        ('%', 'остаток от деления'),
        ('**', 'возведение в степень'),
        ('<<', 'левый битовый сдвиг'),
        ('>>', 'правый битовый сдвиг'),
        ('&', 'битовая операция AND'),
        ('|', 'битовая операция OR'),
        ('^', 'битовая операция XOR')
    ]

    print("\nДоступные операции:")
    for idx, op in enumerate(operations):
        print(f"{idx + 1}. {op[0]} ({op[1]})")

    choice = int(input("Выберите номер операции: "))

    calc = Calculator(numbers)

    results = {
        1: calc.add_numbers,
        2: calc.multiply_numbers,
        3: calc.subtract_numbers,
        4: calc.divide_numbers,
        5: calc.floor_divide_numbers,
        6: calc.mod_numbers,
        7: calc.pow_numbers,
        8: calc.lshift_numbers,
        9: calc.rshift_numbers,
        10: calc.bit_and_numbers,
        11: calc.bit_or_numbers,
        12: calc.bit_xor_numbers
    }

    if choice in results.keys():
        result = results.get(choice)()
        if result is not None:
            print(f"\nРезультат операции '{operations[choice - 1][0]}' над числами {numbers}: {result}")
        else:
            print("\nНе удалось выполнить операцию.")
    else:
        print("\nНеправильный выбор операции.")

run_calculator()