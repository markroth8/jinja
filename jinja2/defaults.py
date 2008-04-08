# -*- coding: utf-8 -*-
"""
    jinja.defaults
    ~~~~~~~~~~~~~~

    Jinja default filters and tags.

    :copyright: 2007 by Armin Ronacher.
    :license: BSD, see LICENSE for more details.
"""
from jinja2.filters import FILTERS as DEFAULT_FILTERS
from jinja.tests import TESTS as DEFAULT_TESTS
DEFAULT_NAMESPACE = {}


__all__ = ['DEFAULT_FILTERS', 'DEFAULT_TESTS', 'DEFAULT_NAMESPACE']
