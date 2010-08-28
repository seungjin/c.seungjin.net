# Create your views here.

from django.http import HttpResponse
from django.template import Context
from django.template.loader import get_template

from time import gmtime, strftime

from journals.models import *

def main(request):
  journals = Journals.objects.filter(publishing_code=1).order_by('-id').all()
  variables = Context({
    'current_time' : strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime()),
    'journals' : journals
  })
  template = get_template('journals/main.html')
  output = template.render(variables)
  return HttpResponse(output)