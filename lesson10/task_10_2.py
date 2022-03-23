__author__ = 'Рейтер Валерия Борисовна'

# 2. Реализовать проект расчёта суммарного расхода ткани на производство одежды.
# Формат вывода результата:
#
# Создать не менее 3 экземпляров классов с различными данными.
# Провести расчет ткани для каждого - вывести на экран
# Продемонстрировать накопительный счетчик по каждому классу.
# Техническое задание:
#
# Основная сущность (класс) этого проекта — одежда, которая может иметь определённое название/имя (атрибут).
# К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры: размер
# (для пальто) и рост (для костюма). Это целые числа, например V и H, соответственно.
# Создать метод расчета ткани для каждого класса: пальто, костюм по формуле: для пальто (V/6.5 + 0.5),
# для костюма (2*H + 0.3).
# Выполнить общий подсчёт расхода ткани. Для всех экземпляров пальто и отдельно для всех экземпляров костюма.
# Алгоритм должен работать для любого кол-ва экземпляров.
# Проверить на практике полученные на этом уроке знания. Использовать абстрактный класс для «одежды» и наследование.
# Проверить работу декоратора @property. Не допускайте дублирования кода или спагетти-кода (кода с многочисленными
# проверками условий). Тщательно продумайте что должно быть данными (атрибутами), а что методами.
# Не принципиально будет ли накапливаться общий расход ткани определенным методом или будет скрыт внутри других
# методов/конструктора.
# Примеры/Тесты:
# Здесь специально не показан вывод общего количества ткани, чтобы это не было для вас избыточной подсказкой.
#
#
# >>> c1 = Coat(12)
# >>> c2 = Coat(1)
# >>> c3 = Coat(121)
# >>> c1.add_to_reserve
# >>> c2.add_to_reserve
# >>> c3.add_to_reserve
# >>> print(c1.cloth_require)
# 2.3461538461538463
# >>> print(c2.cloth_require)
# 0.6538461538461539
# >>> print(c3.cloth_require)
# 19.115384615384617
# >>>
#
# Алгоритм:
#
# Исходя из условия задачи подумайте, где здесь абстрактный класс, и какие наследники. Какие методы следует сделать
# абстрактными.
# Как методами ООП реализовать «накопительный счетчик» расхода ткани для всех экземпляров пальто или костюма?
from abc import ABC, abstractmethod


class Clothes(ABC):

    def __init__(self, type):
        self.type = type

    @abstractmethod
    def cloth_require(self):
        pass

    @abstractmethod
    def add_to_reserve(self):
        pass


class Coat(Clothes):
    reserve = 0

    def __init__(self, size):
        self.size = size
        super().__init__("coat")

    @property
    def cloth_require(self):
        return self.size/6.5 + 0.5

    @property
    def add_to_reserve(self):
        Coat.reserve += self.cloth_require


class Suit(Clothes):
    reserve = 0

    def __init__(self, growth):
        self.growth = growth
        super().__init__("suit")

    @property
    def cloth_require(self):
        return 2*self.growth + 0.3

    @property
    def add_to_reserve(self):
        Suit.reserve += self.cloth_require


c1 = Coat(12)
c2 = Coat(1)
c3 = Coat(121)
c1.add_to_reserve
c2.add_to_reserve
c3.add_to_reserve

print(c1.cloth_require)
print(c2.cloth_require)
print(c3.cloth_require)
print(c1.reserve)
print(c2.reserve)
print(c3.reserve)

s1 = Suit(168)
s2 = Suit(187)
s3 = Suit(155)
s1.add_to_reserve
s2.add_to_reserve
s3.add_to_reserve

print(s1.cloth_require)
print(s2.cloth_require)
print(s3.cloth_require)
print(s1.reserve)
print(s2.reserve)
print(s3.reserve)

