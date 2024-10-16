import pyttsx3
import speedtest


class CalculatorClass:
    '''Класс для калькулятора(calculate)'''

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

    def plus(self):
        a = float(input("Введите первое число: "))
        b = float(input("Введите второе число: "))
        return f"{a} + {b} = {a + b}"

    def minus(self):
        a = float(input("Введите первое число: "))
        b = float(input("Введите второе число: "))
        return f"{a} - {b} = {a - b}"

    def multiply(self):
        a = float(input("Введите первое число: "))
        b = float(input("Введите второе число: "))
        return f"{a} * {b} = {a * b}"

    def divide(self):
        try:
            a = float(input("Введите делимое: "))
            b = float(input("Введите делитель: "))
            return f"{a} / {b} = {a / b}"
        except ZeroDivisionError:
            print("На ноль делить нельзя!")

    def modulo(self):
        try:
            a = float(input("Введите делимое: "))
            b = float(input("Введите делитель: "))
            return f"{a} % {b} = {a % b}"
        except ZeroDivisionError:
            print("На ноль делить нельзя!")

    def power(self):
        a = float(input("Введите основание: "))
        b = float(input("Введите степень: "))
        return f"{a} ** {b} = {a ** b}"

    def floor_divide(self):
        try:
            a = float(input("Введите делимое: "))
            b = float(input("Введите делитель: "))
            return f"{a} // {b} = {a // b}"
        except ZeroDivisionError:
            print("На ноль делить нельзя!")


class MathematicalClass:
    '''Класс для математических функций(math)'''

    def table(self):
        for i in range(1, 10):
            print('-' * 34)
            for y in range(1, 10):
                print(i * y, end="\t")
            print()

    def procent_stavka(self):

        p = int(input("Процент: "))  # процент
        x = int(input("Рубли: "))  # рубли
        y = int(input("Копейки: "))  # копейки
        money_before = 100 * x + y
        money_after = int(money_before * (100 + p) / 100)
        print(f'Сумма за год: {money_after // 100, money_after % 100}')


class ProgrammClass:
    '''Класс для программ'''

    def golos(self):
        tts = pyttsx3.init()

        voices = tts.getProperty('voices')

        # Задать голос по умолчанию
        tts.setProperty('voice', 'ru')

        # Попробовать установить предпочтительный голос
        for voice in voices:
            if voice.name == 'Aleksandr':
                tts.setProperty('voice', voice.id)

        tts.say(input("Введите текст и он будет звучать: "))
        tts.runAndWait()


class SpeedTest:
    def __init__(self):
        self.st = speedtest.Speedtest()

    def test(self):
        self.ds = self.st.download()
        self.us = self.st.upload()
        self.ping = self.st.results.ping

        return self.ds, self.us, self.ping

    def humansize(self, nbytes):
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


speed_test = SpeedTest()
print('Идет загрузка!')
# speed_test.print_results()


'''Функции для выбора выполннения классов'''


def calculate():  # Калькулятор для class CalculatorClass
    operation = input("Выберите операцию: +, -, *, /, %, **, //: ")
    calculator = CalculatorClass()
    try:
        result = calculator.operations[operation]()
        print(result)
    except KeyError:
        print("Неправильный выбор операции!")


def math():  # Математические функции для class MathematicalClass
    choice = input("""Математические функции:
    1 - Таблица умножения
    2 - Процентная ставка за год """)
    mathematical = MathematicalClass()
    if choice == "1":
        print(mathematical.table())
    elif choice == "2":
        print(mathematical.procent_stavka())
    else:
        print("Неправильный выбор операции!")


def programm():  # Программы функция для class ProgrammClass
    choice = input("""Программы:
    1 - Произношение голоса
    2 - Скорость интернета """)
    programmi = ProgrammClass()
    if choice == "1":
        print(programmi.golos())
    elif choice == "2":
        print(speed_test.print_results())
    else:
        print("Неправильный выбор операции!")


'''Функция для выбора операции(наверно стоит засунуть в класс)'''


def choose():
    choice = input("""Выберите функционал: 
    1 - Калькулятор
    2 - Математические функции
    3 - Программы """
                   )
    if choice == "1":
        calculate()
    elif choice == "2":
        math()
    elif choice == "3":
        programm()
    elif choice == "4":
        pass
    else:
        print("Неправильный выбор операции!")

    while True:
        flag = input("Еще раз: да / нет: ")
        if flag == "да" and choice == '1':
            calculate()
        elif flag == 'да' and choice == '2':
            math()
        elif flag == 'да' and choice == '3':
            programm()
        elif flag == "нет":
            choose()
        else:
            break


choose()
