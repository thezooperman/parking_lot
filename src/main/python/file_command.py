#p1.py

import os, logging
from command import Command
from parking_lot import ParkingLot
from constants import COMMANDS, OUTPUT_MESSAGES

LOGGER = logging.getLogger(__name__)

class FileCommand(object):
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

    def execute_command(self):
        cmd = Command()
        receiver = ParkingLot()
        data = None
        with open(self.file_path, encoding='utf-8') as input_file:
            data = input_file.readlines()
        if data:
            try:
                for line in data:
                    splitted = line.split(' ')
                    command = splitted[0].strip().lower()
                    if command in COMMANDS:
                        method, param = COMMANDS[command]
                        params = list()
                        for i in range(1, param + 1):
                            tmp = splitted[i].replace('\n', '')
                            if tmp.isdigit():
                                tmp = int(tmp)
                            params.append(tmp)
                        cmd.dynamic_invoke(receiver, command, params)
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
