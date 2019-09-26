from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from shop.models import first
# Create your views here.
def HomePage(request):
	s=first()
	s.first_name='sharad'
	s.save()
	return HttpResponse(s.first_name)