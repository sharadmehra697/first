from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from shop.models import first
# Create your views here.
def HomePage(request):
	
	return HttpResponse('all set')