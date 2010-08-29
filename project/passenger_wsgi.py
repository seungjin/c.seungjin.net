#!/usr/env python

import sys, os

#this_directory = "/home/seungjin/webapps/c.seungjin.net/project"
this_directory = os.path.dirname(__file__)

INTERP = this_directory + "/../bin/python"

if sys.executable != INTERP:
  os.execl(INTERP, INTERP, *sys.argv)

sys.path.append(this_directory)

os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

import django.core.handlers.wsgi

application = django.core.handlers.wsgi.WSGIHandler() 

