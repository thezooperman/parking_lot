#!/usr/bin/env python3

import logging
import os
import sys
from parking_util import ParkingUtil
from constants import Constants

LOGGER = logging.getLogger(__name__)
PARKING_FULL = 'Sorry, parking lot is full'


class CommandParser(object):
    def __init__(self):
        self.__commands = {
            Constants.CREATE_PARKING_LOT: ('init_slots', 1),
            Constants.PARK: ('block', 2),
            Constants.LEAVE: ('release', 1),
            Constants.STATUS: ('get_parking_status', 0),
            Constants.REGISTRATION_NUMBERS_FOR_CARS_WITH_COLOUR: ('get_registrations_by_colour', 1),
            Constants.SLOT_NUMBERS_FOR_CARS_WITH_COLOUR:
            ('get_slots_by_colour', 1),
            Constants.SLOT_NUMBER_FOR_REGISTRATION_NUMBER:
            ('get_slot_by_registration', 1)
        }
        self.__output_messages = {
            Constants.CREATE_PARKING_LOT: 'Created a parking lot with {} slots',
            Constants.PARK: 'Allocated slot number: {}',
            Constants.STATUS: 'Slot No.{: <3}Registration No{: <5}Colour',
            Constants.LEAVE: 'Slot number {} is free'
        }

    def file_command(self, file_path):
        data = None
        if not file_path or not os.path.exists(file_path) or\
                not os.path.isfile(file_path):
            LOGGER.error('Invalid file path')
            raise FileNotFoundError('Invalid file path')
        with open(file_path) as input_file:
            data = input_file.readlines()
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
                            if command == Constants.CREATE_PARKING_LOT:
                                value = getattr(util, method)(*params)
                                print(
                                    self.__output_messages[command].
                                    format(*params))
                            elif command == Constants.PARK:
                                value = getattr(util, method)(*params)
                                if value == PARKING_FULL:
                                    print(PARKING_FULL)
                                else:
                                    print(self.__output_messages[command]
                                          .format(value))
                            elif command == Constants.LEAVE:
                                getattr(util, method)(*params)
                                print(self.__output_messages[command]
                                      .format(*params))
                            elif command == Constants.STATUS:
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
                            elif command == Constants.REGISTRATION_NUMBERS_FOR_CARS_WITH_COLOUR:
                                value = getattr(util, method)(*params)
                                print(*value, sep=', ')
                            elif command == Constants.SLOT_NUMBERS_FOR_CARS_WITH_COLOUR:
                                value = getattr(util, method)(*params)
                                print(*value, sep=', ')
                            elif command == Constants.SLOT_NUMBER_FOR_REGISTRATION_NUMBER:
                                value = getattr(util, method)(*params)
                                print(value, sep=', ')
                            else:
                                raise ValueError(
                                    'Invalid command: {}'
                                    .format(command))
            except Exception as ex:
                LOGGER.exception(str(ex), exc_info=True)
        else:
            LOGGER.error('File does not have valid data')
            raise ValueError('File does not have valid data')
        return data


def main(argv):
    if len(argv) == 1:
        obj = CommandParser()
        obj.file_command(*argv)


if __name__ == '__main__':
    main(sys.argv[1:2])
