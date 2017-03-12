from __future__ import absolute_import, unicode_literals

from .base import BaseDataSource


class ModelDataSource(BaseDataSource):
    """
    Data source for Django models(queryset)
    """
    def __init__(self, queryset, fields, index_field=None):
        self.queryset = queryset
        if isinstance(fields[0], (list, tuple)):
            self.data_fields = [f[0] for f in fields]
            self.axes = [f[1] for f in fields]
        else:
            self.data_fields = fields
            self.axes = []
        self.data = self.normalize_data()

        self.indices = []
        if index_field:
            self.indices = [
                self.get_field_value(row, index_field)
                for row in self.queryset
            ]

    def normalize_data(self):
        data = [
            [self.get_field_value(row, field) for field in self.data_fields]
            for row in self.queryset
        ]
        return data

    def get_field_value(self, row, field):
        value = getattr(row, field)
        if callable(value):
            return value()
        else:
            return value
