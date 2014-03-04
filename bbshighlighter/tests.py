#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from nose.tools import assert_equals
from pygments import highlight
from pygments.lexers import CLexer
from .formatters import BBSFormatter


def test_format():
    source = 'static'
    highlighted = highlight(source, CLexer(), BBSFormatter())
    assert_equals(highlighted.strip(), '\x15[38;5;28;01mstatic\x15[39;00m')
