#!/usr/bin/env python3
import logging

from parking import Parking
from vehicle import Car

LOGGER = logging.getLogger(__name__)


class ParkingUtil(object):
    def __init__(self):
        self.__max_slots = None
        self.parkings = []
        self.__slot_counter = 0

    def init_slots(self, number_of_slots):
        if number_of_slots <= 0:
            LOGGER.error('Number of slots must be integer and positive')
            raise ValueError('Number of slots must be integer and positive')
        self.__max_slots = number_of_slots
        self.parkings = [0] * number_of_slots

    def is_parking_full(self):
        return self.__slot_counter >= self.__max_slots

    def block(self, registration, colour):
        if self.is_parking_full():
            return 'No slot available'
        # Find first empty slot
        empty_slot = self.parkings.index(0)
        self.parkings[empty_slot] = Parking(
            Car(registration, colour), empty_slot)
        self.__slot_counter += 1

    def release(self, slot):
        if slot <= 0 and slot > len(self.parkings):
            return ''
        self.parkings[slot - 1] = 0
        self.__slot_counter -= 1

    def get_registration_by_colour(self, colour):
        return [c.car.registration for c in self.parkings
                if c.car is isinstance(Car)
                and c.car.colour.lower() == colour.lower()]

    def get_slot_by_registration(self, registration):
        for parking in self.parkings:
            if parking.car.registration.lower() == registration.lower():
                return parking.parking_slot

    def get_slots_by_registration(self, registration):
        for parking in self.parkings:
            if parking.car.registration.lower() ==\
                    registration.lower():
                yield parking.parking_slot


if __name__ == '__main__':
    obj = ParkingUtil()
    obj.init_slots(1)
    obj.block('abcd', 'white')
