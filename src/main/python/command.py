#!/usr/bin/env python3

from constants import COMMANDS


class Command:
    def __init__(self):
        self._persist_methods = [x for x in COMMANDS.keys()]

    def dynamic_invoke(self, receiver, attribute, args):
        if attribute in self._persist_methods:
            name = COMMANDS[attribute][0]
            action = getattr(receiver, name)
            return action(*args)
