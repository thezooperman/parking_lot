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
            Car(registration, colour), empty_slot + 1)
        self.__slot_counter += 1

    def release(self, slot):
        if slot <= 0 and slot > len(self.parkings):
            LOGGER.error('Slot does not exist')
            raise ValueError('Slot does not exist')
        flagFound = False
        for idx, parked in enumerate(self.parkings):
            if isinstance(parked, Parking)\
                    and parked.parking_slot == slot:
                flagFound = True
                break
        if flagFound:
            self.parkings[idx] = 0
            self.__slot_counter -= 1
        else:
            LOGGER.error('Slot does not exist')
            raise ValueError('Slot does not exist')

    def get_registrations_by_colour(self, colour):
        for c in self.parkings:
            if isinstance(c.car, Car) and \
                    c.car.colour.lower() == colour.lower():
                yield c.car.registration

    def get_slot_by_registration(self, registration):
        for parking in self.parkings:
            if parking.car.registration.lower() == registration.lower():
                return parking.parking_slot

    def get_slots_by_colour(self, colour):
        for parking in self.parkings:
            if parking.car.colour.lower() ==\
                    colour.lower():
                yield parking.parking_slot


if __name__ == '__main__':
    obj = ParkingUtil()
    obj.init_slots(1)
    obj.block('abcd', 'white')
    obj.block('efgh', 'red')
    obj.release(1)
