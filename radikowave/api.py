from enum import Enum


__author__ = 'attakei'


class _RadikoArea(Enum):
    """Behavior extension for RadikoArea.
    """
    def get_id(self):
        return 'JP{}'.format(self.value)

    @property
    def area_id(self):
        return self.get_id()


class RadikoArea(_RadikoArea):
    """Radiko Area id enumerations.

    Names is based from http://jprs.jp/about/jp-dom/prefecture.html#labels
    """
    Hokkaido = 1
    Aomori = 2
    Iwate = 3
    Miyagi = 4
    Akita = 5
    Yamagata = 6
    Fukushima = 7
    Ibaraki = 8
    Tochigi = 9
    Gunma = 10
    Saitama = 11
    Chiba = 12
    Tokyo = 13
    Kanagawa = 14
    Niigata = 15
    Yamanashi = 16
    Nagano = 17
    Ishikawa = 18
    Toyama = 19
    Fukui = 20
    Aichi = 21
    Gifu = 22
    Shizuoka = 23
    Mie = 24
    Osaka = 25
    Hyogo = 26
    Kyoto = 27
    Shiga = 28
    Nara = 29
    Wakayama = 30
    Okayama = 31
    Hiroshima = 32
    Tottori = 33
    Shimane = 34
    Yamaguchi = 35
    Kagawa = 36
    Tokushima = 37
    Ehime = 38
    Kochi = 39
    Fukuoka = 40
    Saga = 41
    Nagasaki = 42
    Kumamoto = 43
    Oita = 44
    Miyazaki = 45
    Kagoshima = 46
    Okinawa = 47


class RadikoApi(object):
    """Radiko API caller.
    """
    ENDPOINT = 'http://radiko.jp/v2'
    DEFAULT_AREA = RadikoArea.Tokyo

    def __init__(self, area=None):
        self.area = area if area is not None else self.DEFAULT_AREA
