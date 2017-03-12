# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from ..utils import transpose


class BaseDataSource(object):
    """
    Concept:

    data: 2 dimension table. each column represents a series.
    axes: the names of all series, it is the column names under the table view
    indices: it is the row names under the table view
    """
    def as_table(self):
        return [row for row in self.data]

    def T(self):
        """
        Perform a matrix transpose on data
        """
        self.data = transpose(self.data)
        return self
