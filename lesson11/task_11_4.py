__author__ = 'Рейтер Валерия Борисовна'

# 4. Реализовать проект «Операции с комплексными числами».
# Техническое задание:
#
# Создайте класс «Комплексное число». Комплексное число - это упорядоченная пара чисел, например x,y. Для простоты
# числа берем только целые.
# Перегрузите методы(операторы) сложения/вычитания и умножения комплексных чисел (три метода). Правила
# сложения/умножения можно найти в сети.
# Перегрузите метод __str__ для вывода числа в виде x + yj, где x,y - атрибуты. Попробуйте учесть, что y может быть
# отрицательным.
# Создайте экземпляры класса (комплексные числа), выполните сложение/вычитание/умножение созданных экземпляров.
# Выведите на экран результат.
# Встроенным типом данных complex пользоваться нельзя. Найдите в интернете описание правил сложения/вычитания и
# умножения комплексных чисел.
# При переопределении операторов помним, что возвращается новый объект, Аргументы остаются неизменными.
# Примеры/Тесты:
# Например так:
#
#
# Число 1: 2+3j
# Число 2: -1+1j
# Сложение: 1+4j
# Вычитание: 3+2j
# Умножение: -5-1j


class ComplexNumber:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        if isinstance(other, ComplexNumber):
            x = self.x + other.x
            y = self.y + other.y
            return ComplexNumber(x, y)

    def __sub__(self, other):
        if isinstance(other, ComplexNumber):
            x = self.x - other.x
            y = self.y - other.y
            return ComplexNumber(x, y)

    def __mul__(self, other):
        if isinstance(other, ComplexNumber):
            x = self.x * other.x - self.y * other.y
            y = self.x * other.y + self.y * other.x
            return ComplexNumber(x, y)

    def __str__(self):
        if self.y < 0:
            sign = "-"
        else:
            sign = "+"
        return str(f"{self.x}{sign}{abs(self.y)}j")


a1 = ComplexNumber(2, 3)
a2 = ComplexNumber(-1, 1)
print(f"Число 1: {a1}")
print(f"Число 2: {a2}")
print(f"Сложение: {a1+a2}")
print(f"Вычитание: {a1-a2}")
print(f"Умножение: {a1*a2}")
