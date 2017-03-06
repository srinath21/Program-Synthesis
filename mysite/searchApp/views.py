from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.http import HttpResponse
# Create your views here.
def LoginPage(request):
	users=User.objects.all()
	if request.method=='POST':
		name=request.POST.get('name')
		user_password=request.POST.get('password')
		user=authenticate(username=name, password=user_password)
		if user is not None:
			if user.is_active:
				response="Logged in successfully"
				return HttpResponse(response)
			else:
				response="Invalid Password"
				return HttpResponse(response)
		else:
			response="Username/ password are incorrect"
			return HttpResponse(response)
		
	else:
		return render(request, 'login.html',{'user_list':users})

def Register(request):
	if request.method=='POST':
		username=request.POST.get('username')
		first_name=request.POST.get('first_name')
		last_name=request.POST.get('last_name')
		email=request.POST.get('email')
		password=request.POST.get('password')
		User.objects.create_user(username, email, password)
		return HttpResponse("Success")
	return render(request, 'register.html')
