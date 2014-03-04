#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.http import HttpResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import FormView, View
import pygments
from pygments.lexers import get_lexer_by_name, guess_lexer
from bbshighlighter.formatters import BBSFormatter
from .forms import HighlighterForm


class HighlightView(View):

    @csrf_exempt
    def dispatch(self, *args, **kwargs):
        return super(HighlightView, self).dispatch(*args, **kwargs)

    def post(self, request, lexer_name='', *args, **kwargs):
        code = request.POST.get('code')
        if not code:
            return HttpResponseBadRequest()
        if lexer_name:
            lexer = get_lexer_by_name(lexer_name)
        else:
            lexer = guess_lexer(code)
        result = pygments.highlight(code, lexer, BBSFormatter())
        return HttpResponse(result)


class HighlighterFormView(FormView):

    form_class = HighlighterForm
    template_name = 'highlighter/form.html'


highlight = HighlightView.as_view()
highlighter = HighlighterFormView.as_view()
