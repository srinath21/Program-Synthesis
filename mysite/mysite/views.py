from django.shortcuts import render
from django.contrib.auth.models import User
def Startpage(request):
	return render(request, 'search.html')

def LoginPage(request):
	users=User.objects.all()
	return render(request, 'login.html',{'user_list':users})

def Register(request):
	return render(request, 'register.html')
