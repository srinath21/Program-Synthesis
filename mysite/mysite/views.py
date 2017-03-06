from django.shortcuts import render
from django.contrib.auth.models import User
def Startpage(request):
	return render(request, 'welcome.html')

