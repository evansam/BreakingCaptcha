# WSGI file is how the Python web app and the server communicate
"""
WSGI config for BreakingCaptcha project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "BreakingCaptcha.settings")

application = get_wsgi_application()