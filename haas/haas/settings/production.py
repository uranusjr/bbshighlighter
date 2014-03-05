#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .base import *     # noqa


SECRET_KEY = get_env_var('SECRET_KEY')

STATIC_ROOT = get_env_var('STATIC_ROOT')
