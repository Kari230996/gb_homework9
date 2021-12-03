'''Пятое задание'''

class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')

class Pen(Stationery):
    def draw(self):
        print('Ручка. Воплощение совершенства.')


class Pencil(Stationery):
    def draw(self):
        print('Карандаш. Качество определяет стиль.')

class Handle(Stationery):
    def draw(self):
        print('Маркер. Хочешь?')

pen = Pen('Ручка')
pencil = Pencil('Карандаш')
handle = Handle('Маркер')

pen.draw()
pencil.draw()
handle.draw()



