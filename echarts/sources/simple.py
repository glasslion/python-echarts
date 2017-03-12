from __future__ import absolute_import, unicode_literals

from ..utils import transpose
from .base import BaseDataSource


class SimpleDataSource(BaseDataSource):
    def __init__(self, rows=None, series=None):
        checks = [rows is None, series is None]
        if all(checks) or not any(checks):
            raise ValueError("The `rows` and `series` parameters are incompatible.")

        if rows is not None:
            self.data = rows
        elif series is not None:
            self.data = transpose(series)
