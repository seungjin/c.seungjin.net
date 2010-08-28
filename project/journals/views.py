# Create your views here.

from django.http import HttpResponse
from journals.models import *

def main(request):
  return HttpResponse("hi")