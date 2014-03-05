#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Custom formatter for Pygments
"""

from __future__ import unicode_literals
from pygments.formatters.terminal256 import (
    EscapeSequence as ESCEscapeSequence,
    Terminal256Formatter,
)

__all__ = ['BBSFormatter']


class ControlUEscapeSequence(ESCEscapeSequence):
    def escape(self, *attrs, **kwargs):
        if attrs or kwargs.pop('force', False):
            return '\x15[' + ';'.join(attrs) + 'm'
        return ''

    def color_string(self):
        attrs = []
        if self.bold:
            attrs.append('1')
        if self.underline:
            attrs.append('4')
        if self.fg is not None:
            attrs.append('3%i' % self.fg)
        if self.bg is not None:
            attrs.append('4%i' % self.bg)
        return self.escape(*attrs)

    def reset_string(self):
        return self.escape(force=True)


class BBSFormatter(Terminal256Formatter):
    """Custom Pygments formatter for BBS ASCII coloring

    BBS uses ASCII coloring code with either ^U (0x15) or ESC (0x1b) as the
    escape character, and has only 8 colors and bolds (blinks are not used).
    """

    ESCAPE_SEQUENCE_CONTROL_U = 'ControlUEscapeSequence'
    ESCAPE_SEQUENCE_ESC = 'ESCEscapeSequence'

    def __init__(self, **options):
        """Customized initializer

        This initializer accepts an extra option ``escape_char``. Defaults to
        ``ESCAPE_WITH_CONTROL_U``.
        """
        escape_sequence_name = options.get(
            'escape_sequence',
            BBSFormatter.ESCAPE_SEQUENCE_CONTROL_U,
        )
        self.escape_sequence = globals()[escape_sequence_name]
        super(BBSFormatter, self).__init__(**options)

    def _build_color_table(self):
        self.xterm_colors.append((0x00, 0x00, 0x00))    # 0 Black
        self.xterm_colors.append((0xcd, 0x00, 0x00))    # 1 Red
        self.xterm_colors.append((0x00, 0xcd, 0x00))    # 2 Green
        self.xterm_colors.append((0xcd, 0xcd, 0x00))    # 3 Yellow
        self.xterm_colors.append((0x00, 0x00, 0xcd))    # 4 Blue
        self.xterm_colors.append((0xcd, 0x00, 0xcd))    # 5 Magneta
        self.xterm_colors.append((0x00, 0xcd, 0xcd))    # 6 Cyan
        self.xterm_colors.append((0xe5, 0xe5, 0xe5))    # 7 White

    def _setup_styles(self):
        for ttype, ndef in self.style:
            escape = self.escape_sequence()
            if ndef['color']:
                escape.fg = self._color_index(ndef['color'])
                if escape.fg == 0:
                    escape.bold = True
            if ndef['bgcolor']:
                escape.bg = self._color_index(ndef['bgcolor'])
            if self.usebold and ndef['bold']:
                escape.bold = True
            if self.useunderline and ndef['underline']:
                escape.underline = True
            self.style_string[str(ttype)] = (
                escape.color_string(),
                escape.reset_string()
            )

    def _closest_color(self, r, g, b):
        distance = 257 * 257 * 3
        match = 7

        for i, values in enumerate(self.xterm_colors):
            rd = r - values[0]
            gd = g - values[1]
            bd = b - values[2]
            d = rd * rd + gd * gd + bd * bd
            if d < distance:
                match = i
                distance = d
        return match
