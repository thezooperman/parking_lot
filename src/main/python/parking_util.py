#!/usr/bin/env python3
from vehicle import Car
from parking import Parking
import errno
import logging


logger = logging.getLogger(__name__)


class ParkingUtil(object):
    def __init__(self):
        self.__max_slots = None
        self.__cars = None

    def init_slots(self, number_of_slots):
        if number_of_slots <= 0:
            logger.error('Number of slots must be integer and positive')
            raise ValueError(errno.ENOENT)
        self.__max_slots = number_of_slots
        self.__cars = [0] * number_of_slots

    def is_parking_full(self):
        return self.__max_slots <= 0

    def block(self, registration, colour):
        if self.is_parking_full():
            return ''
        # Find first empty slot
        empty_slot = self.__cars.index(0)
        self.__cars[empty_slot] = Parking(
            Car(registration, colour), empty_slot)
        self.__max_slots -= 1

    def release(self, slot):
        if slot <= 0 and slot > len(self.__cars):
            return ''
        self.__cars[slot - 1] = 0
        self.__max_slots += 1

    def get_registration_by_colour(self, colour):
        # for c in self.__cars:
        #     if c is Car and c.colour == colour:
        #         yield c.colour
        return [c.registration for c in self.__cars if c is isinstance(Car)
                and c.colour.lower() == colour.lower()]

    def get_slot_by_registration(self, registration):
        pass

    def get_slots_by_registration(self, registration):
        pass
