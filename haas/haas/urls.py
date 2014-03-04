#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url

urlpatterns = patterns(
    '',
    url(r'^$', 'highlighter.views.highlighter'),
    url(r'^highlight/$', 'highlighter.views.highlight', name='highlight'),
    url(r'^highlight/(?P<lexer_name>[^/]+)/$', 'highlighter.views.highlight'),
)
