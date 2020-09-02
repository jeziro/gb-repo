class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f'{self.name}  поехал'

    def stop(self):
        return f'{self.name}  остановился'

    def turn_right(self):
        return f'{self.name}  повернул направо'

    def turn_left(self):
        return f'{self.name}  повернул налево'

    def show_speed(self):
        return f'Скорость {self.name} в данный момент  - {self.speed}'


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Скорость {self.name} - {self.speed}')

        if self.speed > 40:
            return f'Скорость {self.name} превышает разрешенную для town car'
        else:
            return f'Скорость {self.name} в пределах ограничений для town car'


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Скорость work car {self.name} - {self.speed}')

        if self.speed > 60:
            return f'Скорость {self.name} превышает разрешенную для work car'
        else:
            return f'Скорость {self.name} в пределах ограничений для town car'

class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def police(self):
        if self.is_police:
            return f'{self.name} - полицейский автомобиль'
        else:
            return f'{self.name} - не полицейский автомобиль'


Mercedes = SportCar(150, 'Red', 'Mercedes', False)
Daewoo = TownCar(40, 'White', 'Daewoo', False)
Truck = WorkCar(80, 'White', 'Truck', False)
Ford = PoliceCar(110, 'Blue', 'Ford', True)
print(Truck.turn_left())
print(f'Когда {Daewoo.turn_right()}, then {Mercedes.stop()}')
print(f'{Truck.go()} и двигается со скоростью {Truck.show_speed()}')
print(f'{Truck.name} - {Truck.color}')
print(f'Is {Mercedes.name} полицейский авто? {Mercedes.is_police}')
print(f'Is {Truck.name}  полицейский авто? {Truck.is_police}')
print(Mercedes.show_speed())
print(Daewoo.show_speed())
print(Ford.police())
print(Ford.show_speed())
