# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from ..utils import transpose

class BaseDataSource(object):
    """
    Concept:

    data: 2 dimension table. each column represents a series.
    axes: the names of all series is
    """
    def as_table(self):
        return [row for row in self.data]

    def T(self):
        """
        Perform a matrix transpose on data
        """
        self.data = transpose(self.data)
        return self
