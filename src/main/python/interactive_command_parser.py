#!/usr/bin/env python3
import logging
import sys

from constants import Constants
from parking_util import ParkingUtil

LOGGER = logging.getLogger(__name__)


class InteractiveCommandParser(object):
    def __init__(self):
        self.__util = ParkingUtil()

    def __exec_choice(self, choice, commands, output_messages):
        choice = choice.strip()
        if choice == "exit":
            sys.exit(0)
        splitted = choice.split(' ')
        command = splitted[0].lower()
        method, param = commands[command]
        if command in commands:
            params = list()
            for i in range(1, param + 1):
                tmp = splitted[i].replace('\n', '')
                if tmp.isdigit():
                    tmp = int(tmp)
                params.append(tmp)
            if command == Constants.CREATE_PARKING_LOT:
                getattr(self.__util, method)(*params)
                print(
                    output_messages[command].
                    format(*params))
            elif command == Constants.PARK:
                value = getattr(self.__util, method)(*params)
                if value == Constants.PARKING_FULL:
                    print(Constants.PARKING_FULL)
                else:
                    print(output_messages[command]
                          .format(value))
            elif command == Constants.LEAVE:
                getattr(self.__util, method)(*params)
                print(output_messages[command]
                      .format(*params))
            elif command == Constants.STATUS:
                value = getattr(self.__util, method)(*params)
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
                value = getattr(self.__util, method)(*params)
                print(*value, sep=', ')
            elif command == Constants.SLOT_NUMBERS_FOR_CARS_WITH_COLOUR:
                value = getattr(self.__util, method)(*params)
                print(*value, sep=', ')
            elif command == Constants.SLOT_NUMBER_FOR_REGISTRATION_NUMBER:
                value = getattr(self.__util, method)(*params)
                print(value, sep=', ')

    def __init_menu(self, commands, output_messages):
        while True:
            choice = input()
            self.__exec_choice(choice, commands, output_messages)

    def execute_command(self, commands, output_messages):
        self.__init_menu(commands, output_messages)
