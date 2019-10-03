from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
# Create your views here.
def HomePage(request):
	
	return HttpResponse('all set')