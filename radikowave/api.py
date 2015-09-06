from enum import Enum


__author__ = 'attakei'


class RadikoArea(Enum):
    Chiba = 12
    Tokyo = 13


class RadikoApi(object):
    """Radiko API caller.
    """
    ENDPOINT = 'http://radiko.jp/v2'
    DEFAULT_AREA = RadikoArea.Tokyo

    def __init__(self, area_id=None):
        self.area_id = area_id if area_id is not None else self.DEFAULT_AREA
