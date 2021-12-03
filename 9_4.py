'''Четвертое задание'''
class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f'The {self.name} went'

    def stop(self):
        return f'The {self.name} stopped'

    def turn(self, direction):
        return f'The {self.name} turned to the {direction} side'

    def show_speed(self):
        return f'Your current speed: {self.speed}'

class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            return 'Speed exceeded'

class SportCar(Car):
    pass

class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            return 'Speed exceeded'

class PoliceCar(Car):
    pass


town_car = TownCar(70, 'silver', 'BMW', False)
sport_car = SportCar(180, 'red', 'Ferrari', False)
work_car = WorkCar(60, 'brown', 'Mitsubishi', False)
police_car = PoliceCar(140, 'blue-white', 'Mercedez', True)

print(town_car.show_speed())
print(sport_car.turn('right'))
print(work_car.show_speed())
print(police_car.show_speed())






