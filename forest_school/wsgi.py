"""
WSGI config for forest_school project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""
#WSGI is basically the universal
# adapter that lets your Django app talk to any web server

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'forest_school.settings')

application = get_wsgi_application()
