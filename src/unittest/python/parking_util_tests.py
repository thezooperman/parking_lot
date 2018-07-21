#!/usr/bin/env python3

import unittest
from parking_util import ParkingUtil, NOT_FOUND


class TestClass(unittest.TestCase):
    def test_init_slots(self):
        p_util = ParkingUtil()
        p_util.init_slots(10)
        self.assertTrue(len(p_util.parkings) == 10)

    def test_invalid_init_slots(self):
        p_util = ParkingUtil()
        with self.assertRaises(ValueError):
            p_util.init_slots(0)
            p_util.init_slots(-10)

    def test_is_parking_full(self):
        p_util = ParkingUtil()
        p_util.init_slots(5)
        self.assertFalse(p_util.is_parking_full())
        p_util.init_slots(1)
        p_util.block('KA-01-WQ-2491', 'Orange')
        self.assertTrue(p_util.is_parking_full())

    def test_block_one(self):
        p_util = ParkingUtil()
        p_util.init_slots(1)
        p_util.block('KA-01-AB-1234', 'Magenta')
        self.assertTrue(len(p_util.parkings) == 1)
        self.assertEqual(p_util.parkings[0].car.colour, 'Magenta')
        self.assertEqual(p_util.parkings[0].car.registration, 'KA-01-AB-1234')
        self.assertTrue(p_util.is_parking_full())

    def test_release_one(self):
        p_util = ParkingUtil()
        p_util.init_slots(2)
        p_util.block('KA-01-AB-1234', 'Red')
        p_util.block('KA-02-cd-5678', 'Green')
        self.assertEqual(len(p_util.parkings), 2)
        p_util.release(1)

    def test_release_negative_index(self):
        p_util = ParkingUtil()
        p_util.init_slots(1)
        p_util.block('KA-01-AB-1234', 'Red')
        with self.assertRaises(ValueError):
            p_util.release(-2)

    def test_release_out_of_bound_index(self):
        p_util = ParkingUtil()
        p_util.init_slots(1)
        p_util.block('KA-01-AB-1234', 'Red')
        with self.assertRaises(ValueError):
            p_util.release(12)

    def test_get_regs_by_colour(self):
        p_util = ParkingUtil()
        p_util.init_slots(3)
        p_util.block('KA-01-AB-1234', 'Red')
        p_util.block('KA-02-cd-5678', 'Green')
        p_util.block('KA-01-AB-9012', 'Red')
        regs = p_util.get_registrations_by_colour('Red')
        self.assertTrue(regs[0] == 'KA-01-AB-1234')
        self.assertTrue(regs[1] == 'KA-01-AB-9012')

    def test_get_regs_by_colour_not_found(self):
        p_util = ParkingUtil()
        p_util.init_slots(3)
        p_util.block('KA-01-AB-1234', 'Red')
        self.assertTrue(p_util.get_registrations_by_colour(
            'White') == [])

    def test_get_slots_by_colour_not_found(self):
        p_util = ParkingUtil()
        self.assertTrue(p_util.get_slots_by_colour(
            'red') == [])

    def test_get_slot_by_reg(self):
        p_util = ParkingUtil()
        p_util.init_slots(3)
        p_util.block('KA-01-AB-1234', 'Red')
        p_util.block('KA-02-cd-5678', 'Green')
        p_util.block('KA-01-AB-9012', 'Red')
        self.assertTrue(p_util.get_slot_by_registration('KA-02-cd-5678') == 2)

    def test_get_slots_by_colour(self):
        p_util = ParkingUtil()
        p_util.init_slots(3)
        p_util.block('KA-01-AB-1234', 'Red')
        p_util.block('KA-02-CD-5678', 'Green')
        p_util.block('KA-01-AB-9012', 'Red')
        p_util.block('KA-02-CD-9012', 'Green')
        obj = p_util.get_slots_by_colour('red')
        self.assertEqual(obj[0], 1)
        self.assertEqual(obj[1], 3)
        obj = p_util.get_slots_by_colour('green')
        self.assertEqual(obj[0], 2)

    def test_get_parking_status(self):
        p_util = ParkingUtil()
        p_util.init_slots(4)
        p_util.block('KA-01-AB-1234', 'Red')
        p_util.block('KA-02-CD-5678', 'Green')
        p_util.block('KA-01-AB-9012', 'Red')
        p_util.block('KA-02-CD-9012', 'Green')
        self.assertTrue(len(p_util.get_parking_status()) == 4)
        p_util = ParkingUtil()
        self.assertTrue(len(p_util.get_parking_status()) == 0)
