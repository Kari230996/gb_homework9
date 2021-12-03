'''Второе задание'''

class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def formulation(self):
        road_mass = (self._length * self._width * 25 * 5) // 1000
        return road_mass


r = Road(20, 5000)
print(r.formulation(), 'т')

