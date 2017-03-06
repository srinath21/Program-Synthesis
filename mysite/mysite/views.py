from django.shortcuts import render
from django.contrib.auth.models import User
def Startpage(request):
	if request.user.is_authenticated():
		return render (request, 'welcome.html',{'logout':True})
	return render(request, 'welcome.html')
