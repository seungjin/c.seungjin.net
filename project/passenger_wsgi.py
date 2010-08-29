#!/usr/env python

import sys, os

INTERP = os.path.dirname(__file__) + "../bin/python"

if sys.executable != INTERP:
  os.execl(INTERP, INTERP, *sys.argv)

sys.path.append(os.path.dirname(__file__))

os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

import django.core.handlers.wsgi

application = django.core.handlers.wsgi.WSGIHandler() 

