#!/usr/bin/env python3

import logging
import os
import sys
from constants import Constants
from file_command import FileCommand
from interactive_command import InteractiveCommand

LOGGER = logging.getLogger(__name__)


class CommandParser(object):
    def file_command(self, file_path):
        file_parser = FileCommand()
        file_parser.file_path = file_path
        data = \
            file_parser.execute_command()
        return data

    def interactive_command(self):
        os.system('clear')
        interactive_parser = InteractiveCommand()
        interactive_parser.execute_command()


def main(argv):
    obj = CommandParser()
    if len(argv) == 1:
        obj.file_command(argv[0])
    else:
        obj.interactive_command()


if __name__ == '__main__':
    main(sys.argv[1:2])
