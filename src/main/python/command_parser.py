#!/usr/bin/env python3

import logging
import os
import sys
from constants import Constants
from file_command_parser import FileCommandParser
from interactive_command_parser import InteractiveCommandParser

LOGGER = logging.getLogger(__name__)


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
        file_parser = FileCommandParser()
        file_parser.file_path = file_path
        data = \
            file_parser.execute_command(
                self.__commands, self.__output_messages)
        return data

    def interactive_command(self):
        os.system('clear')
        interactive_parser = InteractiveCommandParser()
        interactive_parser.execute_command(
            self.__commands, self.__output_messages)


def main(argv):
    obj = CommandParser()
    if len(argv) == 1:
        obj.file_command(argv[0])
    else:
        obj.interactive_command()


if __name__ == '__main__':
    main(sys.argv[1:2])
