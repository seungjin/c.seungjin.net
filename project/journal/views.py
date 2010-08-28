# Create your views here.

from django.http import HttpResponse
from django.template import Context
from django.template.loader import get_template

from time import gmtime, strftime

from journal.models import *

def main(request):
  journals = Journals.objects.filter(publishing_code=1).order_by('-id').all()
  variables = Context({
    'current_time' : strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime()),
    'journals' : journals
  })
  template = get_template('journal/main.html')
  output = template.render(variables)
  return HttpResponse(output)
  
def view_with_id(request, id):
  journals = Journals.objects.filter(publishing_code=1).filter(id=id).order_by('-id').all()
  variables = Context({
    'current_time' : strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime()),
    'journals' : journals
  })
  template = get_template('journal/view_with_id.html')
  output = template.render(variables)
  return HttpResponse(output)

def post(request):
  pass