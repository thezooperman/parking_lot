#!/usr/bin/env python3

import logging
import os
from parking_util import ParkingUtil

LOGGER = logging.getLogger(__name__)
PARKING_FULL = 'Sorry, parking lot is full'


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
        self.__output_messages = {
            'create_parking_lot': 'Created a parking lot with {} slots',
            'park': 'Allocated slot number: {}',
            'status': 'Slot No.{: <3}Registration No{: <5}Colour',
            'leave': 'Slot number {} is free'
        }

    def command_execute(self, file_path):
        data = None
        if not file_path or not os.path.exists(file_path) or\
                not os.path.isfile(file_path):
            LOGGER.error('Invalid file path')
            raise FileNotFoundError('Invalid file path')
        with open(file_path) as fs:
            data = fs.readlines()
        if data:
            try:
                util = ParkingUtil()
                for line in data:
                    if line:
                        splitted = line.split(' ')
                        command = splitted[0].strip().lower()
                        if command in self.__commands:
                            method, param = self.__commands[command]
                            params = list()
                            for i in range(1, param + 1):
                                tmp = splitted[i].replace('\n', '')
                                if tmp.isdigit():
                                    tmp = int(tmp)
                                params.append(tmp)
                            if command == 'create_parking_lot':
                                value = getattr(util, method)(*params)
                                print(
                                    self.__output_messages[command].
                                    format(*params))
                            elif command == 'park':
                                value = getattr(util, method)(*params)
                                if value == PARKING_FULL:
                                    print(PARKING_FULL)
                                else:
                                    print(self.__output_messages[command]
                                          .format(value))
                            elif command == 'leave':
                                getattr(util, method)(*params)
                                print(self.__output_messages[command]
                                      .format(*params))
                            elif command == 'status':
                                value = getattr(util, method)(*params)
                                print(self.__output_messages[command]
                                      .format('', '', ''))
                                str_format = '{: <10} {: <19} {}'
                                for parking in value:
                                    print(
                                        str_format.format(
                                            parking.parking_slot,
                                            parking.car.registration,
                                            parking.car.colour))
                            elif command == 'registration_numbers_for_cars_with_colour':
                                value = getattr(util, method)(*params)
                                print(*value, sep=', ')
                            elif command == 'slot_numbers_for_cars_with_colour':
                                value = getattr(util, method)(*params)
                                print(*value, sep=', ')
                            elif command == 'slot_number_for_registration_number':
                                value = getattr(util, method)(*params)
                                print(value, sep=', ')
                            else:
                                raise ValueError(
                                    'Invalid command passed: {}'
                                    .format(command))
            except Exception as ex:
                LOGGER.exception(str(ex), exc_info=True)
        else:
            LOGGER.error('File does not have valid data')
            raise ValueError('File does not have valid data')
        return data


if __name__ == '__main__':
    obj = CommandParser()
    obj.command_execute(
        r'/home/aritraghosh/Desktop/parking-lot-1.3.0/parking_lot/functional_spec/fixtures/file_input.txt')
