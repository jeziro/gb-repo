class road:
    def __init__(self, _length, _width):
        self._length = _length
        self._width = _width


class Asph(road):
    def __init__(self, _length, _width, layer, mass=25):
        super().__init__(_length, _width)
        self.layer = layer
        print(f"Необходимое количество асфальта {(self._length * self._width * layer * mass) / 1000} тонн")


Asph(int(input("Введите длину в метрах")), int(input("Введите ширину в метрах")),
     int(input("Введите толщину полотна в сантиметрах")))
