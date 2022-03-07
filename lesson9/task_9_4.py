__author__ = 'Рейтер Валерия Борисовна'

# 4. Реализуйте класс Car (машина).
# Техническое задание:
#
# атрибуты: speed, color, name, is_police(булево). speed - текущая скорость машины.
# методы: go, stop, turn(direction), которые должны сообщать(выводить на экран), что машина поехала, остановилась,
# повернула (куда). turn(direction) - метод, принимающий параметр: направление поворота.
# опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar
# добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля
# для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar)
# должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат. Вызовите
# методы и покажите результат.


class Car:

    def __init__(self, speed, color, name, car_type="Car", is_police="False"):
        self.speed = speed
        self.color = color
        self.name = name
        self.car_type = car_type
        self.is_police = is_police

    def car_go(self):
        return f"Машина движется"

    def car_stop(self):
        return f"Машина остановилась"

    def car_turn(self, direction):
        return f"Машина повернула {direction}"

    def show_speed(self):
        return f"Текущая скорость автомобиля {self.speed} км/ч"


class TownCar(Car):
    def __init__(self, speed, color, name, speed_limit):
        self.speed_limit = speed_limit
        super().__init__(speed, color, name, "town")

    def show_speed(self):
        if self.speed > self.speed_limit:
            result = f"Превыщение скорости! {self.speed} км/ч"
        else:
            result = f"Текущая скорость автомобиля {self.speed} км/ч"
        return result


class SportCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, "sport")


class WorkCar(Car):
    def __init__(self, speed, color, name, speed_limit):
        self.speed_limit = speed_limit
        super().__init__(speed, color, name, "work")

    def show_speed(self):
        if self.speed > self.speed_limit:
            result = f"Превыщение скорости! {self.speed}"
        else:
            result = f"Текущая скорость автомобиля {self.speed} км/ч"
        return result


class PoliceCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, "Car", "True")


car_a = Car(speed=60, color="green", name="Toyota")
print(f"Машина класса Car: {car_a.show_speed()}")

car_town = TownCar(speed=80, color="blue", name="BMW", speed_limit=60)
print(f"Машина класса TownCar: {car_town.show_speed()}")

car_police = PoliceCar(speed=100, color="white", name="Lada")
print(f"Машина класса PoliceCar: {car_police.show_speed()}")

