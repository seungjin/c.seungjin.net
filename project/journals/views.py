# Create your views here.

from django.http import HttpResponse
from journals.models import *

def main(request):
  journals = Journals.objects.order_by('-id').all()
  for journal in journals.all() :
    print journal.subject
  return HttpResponse("hi")