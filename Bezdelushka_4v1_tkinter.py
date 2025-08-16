import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import pyttsx3
import speedtest
import math
import threading
import re
from typing import Optional, Callable


class CalculatorClass:
    """Класс для математических операций"""
    def __init__(self):
        self.history = []
        self.max_history = 50  # Максимальное количество записей в истории

    def add_to_history(self, operation: str, result: str):
        """Добавление операции в историю"""
        from datetime import datetime
        timestamp = datetime.now().strftime("%H:%M:%S")
        history_entry = {
            'timestamp': timestamp,
            'operation': operation,
            'result': result
        }
        self.history.insert(0, history_entry)  # Добавляем в начало
        # Ограничиваем размер истории
        if len(self.history) > self.max_history:
            self.history = self.history[:self.max_history]

    def get_history(self) -> list:
        """Получение истории операций"""
        return self.history.copy()

    def clear_history(self):
        """Очистка истории"""
        self.history.clear()

    def get_last_result(self) -> str:
        """Получение последнего результата"""
        if self.history:
            return self.history[0]['result']
        return ""

    @staticmethod
    def plus(a: float, b: float) -> str:
        return f"{a} + {b} = {a + b}"

    @staticmethod
    def minus(a: float, b: float) -> str:
        return f"{a} - {b} = {a - b}"

    @staticmethod
    def multiply(a: float, b: float) -> str:
        return f"{a} × {b} = {a * b}"

    @staticmethod
    def divide(a: float, b: float) -> str:
        try:
            if b == 0:
                return "❌ На ноль делить нельзя!"
            result = a / b
            return f"{a} ÷ {b} = {result:.4f}"
        except Exception:
            return "❌ Ошибка вычисления"

    @staticmethod
    def modulo(a: float, b: float) -> str:
        try:
            if b == 0:
                return "❌ На ноль делить нельзя!"
            return f"{a} % {b} = {a % b}"
        except Exception:
            return "❌ Ошибка вычисления"

    @staticmethod
    def power(a: float, b: float) -> str:
        try:
            result = a ** b
            if result > 1e10:
                return f"{a} ^ {b} = {result:.2e}"
            return f"{a} ^ {b} = {result:.4f}"
        except Exception:
            return "❌ Ошибка вычисления"

    @staticmethod
    def floor_divide(a: float, b: float) -> str:
        try:
            if b == 0:
                return "❌ На ноль делить нельзя!"
            result = a // b
            return f"{a} // {b} = {result}"
        except Exception:
            return "❌ Ошибка вычисления"

    @staticmethod
    def bitwise_and(a: float, b: float) -> str:
        """Побитовое И"""
        try:
            result = int(a) & int(b)
            return f"{int(a)} & {int(b)} = {result}"
        except Exception:
            return "❌ Ошибка вычисления"

    @staticmethod
    def bitwise_or(a: float, b: float) -> str:
        """Побитовое ИЛИ"""
        try:
            result = int(a) | int(b)
            return f"{int(a)} | {int(b)} = {result}"
        except Exception:
            return "❌ Ошибка вычисления"

    @staticmethod
    def bitwise_xor(a: float, b: float) -> str:
        """Побитовое исключающее ИЛИ"""
        try:
            result = int(a) ^ int(b)
            return f"{int(a)} ^ {int(b)} = {result}"
        except Exception:
            return "❌ Ошибка вычисления"

    @staticmethod
    def bitwise_left_shift(a: float, b: float) -> str:
        """Побитовый сдвиг влево"""
        try:
            if b < 0 or b > 63:
                return "❌ Сдвиг должен быть от 0 до 63"
            result = int(a) << int(b)
            return f"{int(a)} << {int(b)} = {result}"
        except Exception:
            return "❌ Ошибка вычисления"

    @staticmethod
    def bitwise_right_shift(a: float, b: float) -> str:
        """Побитовый сдвиг вправо"""
        try:
            if b < 0 or b > 63:
                return "❌ Сдвиг должен быть от 0 до 63"
            result = int(a) >> int(b)
            return f"{int(a)} >> {int(b)} = {result}"
        except Exception:
            return "❌ Ошибка вычисления"

    @staticmethod
    def bitwise_not(a: float, b: float) -> str:
        """Побитовое НЕ (используется только первое число)"""
        try:
            result = ~int(a)
            return f"~{int(a)} = {result}"
        except Exception:
            return "❌ Ошибка вычисления"

    @staticmethod
    def gcd(a: float, b: float) -> str:
        """Наибольший общий делитель"""
        try:
            if a != int(a) or b != int(b):
                return "❌ НОД определен только для целых чисел"
            result = math.gcd(int(a), int(b))
            return f"НОД({int(a)}, {int(b)}) = {result}"
        except Exception:
            return "❌ Ошибка вычисления"

    @staticmethod
    def lcm(a: float, b: float) -> str:
        """Наименьшее общее кратное"""
        try:
            if a != int(a) or b != int(b):
                return "❌ НОК определен только для целых чисел"
            if int(a) == 0 or int(b) == 0:
                return "❌ НОК не определен для нуля"
            result = abs(int(a) * int(b)) // math.gcd(int(a), int(b))
            return f"НОК({int(a)}, {int(b)}) = {result}"
        except Exception:
            return "❌ Ошибка вычисления"

    @staticmethod
    def hypotenuse(a: float, b: float) -> str:
        """Гипотенуза по двум катетам"""
        try:
            result = math.sqrt(a**2 + b**2)
            return f"Гипотенуза({a}, {b}) = {result:.6f}"
        except Exception:
            return "❌ Ошибка вычисления"

    @staticmethod
    def distance(a: float, b: float) -> str:
        """Расстояние между двумя числами"""
        try:
            result = abs(a - b)
            return f"Расстояние({a}, {b}) = {result:.6f}"
        except Exception:
            return "❌ Ошибка вычисления"

    @staticmethod
    def average(a: float, b: float) -> str:
        """Среднее арифметическое"""
        try:
            result = (a + b) / 2
            return f"Среднее({a}, {b}) = {result:.6f}"
        except Exception:
            return "❌ Ошибка вычисления"

    @staticmethod
    def geometric_mean(a: float, b: float) -> str:
        """Среднее геометрическое"""
        try:
            if a < 0 or b < 0:
                return "❌ Среднее геометрическое определено только для неотрицательных чисел"
            result = math.sqrt(a * b)
            return f"Среднее геометрическое({a}, {b}) = {result:.6f}"
        except Exception:
            return "❌ Ошибка вычисления"

    @staticmethod
    def harmonic_mean(a: float, b: float) -> str:
        """Среднее гармоническое"""
        try:
            if a == 0 or b == 0:
                return "❌ Среднее гармоническое не определено для нуля"
            result = 2 / (1/a + 1/b)
            return f"Среднее гармоническое({a}, {b}) = {result:.6f}"
        except Exception:
            return "❌ Ошибка вычисления"

    @staticmethod
    def min(a: float, b: float) -> str:
        """Минимальное из двух чисел"""
        try:
            result = min(a, b)
            return f"min({a}, {b}) = {result}"
        except Exception:
            return "❌ Ошибка вычисления"

    @staticmethod
    def max(a: float, b: float) -> str:
        """Максимальное из двух чисел"""
        try:
            result = max(a, b)
            return f"max({a}, {b}) = {result}"
        except Exception:
            return "❌ Ошибка вычисления"

    @staticmethod
    def percentage(a: float, b: float) -> str:
        """Процент от числа"""
        try:
            if b == 0:
                return "❌ Деление на ноль"
            result = (a / b) * 100
            return f"{a} составляет {result:.2f}% от {b}"
        except Exception:
            return "❌ Ошибка вычисления"

    @staticmethod
    def percentage_change(a: float, b: float) -> str:
        """Изменение в процентах"""
        try:
            if b == 0:
                return "❌ Деление на ноль"
            result = ((a - b) / b) * 100
            if result >= 0:
                return f"Изменение: +{result:.2f}%"
            else:
                return f"Изменение: {result:.2f}%"
        except Exception:
            return "❌ Ошибка вычисления"

    @staticmethod
    def ratio(a: float, b: float) -> str:
        """Отношение двух чисел"""
        try:
            if b == 0:
                return "❌ Деление на ноль"
            result = a / b
            return f"Отношение {a}:{b} = {result:.6f}"
        except Exception:
            return "❌ Ошибка вычисления"

    @staticmethod
    def reciprocal_sum(a: float, b: float) -> str:
        """Сумма обратных чисел"""
        try:
            if a == 0 or b == 0:
                return "❌ Деление на ноль"
            result = (1/a) + (1/b)
            return f"1/{a} + 1/{b} = {result:.6f}"
        except Exception:
            return "❌ Ошибка вычисления"

    @staticmethod
    def square_sum(a: float, b: float) -> str:
        """Сумма квадратов"""
        try:
            result = a**2 + b**2
            return f"{a}² + {b}² = {result:.6f}"
        except Exception:
            return "❌ Ошибка вычисления"

    @staticmethod
    def square_diff(a: float, b: float) -> str:
        """Разность квадратов"""
        try:
            result = a**2 - b**2
            return f"{a}² - {b}² = {result:.6f}"
        except Exception:
            return "❌ Ошибка вычисления"

    @staticmethod
    def cube_sum(a: float, b: float) -> str:
        """Сумма кубов"""
        try:
            result = a**3 + b**3
            return f"{a}³ + {b}³ = {result:.6f}"
        except Exception:
            return "❌ Ошибка вычисления"

    @staticmethod
    def cube_diff(a: float, b: float) -> str:
        """Разность кубов"""
        try:
            result = a**3 - b**3
            return f"{a}³ - {b}³ = {result:.6f}"
        except Exception:
            return "❌ Ошибка вычисления"


class MathematicalClass:
    """Класс для математических функций"""
    @staticmethod
    def multiplication_table() -> str:
        result = "📊 Таблица умножения\n" + "=" * 50 + "\n"
        for i in range(1, 11):
            result += f"🎯 {i} × таблица:\n"
            result += "-" * 30 + "\n"
            row = ""
            for j in range(1, 11):
                row += f"{i:2} × {j:2} = {i*j:3}  "
                if j % 5 == 0:
                    row += "\n"
            result += row + "\n"
        return result

    @staticmethod
    def interest_rate(p: float, x: int, y: int) -> str:
        try:
            if y < 0 or y >= 100:
                return "❌ Копейки должны быть от 0 до 99"
            if x < 0:
                return "❌ Рубли не могут быть отрицательными"
            money_before = 100 * x + y
            money_after = int(money_before * (100 + p) / 100)
            rub = money_after // 100
            kop = money_after % 100
            return f"💰 Сумма за год: {rub} руб. {kop:02d} коп."
        except Exception:
            return "❌ Ошибка расчета"

    @staticmethod
    def scientific_calc(num: float, op: str) -> str:
        try:
            if op == 'sin':
                result = math.sin(math.radians(num))
                return f"sin({num}°) = {result:.6f}"
            elif op == 'cos':
                result = math.cos(math.radians(num))
                return f"cos({num}°) = {result:.6f}"
            elif op == 'tan':
                result = math.tan(math.radians(num))
                return f"tan({num}°) = {result:.6f}"
            elif op == 'asin':
                if -1 <= num <= 1:
                    result = math.degrees(math.asin(num))
                    return f"arcsin({num}) = {result:.6f}°"
                else:
                    return "❌ arcsin определен только для [-1, 1]"
            elif op == 'acos':
                if -1 <= num <= 1:
                    result = math.degrees(math.acos(num))
                    return f"arccos({num}) = {result:.6f}°"
                else:
                    return "❌ arccos определен только для [-1, 1]"
            elif op == 'atan':
                result = math.degrees(math.atan(num))
                return f"arctan({num}) = {result:.6f}°"
            elif op == 'sinh':
                result = math.sinh(num)
                return f"sinh({num}) = {result:.6f}"
            elif op == 'cosh':
                result = math.cosh(num)
                return f"cosh({num}) = {result:.6f}"
            elif op == 'tanh':
                result = math.tanh(num)
                return f"tanh({num}) = {result:.6f}"
            elif op == 'sqrt':
                if num < 0:
                    return "❌ Корень из отрицательного числа"
                result = math.sqrt(num)
                return f"√{num} = {result:.6f}"
            elif op == 'cbrt':
                result = num ** (1/3)
                return f"∛{num} = {result:.6f}"
            elif op == 'pow2':
                result = num ** 2
                return f"{num}² = {result:.6f}"
            elif op == 'pow3':
                result = num ** 3
                return f"{num}³ = {result:.6f}"
            elif op == 'pow_n':
                return f"{num}^n (введите степень отдельно)"
            elif op == 'log10':
                if num <= 0:
                    return "❌ Логарифм из неположительного числа"
                result = math.log10(num)
                return f"log₁₀({num}) = {result:.6f}"
            elif op == 'ln':
                if num <= 0:
                    return "❌ Натуральный логарифм из неположительного числа"
                result = math.log(num)
                return f"ln({num}) = {result:.6f}"
            elif op == 'log2':
                if num <= 0:
                    return "❌ Логарифм по основанию 2 из неположительного числа"
                result = math.log2(num)
                return f"log₂({num}) = {result:.6f}"
            elif op == 'abs':
                result = abs(num)
                return f"|{num}| = {result}"
            elif op == 'floor':
                result = math.floor(num)
                return f"⌊{num}⌋ = {result}"
            elif op == 'ceil':
                result = math.ceil(num)
                return f"⌈{num}⌉ = {result}"
            elif op == 'round':
                result = round(num)
                return f"round({num}) = {result}"
            elif op == 'factorial':
                if num < 0 or num != int(num):
                    return "❌ Факториал определен только для неотрицательных целых чисел"
                if num > 170:
                    return "❌ Слишком большое число для факториала"
                result = math.factorial(int(num))
                return f"{int(num)}! = {result}"
            elif op == 'exp':
                result = math.exp(num)
                if result > 1e10:
                    return f"e^{num} = {result:.2e}"
                return f"e^{num} = {result:.6f}"
            elif op == 'exp10':
                result = 10 ** num
                if result > 1e10:
                    return f"10^{num} = {result:.2e}"
                return f"10^{num} = {result:.6f}"
            elif op == 'exp2':
                result = 2 ** num
                if result > 1e10:
                    return f"2^{num} = {result:.2e}"
                return f"2^{num} = {result:.6f}"
            elif op == 'reciprocal':
                if num == 0:
                    return "❌ Деление на ноль"
                result = 1 / num
                return f"1/{num} = {result:.6f}"
            elif op == 'square_root':
                if num < 0:
                    return "❌ Корень из отрицательного числа"
                result = num ** 0.5
                return f"{num}^0.5 = {result:.6f}"
            elif op == 'cube_root':
                result = num ** (1/3)
                return f"{num}^(1/3) = {result:.6f}"
            elif op == 'inverse':
                if num == 0:
                    return "❌ Деление на ноль"
                result = -num
                return f"-({num}) = {result}"
            elif op == 'percent':
                result = num / 100
                return f"{num}% = {result:.6f}"
            elif op == 'degrees_to_radians':
                result = math.radians(num)
                return f"{num}° = {result:.6f} рад"
            elif op == 'radians_to_degrees':
                result = math.degrees(num)
                return f"{num} рад = {result:.6f}°"
            elif op == 'pi_multiply':
                result = num * math.pi
                return f"{num} × π = {result:.6f}"
            elif op == 'e_multiply':
                result = num * math.e
                return f"{num} × e = {result:.6f}"
            else:
                return "❌ Неизвестная операция"
        except Exception as e:
            return f"❌ Ошибка: {str(e)}"

    @staticmethod
    def advanced_calc(num1: float, num2: float, op: str) -> str:
        """Расширенные операции с двумя числами"""
        try:
            if op == 'power':
                result = num1 ** num2
                if result > 1e10:
                    return f"{num1}^{num2} = {result:.2e}"
                return f"{num1}^{num2} = {result:.6f}"
            elif op == 'root':
                if num2 == 0:
                    return "❌ Степень корня не может быть нулем"
                if num1 < 0 and num2 % 2 == 0:
                    return "❌ Четный корень из отрицательного числа"
                result = num1 ** (1/num2)
                return f"√({num1}) по степени {num2} = {result:.6f}"
            elif op == 'log_base':
                if num1 <= 0 or num2 <= 0 or num2 == 1:
                    return "❌ Некорректные числа для логарифма"
                result = math.log(num1, num2)
                return f"log_{num2}({num1}) = {result:.6f}"
            elif op == 'mod':
                if num2 == 0:
                    return "❌ Деление на ноль"
                result = num1 % num2
                return f"{num1} mod {num2} = {result}"
            elif op == 'gcd':
                if num1 != int(num1) or num2 != int(num2):
                    return "❌ НОД определен только для целых чисел"
                result = math.gcd(int(num1), int(num2))
                return f"НОД({int(num1)}, {int(num2)}) = {result}"
            elif op == 'lcm':
                if num1 != int(num1) or num2 != int(num2):
                    return "❌ НОК определен только для целых чисел"
                if int(num1) == 0 or int(num2) == 0:
                    return "❌ НОК не определен для нуля"
                result = abs(int(num1) * int(num2)) // math.gcd(int(num1), int(num2))
                return f"НОК({int(num1)}, {int(num2)}) = {result}"
            elif op == 'hypotenuse':
                result = math.sqrt(num1**2 + num2**2)
                return f"Гипотенуза({num1}, {num2}) = {result:.6f}"
            elif op == 'distance':
                result = abs(num1 - num2)
                return f"Расстояние({num1}, {num2}) = {result:.6f}"
            elif op == 'average':
                result = (num1 + num2) / 2
                return f"Среднее({num1}, {num2}) = {result:.6f}"
            elif op == 'min':
                result = min(num1, num2)
                return f"min({num1}, {num2}) = {result}"
            elif op == 'max':
                result = max(num1, num2)
                return f"max({num1}, {num2}) = {result}"
            else:
                return "❌ Неизвестная операция"
        except Exception as e:
            return f"❌ Ошибка: {str(e)}"


class ProgrammClass:
    """Класс для работы с программами"""
    def __init__(self):
        try:
            self.tts = pyttsx3.init()
            self.voices = self.tts.getProperty('voices')
            self.current_voice_index = 0
            self.rate = 150
            self.volume = 0.9
            self._setup_voice()
            self.tts_available = True
        except Exception as e:
            self.tts = None
            self.voices = []
            self.current_voice_index = 0
            self.rate = 150
            self.volume = 0.9
            self.tts_available = False
            print(f"⚠️ Ошибка инициализации pyttsx3: {e}")

    def _setup_voice(self):
        """Настройка голоса для озвучки"""
        try:
            if self.voices:
                for i, voice in enumerate(self.voices):
                    if 'ru' in voice.languages or 'russian' in voice.name.lower():
                        self.current_voice_index = i
                        break
                self.tts.setProperty('voice', self.voices[self.current_voice_index].id)
            self.tts.setProperty('rate', self.rate)
            self.tts.setProperty('volume', self.volume)
        except Exception:
            pass

    def get_voices_info(self) -> list:
        """Получение информации о доступных голосах"""
        voices_info = []
        for i, voice in enumerate(self.voices):
            voice_info = {
                'index': i,
                'name': voice.name,
                'id': voice.id,
                'languages': voice.languages,
                'gender': voice.gender,
                'age': voice.age
            }
            voices_info.append(voice_info)
        return voices_info

    def change_voice(self, voice_index: int) -> str:
        """Изменение голоса"""
        try:
            if 0 <= voice_index < len(self.voices):
                self.current_voice_index = voice_index
                self.tts.setProperty('voice', self.voices[voice_index].id)
                voice_name = self.voices[voice_index].name
                return f"✅ Голос изменен на: {voice_name}"
            else:
                return "❌ Неверный индекс голоса"
        except Exception as e:
            return f"❌ Ошибка изменения голоса: {str(e)}"

    def change_rate(self, new_rate: int) -> str:
        """Изменение скорости речи"""
        try:
            if 50 <= new_rate <= 300:
                self.rate = new_rate
                self.tts.setProperty('rate', new_rate)
                return f"✅ Скорость изменена на: {new_rate}"
            else:
                return "❌ Скорость должна быть от 50 до 300"
        except Exception as e:
            return f"❌ Ошибка изменения скорости: {str(e)}"

    def change_volume(self, new_volume: float) -> str:
        """Изменение громкости"""
        try:
            if 0.0 <= new_volume <= 1.0:
                self.volume = new_volume
                self.tts.setProperty('volume', new_volume)
                return f"✅ Громкость изменена на: {new_volume:.1f}"
            else:
                return "❌ Громкость должна быть от 0.0 до 1.0"
        except Exception as e:
            return f"❌ Ошибка изменения громкости: {str(e)}"

    def get_current_voice_info(self) -> str:
        """Получение информации о текущем голосе"""
        try:
            if self.voices and 0 <= self.current_voice_index < len(self.voices):
                voice = self.voices[self.current_voice_index]
                return f"🎤 Текущий голос: {voice.name}\n📊 Скорость: {self.rate}\n🔊 Громкость: {self.volume:.1f}"
            else:
                return "❌ Голос не выбран"
        except Exception:
            return "❌ Ошибка получения информации о голосе"

    def speak_text(self, text: str) -> str:
        """Озвучивание текста"""
        if not self.tts_available:
            return "❌ Модуль озвучки недоступен"
        if not text.strip():
            return "❌ Текст пустой"
        try:
            self.tts.say(text)
            self.tts.runAndWait()
            voice_name = self.voices[self.current_voice_index].name if self.voices else "Неизвестный"
            return f"🔊 Произнесено голосом '{voice_name}': {text}"
        except Exception as e:
            return f"❌ Ошибка озвучки: {str(e)}"


class SpeedTestClass:
    """Класс для тестирования скорости интернета"""
    @staticmethod
    def humansize(nbytes: float) -> str:
        """Конвертация байтов в человекочитаемый формат"""
        suffixes = ['B', 'KB', 'MB', 'GB', 'TB', 'PB']
        i = 0
        while nbytes >= 1024 and i < len(suffixes) - 1:
            nbytes /= 1024.0
            i += 1
        f = ('%.2f' % nbytes).rstrip('0').rstrip('.')
        return f'{f} {suffixes[i]}'

    def test_speed(self, callback: Callable[[str], None]):
        """Тест скорости интернета в отдельном потоке"""
        def run():
            try:
                callback("🔄 Тест запущен... Подождите")
                st = speedtest.Speedtest()
                callback("🌐 Поиск лучшего сервера...")
                st.get_best_server()
                callback("⬇️ Тест загрузки...")
                download = st.download()
                callback("⬆️ Тест отдачи...")
                upload = st.upload()
                ping = st.results.ping
                result = (
                    f"📊 Результаты теста скорости:\n"
                    f"{'='*40}\n"
                    f"⬇️ Загрузка: {self.humansize(download)}\n"
                    f"⬆️ Отдача: {self.humansize(upload)}\n"
                    f"🏓 Пинг: {ping:.1f} мс\n"
                    f"🌐 Сервер: {st.results.server['name']}"
                )
                callback(result)
            except Exception as e:
                callback(f"❌ Ошибка теста: {str(e)}")
        thread = threading.Thread(target=run, daemon=True)
        thread.start()


class ModernApp:
    """Современное приложение с улучшенным интерфейсом"""
    def __init__(self, root: tk.Tk):
        self.root = root
        self.setup_main_window()
        self.setup_styles()
        self.initialize_modules()
        self.create_interface()

    def setup_main_window(self):
        """Настройка главного окна"""
        self.root.title("🚀 Многофункциональный помощник")
        self.root.geometry("800x600")
        self.root.resizable(True, True)
        self.root.configure(bg='#f0f0f0')
        self.center_window()

    def center_window(self):
        """Центрирование окна на экране"""
        self.root.update_idletasks()
        width = self.root.winfo_width()
        height = self.root.winfo_height()
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry(f'{width}x{height}+{x}+{y}')

    def setup_styles(self):
        """Настройка стилей"""
        style = ttk.Style()
        style.theme_use('clam')
        style.configure('TNotebook', background='#f0f0f0')
        style.configure('TFrame', background='#f0f0f0')
        style.configure('TButton', padding=10, font=('Segoe UI', 9))
        style.configure('TLabel', background='#f0f0f0', font=('Segoe UI', 9))
        style.configure('TEntry', padding=5, font=('Segoe UI', 9))

    def initialize_modules(self):
        """Инициализация модулей"""
        self.programm = ProgrammClass()
        self.speed_test = SpeedTestClass()
        self.calculator = CalculatorClass()

    def create_interface(self):
        """Создание интерфейса"""
        main_frame = ttk.Frame(self.root)
        main_frame.pack(fill='both', expand=True, padx=10, pady=10)

        title_label = tk.Label(
            main_frame,
            text="🚀 Многофункциональный помощник",
            font=('Segoe UI', 18, 'bold'),
            bg='#f0f0f0',
            fg='#2c3e50'
        )
        title_label.pack(pady=(0, 20))

        self.tab_control = ttk.Notebook(main_frame)
        self.calc_tab = ttk.Frame(self.tab_control)
        self.math_tab = ttk.Frame(self.tab_control)
        self.programs_tab = ttk.Frame(self.tab_control)
        self.tab_control.add(self.calc_tab, text='🧮 Калькулятор')
        self.tab_control.add(self.math_tab, text='📐 Математика')
        self.tab_control.add(self.programs_tab, text='⚙️ Программы')
        self.tab_control.pack(expand=True, fill='both')

        self.create_calculator_tab()
        self.create_math_tab()
        self.create_programs_tab()

    def create_calculator_tab(self):
        frame = self.calc_tab
        tk.Label(
            frame,
            text="🧮 Калькулятор",
            font=('Segoe UI', 16, 'bold'),
            bg='#f0f0f0',
            fg='#2c3e50'
        ).pack(pady=20)

        canvas = tk.Canvas(frame, bg='#f0f0f0', highlightthickness=0)
        scrollbar = ttk.Scrollbar(frame, orient="vertical", command=canvas.yview)
        scrollable_frame = tk.Frame(canvas, bg='#f0f0f0')
        scrollable_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw", tags="window")
        canvas.configure(yscrollcommand=scrollbar.set)

        def center_content(event=None):
            try:
                canvas_width = canvas.winfo_width()
                scrollable_width = scrollable_frame.winfo_reqwidth()
                if canvas_width > scrollable_width and scrollable_width > 0:
                    x = (canvas_width - scrollable_width) // 2
                else:
                    x = 0
                canvas.coords(canvas.find_withtag("window"), x, 0)
            except:
                pass

        canvas.bind('<Configure>', center_content)
        self.root.bind('<Configure>', self.center_title)

        main_calc_frame = tk.Frame(scrollable_frame, bg='#f0f0f0')
        main_calc_frame.pack(fill='both', expand=True, padx=10)

        calc_frame = tk.Frame(main_calc_frame, bg='#f0f0f0')
        calc_frame.pack(side='left', fill='both', expand=True, padx=(0, 10))

        input_frame = tk.Frame(calc_frame, bg='#f0f0f0')
        input_frame.pack(pady=20)

        tk.Label(input_frame, text="Число A:", font=('Segoe UI', 10), bg='#f0f0f0').grid(row=0, column=0, padx=10, pady=10, sticky='e')
        self.calc_a = tk.Entry(input_frame, width=20, font=('Segoe UI', 10), relief='solid', bd=1)
        self.calc_a.grid(row=0, column=1, padx=10, pady=10)

        tk.Label(input_frame, text="Число B:", font=('Segoe UI', 10), bg='#f0f0f0').grid(row=1, column=0, padx=10, pady=10, sticky='e')
        self.calc_b = tk.Entry(input_frame, width=20, font=('Segoe UI', 10), relief='solid', bd=1)
        self.calc_b.grid(row=1, column=1, padx=10, pady=10)

        last_result_frame = tk.Frame(calc_frame, bg='#f0f0f0')
        last_result_frame.pack(pady=10)
        tk.Button(last_result_frame, text="📋 Использовать последний результат", font=('Segoe UI', 9), bg='#95a5a6', fg='white', relief='flat', padx=15, pady=5, command=self.use_last_result).pack()

        result_frame = tk.Frame(calc_frame, bg='#f0f0f0')
        result_frame.pack(pady=20)
        tk.Label(result_frame, text="Результат:", font=('Segoe UI', 10, 'bold'), bg='#f0f0f0').grid(row=0, column=0, padx=10)
        self.calc_result = tk.Label(result_frame, text="Введите числа и выберите операцию", fg="#2c3e50", bg='#f0f0f0', font=('Segoe UI', 10), wraplength=300)
        self.calc_result.grid(row=0, column=1, padx=10)

        button_frame = tk.Frame(calc_frame, bg='#f0f0f0')
        button_frame.pack(pady=20)

        operations = [
            ("➕", "plus", "#27ae60"),
            ("➖", "minus", "#e74c3c"),
            ("✖️", "multiply", "#f39c12"),
            ("➗", "divide", "#3498db"),
            ("%", "modulo", "#9b59b6"),
            ("^", "power", "#e67e22"),
            ("//", "floor_divide", "#1abc9c")
        ]

        advanced_operations = [
            ("&", "bitwise_and", "#8e44ad"),
            ("|", "bitwise_or", "#e67e22"),
            ("⊕", "bitwise_xor", "#f39c12"),
            ("<<", "bitwise_left_shift", "#16a085"),
            (">>", "bitwise_right_shift", "#d35400"),
            ("~", "bitwise_not", "#c0392b"),
            ("НОД", "gcd", "#2980b9"),
            ("НОК", "lcm", "#8e44ad"),
            ("Г", "hypotenuse", "#27ae60"),
            ("Р", "distance", "#e74c3c"),
            ("С", "average", "#f39c12"),
            ("СГ", "geometric_mean", "#9b59b6"),
            ("СГар", "harmonic_mean", "#1abc9c"),
            ("min", "min", "#34495e"),
            ("max", "max", "#e67e22"),
            ("%от", "percentage", "#3498db"),
            ("%изм", "percentage_change", "#e74c3c"),
            (":", "ratio", "#f39c12"),
            ("1/x+1/y", "reciprocal_sum", "#9b59b6"),
            ("a²+b²", "square_sum", "#16a085"),
            ("a²-b²", "square_diff", "#d35400"),
            ("a³+b³", "cube_sum", "#c0392b"),
            ("a³-b³", "cube_diff", "#2980b9")
        ]

        for i, (symbol, op, color) in enumerate(operations):
            btn = tk.Button(button_frame, text=symbol, width=8, height=2, font=('Segoe UI', 12, 'bold'), bg=color, fg='white', relief='flat', command=lambda o=op: self.calculate(o))
            btn.grid(row=i // 4, column=i % 4, padx=5, pady=5)
            btn.bind('<Enter>', lambda e, b=btn: b.config(bg=self.lighten_color(color)))
            btn.bind('<Leave>', lambda e, b=btn, c=color: b.config(bg=c))

        tk.Label(button_frame, text="Расширенные операции:", font=('Segoe UI', 10, 'bold'), bg='#f0f0f0', fg='#2c3e50').grid(row=2, column=0, columnspan=4, pady=(20, 10), sticky='w')

        for i, (symbol, op, color) in enumerate(advanced_operations):
            btn = tk.Button(button_frame, text=symbol, width=8, height=2, font=('Segoe UI', 10, 'bold'), bg=color, fg='white', relief='flat', command=lambda o=op: self.calculate(o))
            row = 3 + (i // 4)
            col = i % 4
            btn.grid(row=row, column=col, padx=5, pady=5)
            btn.bind('<Enter>', lambda e, b=btn: b.config(bg=self.lighten_color(color)))
            btn.bind('<Leave>', lambda e, b=btn, c=color: b.config(bg=c))

        history_frame = tk.Frame(main_calc_frame, bg='#f0f0f0')
        history_frame.pack(side='right', fill='both', expand=True, padx=(10, 0))

        history_header = tk.Frame(history_frame, bg='#f0f0f0')
        history_header.pack(fill='x', pady=(0, 10))
        tk.Label(history_header, text="📚 История операций", font=('Segoe UI', 12, 'bold'), bg='#f0f0f0', fg='#2c3e50').pack(side='left')
        tk.Button(history_header, text="🗑️ Очистить", font=('Segoe UI', 8), bg='#e74c3c', fg='white', relief='flat', padx=10, pady=3, command=self.clear_calculator_history).pack(side='right')

        self.history_text = scrolledtext.ScrolledText(history_frame, wrap=tk.WORD, width=35, height=20, font=('Consolas', 9), bg='white', fg='#2c3e50', state=tk.DISABLED)
        self.history_text.pack(fill='both', expand=True)

        def _on_history_mousewheel(event):
            self.history_text.yview_scroll(int(-1*(event.delta/120)), "units")
        self.history_text.bind("<MouseWheel>", _on_history_mousewheel)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        def _on_mousewheel(event):
            canvas.yview_scroll(int(-1*(event.delta/120)), "units")
        canvas.bind("<MouseWheel>", _on_mousewheel)

        self.update_history_display()

    def lighten_color(self, color: str) -> str:
        colors = {
            '#27ae60': '#2ecc71', '#e74c3c': '#e74c3c', '#f39c12': '#f1c40f',
            '#3498db': '#3498db', '#9b59b6': '#9b59b6', '#e67e22': '#e67e22',
            '#1abc9c': '#1abc9c', '#8e44ad': '#9b59b6', '#16a085': '#1abc9c',
            '#d35400': '#e67e22', '#c0392b': '#e74c3c', '#2980b9': '#3498db',
            '#34495e': '#95a5a6', '#f39c12': '#f1c40f', '#9b59b6': '#8e44ad',
            '#1abc9c': '#2ecc71', '#16a085': '#1abc9c', '#d35400': '#e67e22',
            '#c0392b': '#e74c3c', '#2980b9': '#3498db'
        }
        return colors.get(color, color)

    def calculate(self, operation: str):
        """Выполнение математических операций"""
        try:
            a = float(self.calc_a.get())
            b = float(self.calc_b.get())
            method = getattr(CalculatorClass, operation)
            result = method(a, b)
            operation_text = f"{a} {operation} {b}"
            self.calculator.add_to_history(operation_text, result)
            self.calc_result.config(text=result, fg="#2c3e50")
            self.update_history_display()
        except ValueError:
            self.calc_result.config(text="❌ Введите корректные числа", fg="#e74c3c")
        except Exception as e:
            self.calc_result.config(text=f"❌ Ошибка: {str(e)}", fg="#e74c3c")

    def use_last_result(self):
        """Использование последнего результата в качестве первого числа"""
        last_result = self.calculator.get_last_result()
        if not last_result:
            messagebox.showinfo("📋", "История пуста")
            return

        if "❌" in last_result or "Ошибка" in last_result:
            messagebox.showwarning("⚠️", "Последний результат — ошибка, использовать нельзя")
            return

        try:
            if "=" in last_result:
                value_str = last_result.split("=")[1].strip()
                numbers = re.findall(r'-?\d+\.?\d*', value_str)
                if numbers:
                    self.calc_a.delete(0, tk.END)
                    self.calc_a.insert(0, numbers[0])
                    messagebox.showinfo("📋", f"Использован результат: {numbers[0]}")
                    return
            messagebox.showwarning("⚠️", "Не удалось извлечь число из результата")
        except Exception as e:
            messagebox.showerror("❌", f"Ошибка при извлечении: {e}")

    def update_history_display(self):
        """Обновление отображения истории"""
        history = self.calculator.get_history()
        self.history_text.config(state=tk.NORMAL)
        self.history_text.delete(1.0, tk.END)
        if not history:
            self.history_text.insert(tk.END, "История пуста\n")
        else:
            for entry in history:
                timestamp = entry['timestamp']
                operation = entry['operation']
                result = entry['result']
                history_line = f"[{timestamp}] {operation}\n"
                history_line += f"    → {result}\n"
                history_line += "-" * 40 + "\n"
                self.history_text.insert(tk.END, history_line)
        self.history_text.config(state=tk.DISABLED)
        self.history_text.see(tk.END)

    def clear_calculator_history(self):
        """Очистка истории калькулятора"""
        if messagebox.askyesno("🗑️ Очистить историю", "Вы уверены, что хотите очистить историю операций?"):
            self.calculator.clear_history()
            self.update_history_display()
            messagebox.showinfo("✅", "История очищена")

    def create_math_tab(self):
        frame = self.math_tab
        tk.Label(frame, text="📐 Математические функции", font=('Segoe UI', 16, 'bold'), bg='#f0f0f0', fg='#2c3e50').pack(pady=20)

        canvas = tk.Canvas(frame, bg='#f0f0f0', highlightthickness=0)
        scrollbar = ttk.Scrollbar(frame, orient="vertical", command=canvas.yview)
        scrollable_frame = tk.Frame(canvas, bg='#f0f0f0')
        scrollable_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw", tags="window")
        canvas.configure(yscrollcommand=scrollbar.set)

        def center_content(event=None):
            try:
                canvas_width = canvas.winfo_width()
                scrollable_width = scrollable_frame.winfo_reqwidth()
                if canvas_width > scrollable_width and scrollable_width > 0:
                    x = (canvas_width - scrollable_width) // 2
                else:
                    x = 0
                canvas.coords(canvas.find_withtag("window"), x, 0)
            except:
                pass

        canvas.bind('<Configure>', center_content)

        tk.Button(scrollable_frame, text="📊 Таблица умножения", font=('Segoe UI', 10), bg='#3498db', fg='white', relief='flat', padx=20, pady=10, command=self.show_table).pack(pady=10)

        rate_frame = tk.Frame(scrollable_frame, bg='#f0f0f0')
        rate_frame.pack(pady=20)
        tk.Label(rate_frame, text="💰 Расчет процентов", font=('Segoe UI', 12, 'bold'), bg='#f0f0f0').pack(pady=10)
        inputs_frame = tk.Frame(rate_frame, bg='#f0f0f0')
        inputs_frame.pack()
        labels = [("Процент:", "p_entry"), ("Рубли:", "x_entry"), ("Копейки:", "y_entry")]
        for i, (label_text, entry_name) in enumerate(labels):
            tk.Label(inputs_frame, text=label_text, font=('Segoe UI', 9), bg='#f0f0f0').grid(row=0, column=i*2, padx=5, pady=5)
            entry = tk.Entry(inputs_frame, width=10, font=('Segoe UI', 9), relief='solid', bd=1)
            entry.grid(row=0, column=i*2+1, padx=5, pady=5)
            setattr(self, entry_name, entry)
        tk.Button(inputs_frame, text="Рассчитать", command=self.calculate_rate, bg='#27ae60', fg='white', relief='flat', padx=15, pady=5).grid(row=0, column=6, padx=10)
        self.rate_result = tk.Label(frame, text="", fg="#2c3e50", bg='#f0f0f0', font=('Segoe UI', 10), wraplength=400)
        self.rate_result.pack(pady=10)

        calc_frame = tk.Frame(scrollable_frame, bg='#f0f0f0')
        calc_frame.pack(pady=20)
        tk.Label(calc_frame, text="🔬 Инженерный калькулятор", font=('Segoe UI', 12, 'bold'), bg='#f0f0f0').pack(pady=10)

        calc_notebook = ttk.Notebook(calc_frame)
        calc_notebook.pack(fill='x', pady=10)

        trig_frame = ttk.Frame(calc_notebook)
        calc_notebook.add(trig_frame, text='📐 Тригонометрия')
        trig_inputs = tk.Frame(trig_frame, bg='#f0f0f0')
        trig_inputs.pack(pady=10)
        tk.Label(trig_inputs, text="Число:", font=('Segoe UI', 9), bg='#f0f0f0').grid(row=0, column=0, padx=5, pady=5)
        self.trig_num = tk.Entry(trig_inputs, width=15, font=('Segoe UI', 9), relief='solid', bd=1)
        self.trig_num.grid(row=0, column=1, padx=5, pady=5)
        tk.Label(trig_inputs, text="Функция:", font=('Segoe UI', 9), bg='#f0f0f0').grid(row=0, column=2, padx=5, pady=5)
        self.trig_op = ttk.Combobox(trig_inputs, values=["sin", "cos", "tan", "asin", "acos", "atan", "sinh", "cosh", "tanh"], width=12, font=('Segoe UI', 9))
        self.trig_op.grid(row=0, column=3, padx=5, pady=5)
        self.trig_op.current(0)
        tk.Button(trig_inputs, text="Вычислить", command=self.calculate_trig, bg='#3498db', fg='white', relief='flat', padx=15, pady=5).grid(row=0, column=4, padx=10)

        alg_frame = ttk.Frame(calc_notebook)
        calc_notebook.add(alg_frame, text='🔢 Алгебра')
        alg_inputs = tk.Frame(alg_frame, bg='#f0f0f0')
        alg_inputs.pack(pady=10)
        tk.Label(alg_inputs, text="Число:", font=('Segoe UI', 9), bg='#f0f0f0').grid(row=0, column=0, padx=5, pady=5)
        self.alg_num = tk.Entry(alg_inputs, width=15, font=('Segoe UI', 9), relief='solid', bd=1)
        self.alg_num.grid(row=0, column=1, padx=5, pady=5)
        tk.Label(alg_inputs, text="Функция:", font=('Segoe UI', 9), bg='#f0f0f0').grid(row=0, column=2, padx=5, pady=5)
        self.alg_op = ttk.Combobox(alg_inputs, values=["sqrt", "cbrt", "pow2", "pow3", "factorial", "abs", "floor", "ceil", "round"], width=12, font=('Segoe UI', 9))
        self.alg_op.grid(row=0, column=3, padx=5, pady=5)
        self.alg_op.current(0)
        tk.Button(alg_inputs, text="Вычислить", command=self.calculate_alg, bg='#e67e22', fg='white', relief='flat', padx=15, pady=5).grid(row=0, column=4, padx=10)

        log_frame = ttk.Frame(calc_notebook)
        calc_notebook.add(log_frame, text='📊 Логарифмы')
        log_inputs = tk.Frame(log_frame, bg='#f0f0f0')
        log_inputs.pack(pady=10)
        tk.Label(log_inputs, text="Число:", font=('Segoe UI', 9), bg='#f0f0f0').grid(row=0, column=0, padx=5, pady=5)
        self.log_num = tk.Entry(log_inputs, width=15, font=('Segoe UI', 9), relief='solid', bd=1)
        self.log_num.grid(row=0, column=1, padx=5, pady=5)
        tk.Label(log_inputs, text="Функция:", font=('Segoe UI', 9), bg='#f0f0f0').grid(row=0, column=2, padx=5, pady=5)
        self.log_op = ttk.Combobox(log_inputs, values=["log10", "ln", "log2", "exp", "exp10", "exp2", "reciprocal"], width=12, font=('Segoe UI', 9))
        self.log_op.grid(row=0, column=3, padx=5, pady=5)
        self.log_op.current(0)
        tk.Button(log_inputs, text="Вычислить", command=self.calculate_log, bg='#9b59b6', fg='white', relief='flat', padx=15, pady=5).grid(row=0, column=4, padx=10)

        extra_frame = ttk.Frame(calc_notebook)
        calc_notebook.add(extra_frame, text='✨ Дополнительно')
        extra_inputs = tk.Frame(extra_frame, bg='#f0f0f0')
        extra_inputs.pack(pady=10)
        tk.Label(extra_inputs, text="Число:", font=('Segoe UI', 9), bg='#f0f0f0').grid(row=0, column=0, padx=5, pady=5)
        self.extra_num = tk.Entry(extra_inputs, width=15, font=('Segoe UI', 9), relief='solid', bd=1)
        self.extra_num.grid(row=0, column=1, padx=5, pady=5)
        tk.Label(extra_inputs, text="Функция:", font=('Segoe UI', 9), bg='#f0f0f0').grid(row=0, column=2, padx=5, pady=5)
        self.extra_op = ttk.Combobox(extra_inputs, values=["square_root", "cube_root", "inverse", "percent", "degrees_to_radians", "radians_to_degrees", "pi_multiply", "e_multiply"], width=12, font=('Segoe UI', 9))
        self.extra_op.grid(row=0, column=3, padx=5, pady=5)
        self.extra_op.current(0)
        tk.Button(extra_inputs, text="Вычислить", command=self.calculate_extra, bg='#27ae60', fg='white', relief='flat', padx=15, pady=5).grid(row=0, column=4, padx=10)

        dual_frame = ttk.Frame(calc_notebook)
        calc_notebook.add(dual_frame, text='🔗 Два числа')
        dual_inputs = tk.Frame(dual_frame, bg='#f0f0f0')
        dual_inputs.pack(pady=10)
        tk.Label(dual_inputs, text="Число 1:", font=('Segoe UI', 9), bg='#f0f0f0').grid(row=0, column=0, padx=5, pady=5)
        self.dual_num1 = tk.Entry(dual_inputs, width=15, font=('Segoe UI', 9), relief='solid', bd=1)
        self.dual_num1.grid(row=0, column=1, padx=5, pady=5)
        tk.Label(dual_inputs, text="Число 2:", font=('Segoe UI', 9), bg='#f0f0f0').grid(row=0, column=2, padx=5, pady=5)
        self.dual_num2 = tk.Entry(dual_inputs, width=15, font=('Segoe UI', 9), relief='solid', bd=1)
        self.dual_num2.grid(row=0, column=3, padx=5, pady=5)
        tk.Label(dual_inputs, text="Функция:", font=('Segoe UI', 9), bg='#f0f0f0').grid(row=0, column=4, padx=5, pady=5)
        self.dual_op = ttk.Combobox(dual_inputs, values=["power", "root", "log_base", "mod", "gcd", "lcm", "hypotenuse", "distance", "average", "min", "max"], width=12, font=('Segoe UI', 9))
        self.dual_op.grid(row=0, column=5, padx=5, pady=5)
        self.dual_op.current(0)
        tk.Button(dual_inputs, text="Вычислить", command=self.calculate_dual, bg='#e74c3c', fg='white', relief='flat', padx=15, pady=5).grid(row=0, column=6, padx=10)

        self.scientific_result = tk.Label(scrollable_frame, text="", fg="#2c3e50", bg='#f0f0f0', font=('Segoe UI', 10), wraplength=600)
        self.scientific_result.pack(pady=10)

        self.scientific_num = tk.Entry()
        self.scientific_op = ttk.Combobox()

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        def _on_mousewheel(event):
            canvas.yview_scroll(int(-1*(event.delta/120)), "units")
        canvas.bind("<MouseWheel>", _on_mousewheel)

    def show_table(self):
        result = MathematicalClass.multiplication_table()
        self.show_result_window("📊 Таблица умножения", result)

    def calculate_rate(self):
        try:
            p = float(self.p_entry.get())
            x = int(self.x_entry.get())
            y = int(self.y_entry.get())
            result = MathematicalClass.interest_rate(p, x, y)
            self.rate_result.config(text=result, fg="#2c3e50")
        except ValueError:
            self.rate_result.config(text="❌ Введите корректные числа", fg="#e74c3c")
        except Exception:
            self.rate_result.config(text="❌ Ошибка расчета", fg="#e74c3c")

    def calculate_trig(self):
        try:
            num = float(self.trig_num.get())
            op = self.trig_op.get()
            result = MathematicalClass.scientific_calc(num, op)
            self.scientific_result.config(text=f"Результат: {result}", fg="#2c3e50")
        except ValueError:
            self.scientific_result.config(text="❌ Введите корректное число", fg="#e74c3c")
        except Exception:
            self.scientific_result.config(text="❌ Ошибка вычисления", fg="#e74c3c")

    def calculate_alg(self):
        try:
            num = float(self.alg_num.get())
            op = self.alg_op.get()
            result = MathematicalClass.scientific_calc(num, op)
            self.scientific_result.config(text=f"Результат: {result}", fg="#2c3e50")
        except ValueError:
            self.scientific_result.config(text="❌ Введите корректное число", fg="#e74c3c")
        except Exception:
            self.scientific_result.config(text="❌ Ошибка вычисления", fg="#e74c3c")

    def calculate_log(self):
        try:
            num = float(self.log_num.get())
            op = self.log_op.get()
            result = MathematicalClass.scientific_calc(num, op)
            self.scientific_result.config(text=f"Результат: {result}", fg="#2c3e50")
        except ValueError:
            self.scientific_result.config(text="❌ Введите корректное число", fg="#e74c3c")
        except Exception:
            self.scientific_result.config(text="❌ Ошибка вычисления", fg="#e74c3c")

    def calculate_extra(self):
        try:
            num = float(self.extra_num.get())
            op = self.extra_op.get()
            result = MathematicalClass.scientific_calc(num, op)
            self.scientific_result.config(text=f"Результат: {result}", fg="#2c3e50")
        except ValueError:
            self.scientific_result.config(text="❌ Введите корректное число", fg="#e74c3c")
        except Exception:
            self.scientific_result.config(text="❌ Ошибка вычисления", fg="#e74c3c")

    def calculate_dual(self):
        try:
            num1 = float(self.dual_num1.get())
            num2 = float(self.dual_num2.get())
            op = self.dual_op.get()
            result = MathematicalClass.advanced_calc(num1, num2, op)
            self.scientific_result.config(text=f"Результат: {result}", fg="#2c3e50")
        except ValueError:
            self.scientific_result.config(text="❌ Введите корректные числа", fg="#e74c3c")
        except Exception:
            self.scientific_result.config(text="❌ Ошибка вычисления", fg="#e74c3c")

    def calculate_scientific(self):
        try:
            num = float(self.scientific_num.get())
            op = self.scientific_op.get()
            result = MathematicalClass.scientific_calc(num, op)
            self.scientific_result.config(text=f"Результат: {result}", fg="#2c3e50")
        except ValueError:
            self.scientific_result.config(text="❌ Введите корректное число", fg="#e74c3c")
        except Exception:
            self.scientific_result.config(text="❌ Ошибка вычисления", fg="#e74c3c")

    def create_programs_tab(self):
        frame = self.programs_tab
        tk.Label(frame, text="⚙️ Программы", font=('Segoe UI', 16, 'bold'), bg='#f0f0f0', fg='#2c3e50').pack(pady=20)

        canvas = tk.Canvas(frame, bg='#f0f0f0', highlightthickness=0)
        scrollbar = ttk.Scrollbar(frame, orient="vertical", command=canvas.yview)
        scrollable_frame = tk.Frame(canvas, bg='#f0f0f0')
        scrollable_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw", tags="window")
        canvas.configure(yscrollcommand=scrollbar.set)

        def center_content(event=None):
            try:
                canvas_width = canvas.winfo_width()
                scrollable_width = scrollable_frame.winfo_reqwidth()
                if canvas_width > scrollable_width and scrollable_width > 0:
                    x = (canvas_width - scrollable_width) // 2
                else:
                    x = 0
                canvas.coords(canvas.find_withtag("window"), x, 0)
            except:
                pass

        canvas.bind('<Configure>', center_content)

        speak_frame = tk.Frame(scrollable_frame, bg='#f0f0f0')
        speak_frame.pack(pady=20)
        tk.Label(speak_frame, text="🔊 Озвучка текста", font=('Segoe UI', 12, 'bold'), bg='#f0f0f0').pack(pady=10)

        voice_settings_frame = tk.Frame(speak_frame, bg='#f0f0f0')
        voice_settings_frame.pack(pady=10)
        tk.Label(voice_settings_frame, text="Голос:", font=('Segoe UI', 9), bg='#f0f0f0').grid(row=0, column=0, padx=5, pady=5, sticky='e')
        self.voice_combobox = ttk.Combobox(voice_settings_frame, width=30, font=('Segoe UI', 9), state='readonly')
        self.voice_combobox.grid(row=0, column=1, padx=5, pady=5)
        tk.Button(voice_settings_frame, text="🔄 Обновить", command=self.refresh_voices, bg='#3498db', fg='white', relief='flat', padx=10, pady=3, font=('Segoe UI', 8)).grid(row=0, column=2, padx=5, pady=5)
        tk.Label(voice_settings_frame, text="Скорость:", font=('Segoe UI', 9), bg='#f0f0f0').grid(row=1, column=0, padx=5, pady=5, sticky='e')
        self.rate_scale = tk.Scale(voice_settings_frame, from_=50, to=300, orient='horizontal', length=200, bg='#f0f0f0', fg='#2c3e50', highlightthickness=0)
        self.rate_scale.set(150)
        self.rate_scale.grid(row=1, column=1, padx=5, pady=5)
        tk.Button(voice_settings_frame, text="📊 Применить", command=self.apply_rate, bg='#e67e22', fg='white', relief='flat', padx=10, pady=3, font=('Segoe UI', 8)).grid(row=1, column=2, padx=5, pady=5)
        tk.Label(voice_settings_frame, text="Громкость:", font=('Segoe UI', 9), bg='#f0f0f0').grid(row=2, column=0, padx=5, pady=5, sticky='e')
        self.volume_scale = tk.Scale(voice_settings_frame, from_=0.0, to=1.0, resolution=0.1, orient='horizontal', length=200, bg='#f0f0f0', fg='#2c3e50', highlightthickness=0)
        self.volume_scale.set(0.9)
        self.volume_scale.grid(row=2, column=1, padx=5, pady=5)
        tk.Button(voice_settings_frame, text="🔊 Применить", command=self.apply_volume, bg='#f39c12', fg='white', relief='flat', padx=10, pady=3, font=('Segoe UI', 8)).grid(row=2, column=2, padx=5, pady=5)
        self.voice_info_label = tk.Label(voice_settings_frame, text="", font=('Segoe UI', 9), bg='#f0f0f0', fg='#2c3e50', wraplength=400, justify='left')
        self.voice_info_label.grid(row=3, column=0, columnspan=3, pady=10)
        tk.Button(voice_settings_frame, text="ℹ️ Информация о голосе", command=self.show_voice_info, bg='#9b59b6', fg='white', relief='flat', padx=15, pady=5, font=('Segoe UI', 9)).grid(row=4, column=0, columnspan=3, pady=5)

        input_speak_frame = tk.Frame(speak_frame, bg='#f0f0f0')
        input_speak_frame.pack(pady=10)
        tk.Label(input_speak_frame, text="Текст:", font=('Segoe UI', 9), bg='#f0f0f0').grid(row=0, column=0, padx=5, pady=5)
        self.speak_text = tk.Entry(input_speak_frame, width=40, font=('Segoe UI', 9), relief='solid', bd=1)
        self.speak_text.grid(row=0, column=1, padx=5, pady=5)
        tk.Button(input_speak_frame, text="🔊 Озвучить", command=self.speak, bg='#9b59b6', fg='white', relief='flat', padx=20, pady=5).grid(row=0, column=2, padx=10)

        speed_frame = tk.Frame(scrollable_frame, bg='#f0f0f0')
        speed_frame.pack(pady=30)
        tk.Button(speed_frame, text="🌐 Проверить скорость интернета", font=('Segoe UI', 10), bg='#e74c3c', fg='white', relief='flat', padx=20, pady=10, command=self.test_speed).pack(pady=10)
        self.speed_label = tk.Label(speed_frame, text="Нажмите кнопку для проверки скорости", justify="left", fg="#2c3e50", bg='#f0f0f0', font=('Segoe UI', 9), wraplength=500)
        self.speed_label.pack(pady=10)

        self.refresh_voices()

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        def _on_mousewheel(event):
            canvas.yview_scroll(int(-1*(event.delta/120)), "units")
        canvas.bind("<MouseWheel>", _on_mousewheel)

    def speak(self):
        text = self.speak_text.get()
        if not text.strip():
            messagebox.showwarning("⚠️ Предупреждение", "Введите текст для озвучки")
            return
        result = self.programm.speak_text(text)
        messagebox.showinfo("🔊 Озвучка", result)

    def refresh_voices(self):
        try:
            voices_info = self.programm.get_voices_info()
            if voices_info:
                voice_list = []
                for voice in voices_info:
                    voice_name = voice['name']
                    if voice['languages']:
                        voice_name += f" ({', '.join(voice['languages'])})"
                    voice_list.append(voice_name)
                self.voice_combobox['values'] = voice_list
                if voice_list:
                    self.voice_combobox.current(0)
                    self.voice_combobox.bind('<<ComboboxSelected>>', self.on_voice_changed)
                messagebox.showinfo("✅", f"Найдено {len(voices_info)} голосов")
                self.update_voice_info()
            else:
                messagebox.showwarning("⚠️", "Голоса не найдены")
        except Exception as e:
            messagebox.showerror("❌ Ошибка", f"Не удалось обновить список голосов:\n{str(e)}")

    def on_voice_changed(self, event=None):
        try:
            selected_index = self.voice_combobox.current()
            if selected_index >= 0:
                result = self.programm.change_voice(selected_index)
                messagebox.showinfo("🎤 Изменение голоса", result)
                self.update_voice_info()
        except Exception as e:
            messagebox.showerror("❌ Ошибка", f"Не удалось изменить голос:\n{str(e)}")

    def apply_rate(self):
        try:
            new_rate = self.rate_scale.get()
            result = self.programm.change_rate(new_rate)
            messagebox.showinfo("📊 Изменение скорости", result)
            self.update_voice_info()
        except Exception as e:
            messagebox.showerror("❌ Ошибка", f"Не удалось изменить скорость:\n{str(e)}")

    def apply_volume(self):
        try:
            new_volume = self.volume_scale.get()
            result = self.programm.change_volume(new_volume)
            messagebox.showinfo("🔊 Изменение громкости", result)
            self.update_voice_info()
        except Exception as e:
            messagebox.showerror("❌ Ошибка", f"Не удалось изменить громкость:\n{str(e)}")

    def update_voice_info(self):
        try:
            info = self.programm.get_current_voice_info()
            self.voice_info_label.config(text=info)
        except Exception:
            self.voice_info_label.config(text="❌ Не удалось получить информацию о голосе")

    def show_voice_info(self):
        try:
            voices_info = self.programm.get_voices_info()
            if voices_info:
                info_text = "🎤 Доступные голоса:\n" + "=" * 50 + "\n"
                for voice in voices_info:
                    info_text += f"📌 {voice['name']}\n"
                    info_text += f"   ID: {voice['id']}\n"
                    if voice['languages']:
                        info_text += f"   Языки: {', '.join(voice['languages'])}\n"
                    if voice['gender']:
                        info_text += f"   Пол: {voice['gender']}\n"
                    if voice['age']:
                        info_text += f"   Возраст: {voice['age']}\n"
                    info_text += "-" * 30 + "\n"
                self.show_result_window("🎤 Информация о голосах", info_text)
            else:
                messagebox.showwarning("⚠️", "Голоса не найдены")
        except Exception as e:
            messagebox.showerror("❌ Ошибка", f"Не удалось получить информацию о голосах:\n{str(e)}")

    def test_speed(self):
        self.speed_label.config(text="🔄 Тест запущен... Подождите", fg="#f39c12")
        self.root.update_idletasks()  # Обновляем интерфейс
        self.speed_test.test_speed(self.display_speed_result)

    def display_speed_result(self, result: str):
        self.speed_label.config(text=result, fg="#2c3e50")

    def center_title(self, event=None):
        try:
            main_frame = self.title_label.master
            frame_width = main_frame.winfo_width()
            label_width = self.title_label.winfo_reqwidth()
            if frame_width > label_width and label_width > 0:
                x = (frame_width - label_width) // 2
                self.title_label.pack_configure(padx=(x, 0))
        except:
            pass

    def show_result_window(self, title: str, content: str):
        win = tk.Toplevel(self.root)
        win.title(title)
        win.geometry("600x500")
        win.configure(bg='#f0f0f0')
        win.transient(self.root)
        win.grab_set()
        tk.Label(win, text=title, font=('Segoe UI', 14, 'bold'), bg='#f0f0f0', fg='#2c3e50').pack(pady=10)
        text_area = scrolledtext.ScrolledText(win, wrap=tk.WORD, width=70, height=25, font=('Consolas', 9), bg='white', fg='#2c3e50')
        text_area.insert(tk.END, content)
        text_area.config(state=tk.DISABLED)
        text_area.pack(padx=20, pady=10, fill='both', expand=True)
        def _on_result_mousewheel(event):
            text_area.yview_scroll(int(-1*(event.delta/120)), "units")
        text_area.bind("<MouseWheel>", _on_result_mousewheel)
        tk.Button(win, text="❌ Закрыть", command=win.destroy, bg='#e74c3c', fg='white', relief='flat', padx=20, pady=5).pack(pady=10)


def main():
    try:
        root = tk.Tk()
        app = ModernApp(root)
        root.mainloop()
    except Exception as e:
        messagebox.showerror("❌ Ошибка", f"Не удалось запустить приложение:\n{str(e)}")


if __name__ == "__main__":
    main()