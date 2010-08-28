#!/usr/env python

import sys, os

INTERP = "/home/seungjin/webapps/c.seungjin.net/bin/python"

if sys.executable != INTERP:
  os.execl(INTERP, INTERP, *sys.argv)

sys.path.append("/home/seungjin/webapps/c.seungjin.net/project")

os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

import django.core.handlers.wsgi

application = django.core.handlers.wsgi.WSGIHandler() 

