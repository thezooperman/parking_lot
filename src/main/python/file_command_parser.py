#!/usr/bin/env python3

import logging
import os

from constants import Constants
from parking_util import ParkingUtil

LOGGER = logging.getLogger(__name__)


class FileCommandParser(object):
    def __init__(self):
        self.__file_path = ''

    @property
    def file_path(self):
        return self.__file_path

    @file_path.setter
    def file_path(self, value):
        if not value or not os.path.exists(value) or\
                not os.path.isfile(value):
            LOGGER.error('Invalid file path')
            raise FileNotFoundError('Invalid file path')
        self.__file_path = value

    def execute_command(self, commands, output_messages):
        data = None
        with open(self.file_path, encoding='utf-8')\
                as input_file:
            data = input_file.readlines()

        if data:
            try:
                util = ParkingUtil()
                for line in data:
                    if line:
                        splitted = line.split(' ')
                        command = splitted[0].strip().lower()
                        if command in commands:
                            method, param = commands[command]
                            params = list()
                            for i in range(1, param + 1):
                                tmp = splitted[i].replace('\n', '')
                                if tmp.isdigit():
                                    tmp = int(tmp)
                                params.append(tmp)
                            if command == Constants.CREATE_PARKING_LOT:
                                getattr(util, method)(*params)
                                print(
                                    output_messages[command].
                                    format(*params))
                            elif command == Constants.PARK:
                                value = getattr(util, method)(*params)
                                if value == Constants.PARKING_FULL:
                                    print(Constants.PARKING_FULL)
                                else:
                                    print(output_messages[command]
                                          .format(value))
                            elif command == Constants.LEAVE:
                                getattr(util, method)(*params)
                                print(output_messages[command]
                                      .format(*params))
                            elif command == Constants.STATUS:
                                value = getattr(util, method)(*params)
                                print(output_messages[command]
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
