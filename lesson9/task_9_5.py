__author__ = 'Рейтер Валерия Борисовна'

# 5. Реализовать класс Stationery (канцелярская принадлежность).
# Техническое задание:
#
# атрибут title (название)
# метод draw (отрисовка). Метод выводит сообщение «Запуск отрисовки»;
# создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
# в каждом классе реализовать переопределение метода draw. Для каждого класса метод должен выводить уникальное
# сообщение;
# Подумайте о том, имеет ли смысл при переопределении draw использовать draw базового класса.
# создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.


class Stationery:

    def __init__(self, title):
        self.title = title

    def draw(self):
        return f"Запуск отрисовки"


class Pen(Stationery):
    def __init__(self):
        super().__init__("Ручка")

    def draw(self):
        return f"Запуск отрисовки с помощью: Синяя {self.title}"


class Pencil(Stationery):
    def __init__(self):
        super().__init__("Карандаш")

    def draw(self):
        return f"Запуск отрисовки с помощью: Красный {self.title}"


class Handle(Stationery):
    def __init__(self):
        super().__init__("Маркер")

    def draw(self):
        return f"Запуск отрисовки с помощью: Черный {self.title}"


pen1 = Pen()
print(pen1.draw())

penсil1 = Pencil()
print(penсil1.draw())
