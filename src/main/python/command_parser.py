#!/usr/bin/env python3

import logging
import os

LOGGER = logging.getLogger(__name__)


class CommandParser(object):
    def __init__(self):
        self.__commands = {
            'create_parking_lot': ('init_slots', 1),
            'park': ('block', 2),
            'leave': ('release', 1),
            'status': ('get_parking_status', 0),
            'registration_numbers_for_cars_with_colour': ('get_registrations_by_colour', 1),
            'slot_numbers_for_cars_with_colour': ('get_slots_by_colour', 1),
            'slot_number_for_registration_number':
            ('get_slot_by_registration', 1)
        }

    def read_from_file(self, file_path):
        data = None
        if not file_path or not os.path.exists(file_path) or\
                not os.path.isfile(file_path):
            LOGGER.error('Invalid file path')
            raise FileNotFoundError('Invalid file path')
        with open(file_path, 'r', encoding='utf-8', errors='strict') as fs:
            data = fs.readlines()
        return data


if __name__ == '__main__':
    obj = CommandParser()
    obj.read_from_file(
        r'/home/aritraghosh/Desktop/parking-lot-1.3.0/parking_lot/functional_spec/fixtures/file_input.txt')
