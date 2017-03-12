from __future__ import absolute_import, unicode_literals

from .base import BaseDataSource


class ModelDataSource(BaseDataSource):
    """
    Data source for Django models(queryset)
    """
    def __init__(self, queryset, fields):
        self.queryset = queryset
        self.fields = fields
        self.data = self.normalize_data()

    def normalize_data(self):
        data = [
            [self.get_field_value(row, field) for field in self.fields]
            for row in self.queryset
        ]
        return data

    def get_field_value(self, row, field):
        value = getattr(row, field)
        if callable(value):
            return value()
        else:
            return value
