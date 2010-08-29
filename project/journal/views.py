# Create your views here.

from django.http import HttpResponse
from django.template import Context
from django.template.loader import get_template

from time import gmtime, strftime, localtime, tzname

from journal.models import *

def access_log(request):
  if request.META.has_key('HTTP_REFERER') :
    http_referer = request.META['HTTP_REFERER']
  else:
    http_referer = None
  acessLog = AccessLogs(
    timestamp = strftime("%Y-%m-%d %H:%M:%S",localtime()),
    timezone = tzname[0],
    remote_ip = request.META['REMOTE_ADDR'],
    user_agent = request.META['HTTP_USER_AGENT'],
    url = request.META['SERVER_PROTOCOL'].split("/")[0].lower() + "://" + request.META['HTTP_HOST'] + request.META['PATH_INFO'],
    http_referer = http_referer
  )
  acessLog.save()


def all(request):
  access_log(request)
  journals = Journals.objects.filter(publishing_code=1).order_by('-id').all()
  variables = Context({
    'http_host' : request.META['HTTP_HOST'],
    'current_time' : strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime()),
    'journals' : journals
  })
  template = get_template('journal/main.html')
  output = template.render(variables)
  return HttpResponse(output)

def recent100(request):
  access_log(request)
  journals = Journals.objects.filter(publishing_code=1).order_by('-id').all()[0:100]
  variables = Context({
    'http_host' : request.META['HTTP_HOST'],
    'current_time' : strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime()),
    'journals' : journals
  })
  template = get_template('journal/main.html')
  output = template.render(variables)
  return HttpResponse(output)
  
def view_with_id(request, id):
  access_log(request)
  journals = Journals.objects.filter(publishing_code=1).filter(id=id).order_by('-id').all()
  variables = Context({
    'current_time' : strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime()),
    'journals' : journals
  })
  template = get_template('journal/view_with_id.html')
  output = template.render(variables)
  return HttpResponse(output)

def post(request):
  return HttpResponse("-")
  
  