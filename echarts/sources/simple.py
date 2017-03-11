from __future__ import absolute_import, unicode_literals

from .base import BaseDataSource


class SimpleDataSource(BaseDataSource):
    def as_rows(self):
        return [row for row in self.data]
