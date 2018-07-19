#!/usr/bin/env python3


class Car(object):
    def __init__(self, reg, colour):
        self.registration = reg
        self.colour = colour

    def __str__(self):
        return 'Registration:{} Colour:{}'\
            .format(self.registration, self.colour)


if __name__ == '__main__':
    der = Car('WB-03-VY-1234', 'Chocolate')
    print(der)
