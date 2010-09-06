# Create your views here.

from django.http import HttpResponse
from django.template import Context
from django.template.loader import get_template

from time import gmtime, strftime, localtime, tzname

from django.core.context_processors import csrf
from django.shortcuts import render_to_response


from picture.models import *

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

def view_with_id(request, id):
  access_log(request)
  pictures = Pictures.objects.filter(publishing_code=1).filter(id=id).order_by('-id').all()

  if pictures.count() == 0 :
    return HttpResponse("image not available")
  
  response = HttpResponse(pictures[0].image_blob)
  response['Content-Type'] = pictures[0].content_type
  response['Cache-Control'] = 'max-age=7200'
  return response

  