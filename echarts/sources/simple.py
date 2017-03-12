from __future__ import absolute_import, unicode_literals

from .base import BaseDataSource


class SimpleDataSource(BaseDataSource):
    def as_table(self):
        return [row for row in self.data]
