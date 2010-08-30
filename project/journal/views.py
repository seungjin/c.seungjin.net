# Create your views here.

from django.http import HttpResponse
from django.template import Context
from django.template.loader import get_template

from time import gmtime, strftime, localtime, tzname

from django.core.context_processors import csrf
from django.shortcuts import render_to_response


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

def recent(request,size=None):
  access_log(request)
  if size == None : size = 100
  journals = Journals.objects.filter(publishing_code=1).order_by('-id').all()[0:size]
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
  if request.POST.has_key('subject') :
    subject = request.POST['subject']
  else :
    subject = None
  if request.POST.has_key('message') :
    message = request.POST['message']
  else :
    message = None
  if subject != None :
    journal = Journals(
      date = strftime("%Y-%m-%d",localtime()),
      time = strftime("%H:%M:%S",localtime()),
      timezone = tzname[0],
      tag = "Scratch",
      subject = subject,
      publishing_code = 1,
      body = message,
      ref = None,
      created_at = strftime("%Y-%m-%d %H:%M:%S",localtime())
    )
    journal.save()
  c = {}
  c.update(csrf(request))
  template = get_template('journal/post.html')
  variables = Context({ })
  output = template.render(variables)
  #return HttpResponse(output,c)
  return render_to_response('journal/post.html',c)
  