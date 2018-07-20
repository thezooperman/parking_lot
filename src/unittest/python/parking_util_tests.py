#!/usr/bin/env python3

import unittest
from parking_util import ParkingUtil


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
