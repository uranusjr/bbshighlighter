#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django import forms
from pygments.lexers import get_all_lexers


class HighlighterForm(forms.Form):

    language = forms.ChoiceField()
    code = forms.CharField(label='', widget=forms.Textarea)

    def __init__(self, *args, **kwargs):
        kwargs['initial'] = dict(kwargs.get('initial', {}), language='cpp')
        super(HighlighterForm, self).__init__(*args, **kwargs)
        choices = []
        for name, aliases, filetypes, mimetypes in get_all_lexers():
            choices.append((aliases[0], name))
        self.fields['language'].choices = choices
