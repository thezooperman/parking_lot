#!/usr/bin/env python3

import os
import logging
from command import Command
from parking_lot import ParkingLot
from constants import COMMANDS, OUTPUT_MESSAGES

LOGGER = logging.getLogger(__name__)


class InteractiveCommand:
    def execute_command(self):
        self.__init_menu()

    def __init_menu(self):
        cmd = Command()
        receiver = ParkingLot()
        while True:
            choice = input()
            self.__exec_choice(choice, cmd, receiver)

    def __exec_choice(self, choice, cmd, receiver):
        choice = choice.strip()
        if choice == "exit":
            sys.exit(0)
        splitted = choice.split(' ')
        command = splitted[0].lower()
        method, param = COMMANDS[command]
        if command in COMMANDS:
            params = list()
            for i in range(1, param + 1):
                tmp = splitted[i].replace('\n', '')
                if tmp.isdigit():
                    tmp = int(tmp)
                params.append(tmp)
            cmd.dynamic_invoke(receiver, command, params)
        else:
            print('Not a valid command')
