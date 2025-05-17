from unittest import TestCase, main

# from MyPrograms.alesson import qwerty
#ну или указывать путь к локальному модулю Глобальная папка.папка внутри и импорт модуля

# from maintwo import plus # чтобы импортировать конкретную функцию

import main  # чтобы импортировать все

# from unittest import TestCase, main это лучший вариант юнит тестирования
# from MyPrograms.alesson import qwerty путь к юнит тестированию

'''Образец тестирования'''


class MainTest(TestCase):
    def test_plus(self):
        self.assertEqual(main.plus(1, 1), 2) # проверка на правильность вычисления

    def test_minus(self):
        self.assertEqual(main.minus(1, 1), 0) # cначала добавляем программу потом функцию для тестинга

    def test_divide(self):
        self.assertEqual(main.devide(2, 2), 1)


if __name__ == '__main__':
    main()
