# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals


class BaseDataSource(object):

    @property
    def T(self):
        """
        Perform a matrix transpose on data
        """
        self.data = [
            [row[i] for row in self.data]
            for i in range(len(self.data[0]))
        ]
        return self
