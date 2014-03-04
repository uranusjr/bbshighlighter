"""
WSGI config for haas project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/howto/deployment/wsgi/
"""

import os
import sys

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "haas.settings")

PROJECT_ROOT = os.path.dirname(os.path.dirname(__file__))
sys.path.append(os.path.dirname(PROJECT_ROOT))

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
