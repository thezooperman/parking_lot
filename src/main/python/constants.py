#!/usr/bin/env python3


class Constants(object):
    CREATE_PARKING_LOT = 'create_parking_lot'
    PARK = 'park'
    LEAVE = 'leave'
    STATUS = 'status'
    REGISTRATION_NUMBERS_FOR_CARS_WITH_COLOUR = 'registration_numbers_for_cars_with_colour'
    GET_REGISTRATIONS_BY_COLOUR = 'get_registrations_by_colour'
    SLOT_NUMBERS_FOR_CARS_WITH_COLOUR = 'slot_numbers_for_cars_with_colour'
    SLOT_NUMBER_FOR_REGISTRATION_NUMBER = 'slot_number_for_registration_number'
    PARKING_FULL = 'Sorry, parking lot is full'
    NOT_FOUND = 'Not Found'

COMMANDS = {
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

OUTPUT_MESSAGES = {
    Constants.CREATE_PARKING_LOT: 'Created a parking lot with {} slots',
    Constants.PARK: 'Allocated slot number: {}',
    Constants.STATUS: 'Slot No.{: <3}Registration No{: <5}Colour',
    Constants.LEAVE: 'Slot number {} is free'
}
