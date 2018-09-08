#!/usr/bin/env python3

import logging

from constants import OUTPUT_MESSAGES, Constants
from parking import Parking
from vehicle import Car

LOGGER = logging.getLogger(__name__)


class ParkingLot:
    def __init__(self):
        self.__max_slots = 10
        self.parkings = []
        self.__slot_counter = 0

    def init_slots(self, number_of_slots):
        if number_of_slots <= 0:
            LOGGER.error('Number of slots must be integer and positive')
            raise ValueError('Number of slots must be integer and positive')
        self.__max_slots = number_of_slots
        self.parkings = [0] * number_of_slots
        print(OUTPUT_MESSAGES[Constants.CREATE_PARKING_LOT].format(
            number_of_slots))

    def is_parking_full(self):
        return self.__slot_counter >= self.__max_slots

    def block(self, registration, colour):
        if self.is_parking_full():
            print(Constants.PARKING_FULL)
            return
        # Find first empty slot
        empty_slot = self.parkings.index(0)
        self.parkings[empty_slot] = Parking(
            Car(registration, colour), empty_slot + 1)
        self.__slot_counter += 1
        print(OUTPUT_MESSAGES[Constants.PARK].format(empty_slot + 1))

    def release(self, slot):
        if slot <= 0 and slot > len(self.parkings):
            LOGGER.error('Slot does not exist')
            raise ValueError('Slot does not exist')
        flag_found = False
        for idx, parked in enumerate(self.parkings):
            if isinstance(parked, Parking)\
                    and parked.parking_slot == slot:
                flag_found = True
                break
        if flag_found:
            self.parkings[idx] = 0
            self.__slot_counter -= 1
            print(OUTPUT_MESSAGES[Constants.LEAVE].format(slot))
        else:
            LOGGER.error('Slot does not exist')
            raise ValueError('Slot does not exist')

    def get_registrations_by_colour(self, colour):
        if not colour:
            print(Constants.NOT_FOUND)
            return
        for parking in self.parkings:
            if isinstance(parking, Parking) and\
                    parking.car.colour.lower() == colour.lower():
                print(parking.car.registration, sep=' ', end=' ')
        print(flush=True)

    def get_slot_by_registration(self, registration):
        if not registration:
            print(Constants.NOT_FOUND)
            return
        for parking in self.parkings:
            if parking.car.registration.lower() == registration.lower():
                print(parking.parking_slot, sep=' ', end=' ')
                print(flush=True)
                return
        print(Constants.NOT_FOUND)

    def get_slots_by_colour(self, colour):
        if not colour:
            print(Constants.NOT_FOUND)
            return
        for parking in self.parkings:
            if isinstance(parking, Parking) and\
                    parking.car.colour.lower() == colour.lower():
                print(parking.parking_slot, sep=' ', end=' ')
        print(flush=True)

    def get_parking_status(self):
        str_format = '{: <10} {: <19} {}'
        for parking in self.parkings:
            if isinstance(parking, Parking):
                print(
                    str_format.format(
                        parking.parking_slot,
                        parking.car.registration,
                        parking.car.colour))
