# -*- coding:utf8 -*-
import unittest
from radikowave.api import RadikoApi, RadikoArea

__author__ = 'attakei'


class AreaTest(unittest.TestCase):
    def test_get_id(self):
        self.assertEqual(RadikoArea.Hokkaido.get_id(), 'JP1')
        self.assertEqual(RadikoArea.Okinawa.get_id(), 'JP47')

    def test_as_property(self):
        self.assertEqual(RadikoArea.Hokkaido.area_id, 'JP1')


class ApiTest(unittest.TestCase):
    def test_init_default_area(self):
        api = RadikoApi()
        self.assertEqual(api.area, RadikoArea.Tokyo)

    def test_init_specify_area(self):
        api = RadikoApi(RadikoArea.Chiba)
        self.assertEqual(api.area, RadikoArea.Chiba)
