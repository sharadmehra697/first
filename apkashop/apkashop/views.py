from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
# Create your views here.
def goShop(request):
	return HttpResponse('Type /Shop/ in Url')