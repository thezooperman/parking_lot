#!/usr/bin/env python3

class Vehicle(object):
    def __init__(self, vtype, reg, colour):
        self.vtype = vtype
        self.reg = reg
        self.colour = colour

    def __str__(self):
        return 'Registration:{} Colour:{}'.format(self.reg, self.colour)


class Car(Vehicle):
    def __init__(self, vtype, reg, colour):
        super().__init__(vtype, reg, colour)


if __name__ == '__main__':
    sup = Vehicle('Sedan', 'KA-04-MQ-2649', 'White')
    der = Car('SUV', 'WB-03-VY-1234', 'Chocolate')
    print(sup)
    print(der)

