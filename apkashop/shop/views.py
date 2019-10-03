from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.views import View
# Create your views here.
class userRegis(View):
	def get(self,request):
		udict={'form':'form'}
		if request.session.has_key('login_id'):
			logged=registered_as.objects.get(regis_id=request.session['login_id'])
			userNumber='You are Registered with this '+str(logged.regis_mobile)+' Number'
			udict.update({'userNumber':userNumber})
		return render(request, 'registration.html',udict)


	def post(self,request):
		try:
			g=cut.objects.get(regis_mobile=request.POST.get('user_mobile'))
			return HttpResponse('NumExist')
		except Exception as e:
			uNum=request.POST.get('user_mobile')
			uPass=request.POST.get('user_pass')
			uDate=request.POST.get('user_dob')
			uName=request.POST.get('user_name')
			gObj=registered_as()
			gObj.regis_name=uName
			gObj.regis_mobile=uNum
			gObj.regis_dob=uDate
			gObj.regis_pass=uPass
			gObj.save()
			return HttpResponse('Data Save')