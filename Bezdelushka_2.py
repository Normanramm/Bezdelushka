import pyttsx3
import speedtest
import math


class CalculatorClass:
    """Класс для калькулятора(calculate)"""

    def __init__(self):
        self.operations = {
            "+": self.plus,
            "-": self.minus,
            "*": self.multiply,
            "/": self.divide,
            "%": self.modulo,
            "**": self.power,
            "//": self.floor_divide
        }

    @staticmethod
    def plus():
        a = float(input("Введите первое число: "))
        b = float(input("Введите второе число: "))
        return f"{a} + {b} = {a + b}"

    @staticmethod
    def minus():
        a = float(input("Введите первое число: "))
        b = float(input("Введите второе число: "))
        return f"{a} - {b} = {a - b}"

    @staticmethod
    def multiply():
        a = float(input("Введите первое число: "))
        b = float(input("Введите второе число: "))
        return f"{a} * {b} = {a * b}"

    @staticmethod
    def divide():
        try:
            a = float(input("Введите делимое: "))
            b = float(input("Введите делитель: "))
            return f"{a} / {b} = {a / b}"
        except ZeroDivisionError:
            return "На ноль делить нельзя!"

    @staticmethod
    def modulo():
        try:
            a = float(input("Введите делимое: "))
            b = float(input("Введите делитель: "))
            return f"{a} % {b} = {a % b}"
        except ZeroDivisionError:
            return "На ноль делить нельзя!"

    @staticmethod
    def power():
        a = float(input("Введите основание: "))
        b = float(input("Введите степень: "))
        return f"{a} ** {b} = {a ** b}"

    @staticmethod
    def floor_divide():
        try:
            a = float(input("Введите делимое: "))
            b = float(input("Введите делитель: "))
            return f"{a} // {b} = {a // b}"
        except ZeroDivisionError:
            return "На ноль делить нельзя!"


class MathematicalClass:
    """Класс для математических функций(math)"""

    @staticmethod
    def table():
        for i in range(1, 10):
            print('-' * 34)
            for y in range(1, 10):
                print(i * y, end="\t")
            print()

    @staticmethod
    def procent_stavka():
        p = int(input("Процент: "))  # процент
        x = int(input("Рубли: "))  # рубли
        y = int(input("Копейки: "))  # копейки
        money_before = 100 * x + y
        money_after = int(money_before * (100 + p) / 100)
        result = f'Сумма за год: {money_after // 100, money_after % 100}'
        print(result)
        return result

    @staticmethod
    def injiner_calculator():
        try:
            operation = input(
                '''Введите математическую функцию: 
                1 - sin
                2 - cos
                3 - tan 
                4 - sqrt (квадратный корень) 
                5 - pow (возведение в степень)''')

            num = float(input("Введите число: "))

            if operation == '1':
                result = round(math.sin(math.radians(num)), 2)
                print(result)
                return result
            elif operation == '2':
                result = round(math.cos(math.radians(num)), 2)
                print(result)
                return result
            elif operation == '3':
                result = round(math.tan(math.radians(num)), 2)
                print(result)
                return result
            elif operation == '4':
                result = math.sqrt(num)
                print(result)
                return result
            elif operation == '5':
                power = float(input("Введите степень: "))
                result = round(num ** power, 2)
                print(result)
                return result
            else:
                print("Неверная функция")
                return None

        except ValueError:
            error_msg = "Введены некорректные данные. Пожалуйста, введите число."
            print(error_msg)
            return error_msg


class ProgrammClass:
    """Класс для программ"""

    @staticmethod
    def golos():
        tts = pyttsx3.init()

        voices = tts.getProperty('voices')

        # Задать голос по умолчанию
        tts.setProperty('voice', 'ru')

        # Попробовать установить предпочтительный голос
        for voice in voices:
            if voice.name == 'Aleksandr':
                tts.setProperty('voice', voice.id)

        text = input("Введите текст и он будет звучать: ")
        tts.say(text)
        tts.runAndWait()
        return f"Произнесен текст: {text}"


class SpeedTest:
    def __init__(self):
        self.st = speedtest.Speedtest()
        self.ds = True
        self.us = True
        self.ping = True

    def test(self):
        self.ds = self.st.download()
        self.us = self.st.upload()
        self.ping = self.st.results.ping

        return self.ds, self.us, self.ping

    @staticmethod
    def humansize(nbytes):
        suffixes = ['B', 'KB', 'MB', 'GB', 'TB', 'PB']
        i = 0
        while nbytes >= 1024 and i < len(suffixes) - 1:
            nbytes /= 1024.
            i += 1
        f = ('%.2f' % nbytes).rstrip('0').rstrip('.')
        return '%s %s' % (f, suffixes[i])

    def print_results(self):
        ds, us, ping = self.test()
        print(f'Скорость загрузки: {self.humansize(ds)}')
        print(f'Скорость отдачи: {self.humansize(us)}')
        print(f'Задержка (ping): {ping} м/с')
        return f'Скорость загрузки: {self.humansize(ds)}, Скорость отдачи: {self.humansize(us)}, Задержка (ping): {ping} м/с'


speed_test = SpeedTest()
# speed_test.print_results()


def calculate_functions():
    """Калькулятор для class CalculatorClass"""
    operation = input("Выберите операцию: +, -, *, /, %, **, //: ")
    calculator = CalculatorClass()
    try:
        result = calculator.operations[operation]()
        print(result)
        return result
    except KeyError:
        error_msg = "Неправильный выбор операции!"
        print(error_msg)
        return error_msg


def mathematical_functions():
    """Математические функции для class MathematicalClass"""
    choice = input("""Математические функции:
    1 - Таблица умножения
    2 - Процентная ставка за год
    3 - Триганометрический калькулятор""")
    mathematical = MathematicalClass()
    if choice == "1":
        mathematical.table()
        return "Таблица умножения выведена"
    elif choice == "2":
        return mathematical.procent_stavka()
    elif choice == "3":
        return mathematical.injiner_calculator()
    else:
        error_msg = "Неправильный выбор операции!"
        print(error_msg)
        return error_msg


def programm_functions():
    """Программы функция для class ProgrammClass"""
    choice = input("""Программы:
    1 - Произношение голоса
    2 - Скорость интернета """)
    programmi = ProgrammClass()
    if choice == "1":
        return programmi.golos()
    elif choice == "2":
        print('Идет загрузка, ждите!')
        return speed_test.print_results()
    else:
        error_msg = "Неправильный выбор операции!"
        print(error_msg)
        return error_msg


def choose():
    """Функция для выбора операции"""
    choice = input("""Выберите функционал: 
    1 - Калькулятор
    2 - Математические функции
    3 - Программы """)
    
    if choice == "1":
        calculate_functions()
    elif choice == "2":
        mathematical_functions()
    elif choice == "3":
        programm_functions()
    elif choice == "4":
        pass
    else:
        print("Неправильный выбор операции!")

    while True:
        flag = input("Еще раз: да / нет: ")
        if flag == "да":
            if choice == '1':
                calculate_functions()
            elif choice == '2':
                mathematical_functions()
            elif choice == '3':
                programm_functions()
        elif flag == "нет":
            break
        else:
            print("Пожалуйста, введите 'да' или 'нет'")


if __name__ == "__main__":
    choose()
