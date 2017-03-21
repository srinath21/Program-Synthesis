from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from searchApp.models import Query, Code_Query, Code
# Create your views here.
def LoginPage(request):
	users=User.objects.all()
	if request.method=='POST':
		name=request.POST.get('name')
		user_password=request.POST.get('password')
		user=authenticate(username=name, password=str(user_password))
		if user is not None:
			if user.is_active:
				login(request, user)
				return HttpResponseRedirect('/welcome/')
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
		user=User.objects.create_user(username, email, password, first_name=first_name, last_name=last_name)
		return HttpResponseRedirect('/login/')
	else:
		return render(request, 'register.html')

def Search(request):
	if request.user.is_authenticated():
		query=Query.objects.all()
		return render(request, 'search.html', {'options_list':query, 'user':request.user})
	return HttpResponseRedirect('/login/')

def SearchResult(request):
	if request.method=='GET':
		option=request.GET.get('option')
		query=Query.objects.get(query_text=option)
		query_id=query.id
		code_query=Code_Query.objects.all()
		for code_object in code_query:
			if query_id==code_object.query:
				return render(request, 'searchResult.html', {'code_exists':True, 'code':Code.objects.get(id=code_object.id)})
		return render(request, 'searchResult.html', {'code_exists':False})
def Logout(request):
	logout(request)
	return HttpResponseRedirect('/welcome/')

def addCode(request):
	return render(request, 'addCode.html')
