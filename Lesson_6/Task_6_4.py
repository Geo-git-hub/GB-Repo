"""
Реализуйте базовый класс Car.
У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать,
что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
Добавьте в базовый класс метод show_speed,
который должен показывать текущую скорость автомобиля.
Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar)
должно выводиться сообщение о превышении скорости.
"""


class Car:
    def __init__(self, name, color, speed, is_police):
        self.name = name
        self.speed = speed
        self.color = color
        self.is_police = is_police

    def go(self):
        print(f'Car {self.name} went')

    def stop(self):
        print(f'Car {self.name} stopped')

    def turn(self, direction):
        print(f'Car {self.name} changed direction to {direction}')

    def show_speed(self, speed):
        print(f'{self.name} speed is {speed}')

    def __str__(self):
        return f'{self.name} have parameters: color = {self.color}, max speed = {self.speed}' \
               f' {" and is police car" if self.is_police else " and is not police car"}'


class TownCar(Car):
    def __init__(self, name, color, speed, is_police=False):
        super().__init__(name, color, speed, is_police)

    def show_speed(self, speed):
        speed_limit = 60
        if speed > speed_limit:
            print(f'attention you exceeded the speed {speed}, slow down to {speed_limit}')
        else:
            print(f'{self.name} speed is {speed}')


class SportCar(Car):
    def __init__(self, name, color, speed, is_police=False):
        super().__init__(name, color, speed, is_police)


class WorkCar(Car):
    def __init__(self, name, color, speed, is_police=False):
        super().__init__(name, color, speed, is_police)

    def show_speed(self, speed):
        speed_limit = 40
        if speed > speed_limit:
            print(f'attention you exceeded the speed {speed}, slow down to {speed_limit}')
        else:
            print(f'{self.name} speed is {speed}')


class PoliceCar(Car):
    def __init__(self, name, color, speed, is_police=True):
        super().__init__(name, color, speed, is_police)


print('===================================================================')
town_car = TownCar('Peugeot 208', 'red', 180)
print(town_car)
print(town_car.name)
town_car.go()
town_car.show_speed(40)
town_car.turn('right')
print('===================================================================')

sport_car = SportCar('Ferrari', 'black', 400)
sport_car.stop()
sport_car.turn('left')
print('===================================================================')

work_car = WorkCar('Kia', 'white', 180)
print(work_car)
work_car.show_speed(60)
print('===================================================================')

police_car = PoliceCar('Ford', 'pink', 250)
print(police_car)
police_car.turn('left')
print('===================================================================')
