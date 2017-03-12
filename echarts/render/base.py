# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from ..utils import transpose


class BaseChart(object):
    def __init__(self, data_source, title="Chart", axes=None):
        self.data_source = data_source
        self.title = title
        if axes:
            self.axes = axes
        elif hasattr(data_source, 'axes'):
            self.axes = data_source.axes
        else:
            self.axes = None
        self.options = self.aggregate_options()

    def aggregate_options(self):
        """
        Return [echat options](http://echarts.baidu.com/option.html) as a dict
        """
        options = {}
        options['title'] = self.get_title()
        options['legend'] = self.get_legend()
        options['grid'] = self.get_grid()
        options['xAxis'] = self.get_xAxis()
        options['yAxis'] = self.get_yAxis()
        options['tooltip'] = self.get_tooltip()
        options['toolbox'] = self.get_toolbox()
        options['series'] = self.get_series_array()
        return options

    def get_title(self):
        return {
            'text': self.title,
            'x': 'center'
        }

    def get_legend(self):
        return {
            'bottom': 10,
            'data': self.axes or [],
        }

    def get_grid(self):
        return {}

    def get_xAxis(self):
        return {}

    def get_yAxis(self):
        return {}

    def get_tooltip(self):
        return {}

    def get_toolbox(self):
        return {
            'show': True,
            'feature': {
                'dataZoom': {
                    'yAxisIndex': 'none'
                },
                'dataView': {
                    'readOnly': True
                },
                'magicType': {
                    'type': ['line', 'bar', 'stack', 'tiled']
                },
                'restore': {},
                'saveAsImage': {}
            }
        }

    def Axes(self, value):
        self.axes = value
        return self

    def xAxis(self, data=None, **kwargs):
        """
        Usage
        Short form: chart.xAxis([2015, 2016, 2017])
        Long form:
        chart.xAxis(data=[2015, 2016, 2017], type='category', name='Year')
        """
        kwargs['data'] = data
        self.options['xAxis'].update(kwargs)
        return self

    def yAxis(self, data=None, **kwargs):
        """
        """
        self.options['yAxis'].update(kwargs)
        return self

    def Legend(self, **kwargs):
        self.options['legend'].update(kwargs)
        return self

    def Tooltip(self, **kwargs):
        self.options['tooltip'].update(kwargs)
        return self

    def Toolbox(self, **kwargs):
        self.options['toolbox'].update(kwargs)
        return self

    def get_series_array(self):
        series_arr = transpose(self.data_source.data)
        return [
            self.get_series(idx, series)
            for idx, series in enumerate(series_arr)
        ]

    def get_series(self, idx, series):
        ret = {
            'data': series,
            'type': self.type,
        }
        if self.axes:
            ret['name'] = self.axes[idx]
        return ret


class Bar(BaseChart):
    type = 'bar'


class Line(BaseChart):
    type = 'line'


class Pie(BaseChart):
    series_index = 0
    type = 'pie'

    def get_xAxis(self):
        return {
            'show': False,
        }

    def get_yAxis(self):
        return {
            'show': False,
        }

    def get_series_array(self):
        series_arr = transpose(self.data_source.data)
        series = self.data_source.data`[self.series_index]

        return [{
            'type': self.type,
            'radius': '55%',
            'data': [
                {
                    'value': val,
                    'name': self.axes[i],
                }
                for i, val in enumerate(series)
            ],

        }]

    def get_toolbox(self):
        return {
            'show': True,
            'feature': {
                'dataView': {
                    'readOnly': True
                },
                'saveAsImage': {}
            }
        }
