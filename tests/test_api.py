# -*- coding:utf8 -*-
import unittest
from radikowave.api import RadikoApi, RadikoArea

__author__ = 'attakei'


class ApiTest(unittest.TestCase):
    def test_init_default_area(self):
        api = RadikoApi()
        self.assertEqual(api.area_id, RadikoArea.Tokyo)

    def test_init_specify_area(self):
        api = RadikoApi(RadikoArea.Chiba)
        self.assertEqual(api.area_id, RadikoArea.Chiba)
