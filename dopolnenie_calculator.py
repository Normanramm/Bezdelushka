class Calculator:
    def __init__(self, value=0):
        self.value = value

    def __repr__(self):
        return str(self.value)

    # Перегружаемые операторы
    def __add__(self, other):
        return Calculator(self.value + other.value)

    def __sub__(self, other):
        return Calculator(self.value - other.value)

    def __mul__(self, other):
        return Calculator(self.value * other.value)

    def __floordiv__(self, other):
        try:
            return Calculator(self.value // other.value)
        except ZeroDivisionError:
            print("Ошибка: делить на ноль нельзя!")
            return None

    def __truediv__(self, other):
        try:
            return Calculator(self.value / other.value)
        except ZeroDivisionError:
            print("Ошибка: делить на ноль нельзя!")
            return None

    def __mod__(self, other):
        try:
            return Calculator(self.value % other.value)
        except ZeroDivisionError:
            print("Ошибка: делить на ноль нельзя!")
            return None

    def __pow__(self, power):
        return Calculator(pow(self.value, power.value))

    def __lshift__(self, other):
        return Calculator(self.value << other.value)

    def __rshift__(self, other):
        return Calculator(self.value >> other.value)

    def __and__(self, other):
        return Calculator(self.value & other.value)

    def __or__(self, other):
        return Calculator(self.value | other.value)

    def __xor__(self, other):
        return Calculator(self.value ^ other.value)

# Интерфейс взаимодействия с пользователем
def calculator_menu():
    operations = [
        ('+', '__add__'),
        ('-', '__sub__'),
        ('*', '__mul__'),
        ('//', '__floordiv__'),
        ('/', '__truediv__'),
        ('%', '__mod__'),
        ('**', '__pow__'),
        ('<<', '__lshift__'),
        ('>>', '__rshift__'),
        ('&', '__and__'),
        ('|', '__or__'),
        ('^', '__xor__')
    ]

    first_number = float(input("Введите первое число: "))
    second_number = float(input("Введите второе число: "))

    print("\nДоступные операции:")
    for i, op in enumerate(operations):
        print(f"{i + 1}. {op[0]} ({op[1]})")

    choice = input("Выберите номер операции: ")
    index = int(choice) - 1

    if 0 <= index < len(operations):
        operation_name = operations[index][1]
        method = getattr(Calculator(first_number), operation_name)
        result = method(Calculator(second_number))
        
        if isinstance(result, Calculator):
            print(f"\nРезультат: {first_number} {operations[index][0]} {second_number} = {result}")
        else:
            print("\nНевозможно выполнить выбранную операцию.")
    else:
        print("\nНекорректный выбор операции.")

# Запускаем калькулятор
calculator_menu()