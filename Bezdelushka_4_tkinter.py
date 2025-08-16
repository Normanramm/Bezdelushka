import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import pyttsx3
import speedtest
import math
import threading
from typing import Optional, Callable


class CalculatorClass:
    """Класс для математических операций"""
    
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
            return f"{a} // {b} = {a // b}"
        except Exception:
            return "❌ Ошибка вычисления"


class MathematicalClass:
    """Класс для математических функций"""
    
    @staticmethod
    def multiplication_table() -> str:
        result = "📊 Таблица умножения\n" + "=" * 50 + "\n\n"
        for i in range(1, 11):
            result += f"🎯 {i} × таблица:\n"
            result += "-" * 30 + "\n"
            row = ""
            for j in range(1, 11):
                row += f"{i:2} × {j:2} = {i*j:3}  "
                if j % 5 == 0:
                    row += "\n"
            result += row + "\n\n"
        return result
    
    @staticmethod
    def interest_rate(p: float, x: int, y: int) -> str:
        try:
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
            elif op == 'sqrt':
                if num < 0:
                    return "❌ Корень из отрицательного числа"
                result = math.sqrt(num)
                return f"√{num} = {result:.6f}"
            elif op == 'pow':
                result = num ** 2
                return f"{num}² = {result:.6f}"
            elif op == 'log':
                if num <= 0:
                    return "❌ Логарифм из неположительного числа"
                result = math.log10(num)
                return f"log₁₀({num}) = {result:.6f}"
            else:
                return "❌ Неизвестная операция"
        except Exception as e:
            return f"❌ Ошибка: {str(e)}"


class ProgrammClass:
    """Класс для работы с программами"""
    
    def __init__(self):
        try:
            self.tts = pyttsx3.init()
            self._setup_voice()
        except Exception:
            self.tts = None
    
    def _setup_voice(self):
        """Настройка голоса для озвучки"""
        try:
            voices = self.tts.getProperty('voices')
            # Пытаемся найти русский голос
            for voice in voices:
                if 'ru' in voice.languages or 'russian' in voice.name.lower():
                    self.tts.setProperty('voice', voice.id)
                    break
            # Настройка скорости и громкости
            self.tts.setProperty('rate', 150)
            self.tts.setProperty('volume', 0.9)
        except Exception:
            pass
    
    def speak_text(self, text: str) -> str:
        """Озвучивание текста"""
        if not self.tts:
            return "❌ Модуль озвучки недоступен"
        
        if not text.strip():
            return "❌ Текст пустой"
        
        try:
            self.tts.say(text)
            self.tts.runAndWait()
            return f"🔊 Произнесено: {text}"
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
        
        # Центрирование окна
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
        
        # Настройка цветов
        style.configure('TNotebook', background='#f0f0f0')
        style.configure('TFrame', background='#f0f0f0')
        style.configure('TButton', padding=10, font=('Segoe UI', 9))
        style.configure('TLabel', background='#f0f0f0', font=('Segoe UI', 9))
        style.configure('TEntry', padding=5, font=('Segoe UI', 9))
    
    def initialize_modules(self):
        """Инициализация модулей"""
        self.programm = ProgrammClass()
        self.speed_test = SpeedTestClass()
    
    def create_interface(self):
        """Создание интерфейса"""
        # Главный контейнер
        main_frame = ttk.Frame(self.root)
        main_frame.pack(fill='both', expand=True, padx=10, pady=10)
        
        # Заголовок
        title_label = tk.Label(
            main_frame, 
            text="🚀 Многофункциональный помощник", 
            font=('Segoe UI', 18, 'bold'),
            bg='#f0f0f0',
            fg='#2c3e50'
        )
        title_label.pack(pady=(0, 20))
        
        # Вкладки
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
        """Создание вкладки калькулятора"""
        frame = self.calc_tab
        
        # Заголовок
        tk.Label(
            frame, 
            text="🧮 Калькулятор", 
            font=('Segoe UI', 16, 'bold'),
            bg='#f0f0f0',
            fg='#2c3e50'
        ).pack(pady=20)
        
        # Поля ввода
        input_frame = tk.Frame(frame, bg='#f0f0f0')
        input_frame.pack(pady=20)
        
        # Число A
        tk.Label(
            input_frame, 
            text="Число A:", 
            font=('Segoe UI', 10),
            bg='#f0f0f0'
        ).grid(row=0, column=0, padx=10, pady=10, sticky='e')
        
        self.calc_a = tk.Entry(
            input_frame, 
            width=20, 
            font=('Segoe UI', 10),
            relief='solid',
            bd=1
        )
        self.calc_a.grid(row=0, column=1, padx=10, pady=10)
        
        # Число B
        tk.Label(
            input_frame, 
            text="Число B:", 
            font=('Segoe UI', 10),
            bg='#f0f0f0'
        ).grid(row=1, column=0, padx=10, pady=10, sticky='e')
        
        self.calc_b = tk.Entry(
            input_frame, 
            width=20, 
            font=('Segoe UI', 10),
            relief='solid',
            bd=1
        )
        self.calc_b.grid(row=1, column=1, padx=10, pady=10)
        
        # Результат
        result_frame = tk.Frame(frame, bg='#f0f0f0')
        result_frame.pack(pady=20)
        
        tk.Label(
            result_frame, 
            text="Результат:", 
            font=('Segoe UI', 10, 'bold'),
            bg='#f0f0f0'
        ).grid(row=0, column=0, padx=10)
        
        self.calc_result = tk.Label(
            result_frame, 
            text="Введите числа и выберите операцию", 
            fg="#2c3e50",
            bg='#f0f0f0',
            font=('Segoe UI', 10),
            wraplength=300
        )
        self.calc_result.grid(row=0, column=1, padx=10)
        
        # Кнопки операций
        button_frame = tk.Frame(frame, bg='#f0f0f0')
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
        
        for i, (symbol, op, color) in enumerate(operations):
            btn = tk.Button(
                button_frame,
                text=symbol,
                width=8,
                height=2,
                font=('Segoe UI', 12, 'bold'),
                bg=color,
                fg='white',
                relief='flat',
                command=lambda o=op: self.calculate(o)
            )
            btn.grid(row=i // 4, column=i % 4, padx=5, pady=5)
            
            # Эффекты наведения
            btn.bind('<Enter>', lambda e, b=btn: b.config(bg=self.lighten_color(color)))
            btn.bind('<Leave>', lambda e, b=btn, c=color: b.config(bg=c))
    
    def lighten_color(self, color: str) -> str:
        """Осветление цвета для эффекта наведения"""
        # Простое осветление цвета
        colors = {
            '#27ae60': '#2ecc71', '#e74c3c': '#e74c3c', '#f39c12': '#f1c40f',
            '#3498db': '#3498db', '#9b59b6': '#9b59b6', '#e67e22': '#e67e22',
            '#1abc9c': '#1abc9c'
        }
        return colors.get(color, color)
    
    def calculate(self, operation: str):
        """Выполнение математических операций"""
        try:
            a = float(self.calc_a.get())
            b = float(self.calc_b.get())
            
            # Получение метода из класса
            method_name = operation.replace('//', 'floor_divide').replace('^', 'power')
            method = getattr(CalculatorClass, method_name)
            result = method(a, b)
            
            self.calc_result.config(text=result, fg="#2c3e50")
        except ValueError:
            self.calc_result.config(text="❌ Введите корректные числа", fg="#e74c3c")
        except Exception as e:
            self.calc_result.config(text=f"❌ Ошибка: {str(e)}", fg="#e74c3c")
    
    def create_math_tab(self):
        """Создание вкладки математики"""
        frame = self.math_tab
        
        # Заголовок
        tk.Label(
            frame, 
            text="📐 Математические функции", 
            font=('Segoe UI', 16, 'bold'),
            bg='#f0f0f0',
            fg='#2c3e50'
        ).pack(pady=20)
        
        # Таблица умножения
        tk.Button(
            frame, 
            text="📊 Таблица умножения",
            font=('Segoe UI', 10),
            bg='#3498db',
            fg='white',
            relief='flat',
            padx=20,
            pady=10,
            command=self.show_table
        ).pack(pady=10)
        
        # Процентная ставка
        rate_frame = tk.Frame(frame, bg='#f0f0f0')
        rate_frame.pack(pady=20)
        
        tk.Label(
            rate_frame, 
            text="💰 Расчет процентов", 
            font=('Segoe UI', 12, 'bold'),
            bg='#f0f0f0'
        ).pack(pady=10)
        
        inputs_frame = tk.Frame(rate_frame, bg='#f0f0f0')
        inputs_frame.pack()
        
        labels = [("Процент:", "p_entry"), ("Рубли:", "x_entry"), ("Копейки:", "y_entry")]
        
        for i, (label_text, entry_name) in enumerate(labels):
            tk.Label(
                inputs_frame, 
                text=label_text, 
                font=('Segoe UI', 9),
                bg='#f0f0f0'
            ).grid(row=0, column=i*2, padx=5, pady=5)
            
            entry = tk.Entry(
                inputs_frame, 
                width=10, 
                font=('Segoe UI', 9),
                relief='solid',
                bd=1
            )
            entry.grid(row=0, column=i*2+1, padx=5, pady=5)
            setattr(self, entry_name, entry)
        
        tk.Button(
            inputs_frame, 
            text="Рассчитать", 
            command=self.calculate_rate,
            bg='#27ae60',
            fg='white',
            relief='flat',
            padx=15,
            pady=5
        ).grid(row=0, column=6, padx=10)
        
        self.rate_result = tk.Label(
            frame, 
            text="", 
            fg="#2c3e50",
            bg='#f0f0f0',
            font=('Segoe UI', 10),
            wraplength=400
        )
        self.rate_result.pack(pady=10)
        
        # Инженерный калькулятор
        calc_frame = tk.Frame(frame, bg='#f0f0f0')
        calc_frame.pack(pady=20)
        
        tk.Label(
            calc_frame, 
            text="🔬 Инженерный калькулятор", 
            font=('Segoe UI', 12, 'bold'),
            bg='#f0f0f0'
        ).pack(pady=10)
        
        inputs_calc_frame = tk.Frame(calc_frame, bg='#f0f0f0')
        inputs_calc_frame.pack()
        
        tk.Label(
            inputs_calc_frame, 
            text="Число:", 
            font=('Segoe UI', 9),
            bg='#f0f0f0'
        ).grid(row=0, column=0, padx=5, pady=5)
        
        self.scientific_num = tk.Entry(
            inputs_calc_frame, 
            width=15, 
            font=('Segoe UI', 9),
            relief='solid',
            bd=1
        )
        self.scientific_num.grid(row=0, column=1, padx=5, pady=5)
        
        tk.Label(
            inputs_calc_frame, 
            text="Функция:", 
            font=('Segoe UI', 9),
            bg='#f0f0f0'
        ).grid(row=0, column=2, padx=5, pady=5)
        
        self.scientific_op = ttk.Combobox(
            inputs_calc_frame, 
            values=["sin", "cos", "tan", "sqrt", "pow", "log"], 
            width=10,
            font=('Segoe UI', 9)
        )
        self.scientific_op.grid(row=0, column=3, padx=5, pady=5)
        self.scientific_op.current(0)
        
        tk.Button(
            inputs_calc_frame, 
            text="Вычислить", 
            command=self.calculate_scientific,
            bg='#e67e22',
            fg='white',
            relief='flat',
            padx=15,
            pady=5
        ).grid(row=0, column=4, padx=10)
        
        self.scientific_result = tk.Label(
            frame, 
            text="", 
            fg="#2c3e50",
            bg='#f0f0f0',
            font=('Segoe UI', 10),
            wraplength=400
        )
        self.scientific_result.pack(pady=10)
    
    def show_table(self):
        """Показать таблицу умножения"""
        result = MathematicalClass.multiplication_table()
        self.show_result_window("📊 Таблица умножения", result)
    
    def calculate_rate(self):
        """Расчет процентной ставки"""
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
    
    def calculate_scientific(self):
        """Вычисление научных функций"""
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
        """Создание вкладки программ"""
        frame = self.programs_tab
        
        # Заголовок
        tk.Label(
            frame, 
            text="⚙️ Программы", 
            font=('Segoe UI', 16, 'bold'),
            bg='#f0f0f0',
            fg='#2c3e50'
        ).pack(pady=20)
        
        # Озвучка
        speak_frame = tk.Frame(frame, bg='#f0f0f0')
        speak_frame.pack(pady=20)
        
        tk.Label(
            speak_frame, 
            text="🔊 Озвучка текста", 
            font=('Segoe UI', 12, 'bold'),
            bg='#f0f0f0'
        ).pack(pady=10)
        
        input_speak_frame = tk.Frame(speak_frame, bg='#f0f0f0')
        input_speak_frame.pack()
        
        tk.Label(
            input_speak_frame, 
            text="Текст:", 
            font=('Segoe UI', 9),
            bg='#f0f0f0'
        ).grid(row=0, column=0, padx=5, pady=5)
        
        self.speak_text = tk.Entry(
            input_speak_frame, 
            width=40, 
            font=('Segoe UI', 9),
            relief='solid',
            bd=1
        )
        self.speak_text.grid(row=0, column=1, padx=5, pady=5)
        
        tk.Button(
            input_speak_frame, 
            text="🔊 Озвучить", 
            command=self.speak,
            bg='#9b59b6',
            fg='white',
            relief='flat',
            padx=20,
            pady=5
        ).grid(row=0, column=2, padx=10)
        
        # Скорость интернета
        speed_frame = tk.Frame(frame, bg='#f0f0f0')
        speed_frame.pack(pady=30)
        
        tk.Button(
            speed_frame, 
            text="🌐 Проверить скорость интернета",
            font=('Segoe UI', 10),
            bg='#e74c3c',
            fg='white',
            relief='flat',
            padx=20,
            pady=10,
            command=self.test_speed
        ).pack(pady=10)
        
        self.speed_label = tk.Label(
            speed_frame, 
            text="Нажмите кнопку для проверки скорости", 
            justify="left", 
            fg="#2c3e50",
            bg='#f0f0f0',
            font=('Segoe UI', 9),
            wraplength=500
        )
        self.speed_label.pack(pady=10)
    
    def speak(self):
        """Озвучивание текста"""
        text = self.speak_text.get()
        if not text.strip():
            messagebox.showwarning("⚠️ Предупреждение", "Введите текст для озвучки")
            return
        
        result = self.programm.speak_text(text)
        messagebox.showinfo("🔊 Озвучка", result)
    
    def test_speed(self):
        """Запуск теста скорости"""
        self.speed_label.config(text="🔄 Тест запущен... Подождите", fg="#f39c12")
        self.speed_test.test_speed(self.display_speed_result)
    
    def display_speed_result(self, result: str):
        """Отображение результата теста скорости"""
        self.speed_label.config(text=result, fg="#2c3e50")
    
    def show_result_window(self, title: str, content: str):
        """Показать окно с результатом"""
        win = tk.Toplevel(self.root)
        win.title(title)
        win.geometry("600x500")
        win.configure(bg='#f0f0f0')
        
        # Центрирование окна
        win.transient(self.root)
        win.grab_set()
        
        # Заголовок
        tk.Label(
            win, 
            text=title, 
            font=('Segoe UI', 14, 'bold'),
            bg='#f0f0f0',
            fg='#2c3e50'
        ).pack(pady=10)
        
        # Область текста
        text_area = scrolledtext.ScrolledText(
            win, 
            wrap=tk.WORD, 
            width=70, 
            height=25,
            font=('Consolas', 9),
            bg='white',
            fg='#2c3e50'
        )
        text_area.insert(tk.END, content)
        text_area.config(state=tk.DISABLED)
        text_area.pack(padx=20, pady=10, fill='both', expand=True)
        
        # Кнопка закрытия
        tk.Button(
            win, 
            text="❌ Закрыть", 
            command=win.destroy,
            bg='#e74c3c',
            fg='white',
            relief='flat',
            padx=20,
            pady=5
        ).pack(pady=10)


def main():
    """Главная функция"""
    try:
        root = tk.Tk()
        app = ModernApp(root)
        root.mainloop()
    except Exception as e:
        messagebox.showerror("❌ Ошибка", f"Не удалось запустить приложение:\n{str(e)}")


if __name__ == "__main__":
    main()
