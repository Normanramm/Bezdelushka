from unittest import TestCase, main
import Bezdelushka


class QwertyTest(TestCase):
    def test_calculate_functions(self):
        self.assertEqual(Bezdelushka.MathematicalClass(1,1),1)


        if __name__ == '__main__':
            main()
