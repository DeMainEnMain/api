"""
WSGI config for euskalmoneta project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings.settings")

os.environ["DATABASE_NAME"] = "api"
os.environ["DATABASE_USER"] = "api"
os.environ["DATABASE_PASSWORD"] = "api"
os.environ["DATABASE_HOST"] = "localhost"
os.environ["DJANGO_DEBUG"] = "True"
os.environ["DOLIBARR_PUBLIC_URL"] = "http://sauvagnon.acacs.org"
os.environ["API_PUBLIC_URL"] = "http://api.acacs.org"
os.environ["BDC_PUBLIC_URL"] = "http://cde.acacs.org"
os.environ["GI_PUBLIC_URL"] = ""
os.environ["CEL_PUBLIC_URL"] = ""

application = get_wsgi_application()
