#!/usr/bin/env python3

import pytest
from src.main.python.parking_util import ParkingUtil


class TestClass(object):
    def test_init_slots(self):
        p_util = ParkingUtil()
        p_util.init_slots(10)
        assert len(getattr(p_util, 'parkings')) == 10

    def test_invalid_init_slots(self):
        p_util = ParkingUtil()
        with pytest.raises(ValueError):
            p_util.init_slots(0)
            p_util.init_slots(-10)

    def test_is_parking_full(self):
        p_util = ParkingUtil()
        p_util.init_slots(5)
        assert not p_util.is_parking_full()
        p_util.init_slots(1)
        p_util.block('KA-01-WQ-2491', 'Orange')
        assert p_util.is_parking_full()
