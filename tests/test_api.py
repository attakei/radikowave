# -*- coding:utf8 -*-
import unittest
from radikowave.api import RadikoApi, RadikoArea, RadikoStation

__author__ = 'attakei'


class AreaTest(unittest.TestCase):
    def test_get_id(self):
        self.assertEqual(RadikoArea.Hokkaido.get_id(), 'JP1')
        self.assertEqual(RadikoArea.Okinawa.get_id(), 'JP47')

    def test_as_property(self):
        self.assertEqual(RadikoArea.Hokkaido.area_id, 'JP1')


class StationTest(unittest.TestCase):
    def test_from_dom(self):
        dom_base = """<station>
    <id>HBC</id>
    <name>ＨＢＣラジオ</name>
    <ascii_name>HBC RADIO</ascii_name>
    <href>http://www.hbc.co.jp/radio/index.html</href>
    <logo_xsmall>http://radiko.jp/station/logo/HBC/logo_xsmall.png</logo_xsmall>
    <logo_small>http://radiko.jp/station/logo/HBC/logo_small.png</logo_small>
    <logo_medium>http://radiko.jp/station/logo/HBC/logo_medium.png</logo_medium>
    <logo_large>http://radiko.jp/station/logo/HBC/logo_large.png</logo_large>
<logo width="124" height="40">http://radiko.jp/v2/static/station/logo/HBC/124x40.png</logo>
<logo width="344" height="80">http://radiko.jp/v2/static/station/logo/HBC/344x80.png</logo>
<logo width="688" height="160">http://radiko.jp/v2/static/station/logo/HBC/688x160.png</logo>
<logo width="172" height="40">http://radiko.jp/v2/static/station/logo/HBC/172x40.png</logo>
<logo width="224" height="100">http://radiko.jp/v2/static/station/logo/HBC/224x100.png</logo>
<logo width="448" height="200">http://radiko.jp/v2/static/station/logo/HBC/448x200.png</logo>
<logo width="112" height="50">http://radiko.jp/v2/static/station/logo/HBC/112x50.png</logo>
<logo width="168" height="75">http://radiko.jp/v2/static/station/logo/HBC/168x75.png</logo>
<logo width="258" height="60">http://radiko.jp/v2/static/station/logo/HBC/258x60.png</logo>
<feed>http://radiko.jp/station/feed/HBC.xml</feed>
<banner>http://radiko.jp/res/banner/HBC/20110922161828.png</banner>
</station>"""
        import xml.etree.ElementTree as ET
        stations_root = ET.fromstring(dom_base)
        station = RadikoStation.from_dom(stations_root)
        self.assertIsInstance(station, RadikoStation)
        self.assertEqual(station.id, 'HBC')
        self.assertEqual(station.name, 'ＨＢＣラジオ')


class ApiTest(unittest.TestCase):
    def test_init_default_area(self):
        api = RadikoApi()
        self.assertEqual(api.area, RadikoArea.Tokyo)

    def test_init_specify_area(self):
        api = RadikoApi(RadikoArea.Chiba)
        self.assertEqual(api.area, RadikoArea.Chiba)

    def test_featch_stations(self):
        api = RadikoApi(RadikoArea.Hokkaido)
        stations = api.fetch_stations()
        self.assertIsInstance(stations, list)
        self.assertEqual(len(stations), 7)
        for station in stations:
            self.assertIsInstance(station, RadikoStation)
