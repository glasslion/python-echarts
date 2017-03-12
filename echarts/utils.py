# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals


def transpose(matrix):
    return [
        [row[i] for row in matrix]
        for i in range(len(matrix[0]))
    ]
