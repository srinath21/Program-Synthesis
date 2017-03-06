from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.http import HttpResponse
from searchApp.models import Query
# Create your views here.
def LoginPage(request):
	users=User.objects.all()
	if request.method=='POST':
		name=request.POST.get('name')
		user_password=request.POST.get('password')
		user=authenticate(username=name, password=user_password)
		if user is not None:
			if user.is_active:
				query=Query.objects.all()
				response="Logged in successfully"
				return render(request, '/search/',{'options_list':query})
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
		user=User.objects.create_user(username, email, password, first_n)
		user.first_name=first_name
		user.last_name=last_name
		user.save()
		return HttpResponse("Success")
	return render(request, 'register.html')
