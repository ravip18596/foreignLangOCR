"""
WSGI config for foreignLangOCR project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'foreignLangOCR.settings')
os.environ.setdefault('TESSDATA_PREFIX', os.getcwd() + '/tessdata2')
os.environ.setdefault('LC_ALL','C')

application = get_wsgi_application()
