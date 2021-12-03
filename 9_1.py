'''Первое задание'''
from time import sleep

class TrafficLight:

    def __init__(self):
        self.__color = ['red', 'yellow', 'green']

    def running(self):

        i = 0
        while True:
            print(self.__color[i])
            if i == 0:
                sleep(7)
            if i == 1:
                sleep(2)
            if i == 2:
                sleep(4)

            i += 1

            if i == 3: # повторяем последовательность
                i -= 3

traffic = TrafficLight()
print(traffic.running())

