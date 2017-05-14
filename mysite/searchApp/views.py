sfrom django.shortcuts import render
from django.contrib.auth.models import User
import os
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from searchApp.models import Query, Code_Query, Code, Feedback, userInfo, insertCode, User_Search
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
			response="Incorrect Username or Password, please try again."
			return render(request, 'login.html', {'invalid':response})

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
		user_info=userInfo.objects.create(user=user)
		return HttpResponseRedirect('/login/')
	else:
		return render(request, 'register.html')

def Search(request):
	if request.user.is_authenticated():
		queries=Query.objects.all()
		applicationName=[]
		functionType=[]
		for query in queries:
			query_text=query.application.title()
			function=query.function.title()
			applicationName.append(query_text)
			try:
				functionType.append(function)
			except:
				continue;
		return render(request, 'search.html', {'options_list':applicationName, 'functions_list':functionType, 'user':request.user})
	return HttpResponseRedirect('/login/')

def SearchResult(request):
	if request.method=='GET':
		option=request.GET.get('option').lower()
		if request.GET.get('functionType'):
			functionType=request.GET.get('functionType').lower()
			query_txt=option
			func_description={}
			codes={}
			functions={}
			lang=[]
			query=Query.objects.filter(application=query_txt, function=functionType)
			app_desc=query[0].app_description

			for i in range(len(query)):
				query_id=query[i].id
				code_query=Code_Query.objects.get(query=query[i])
				Id=code_query.code
				codes[query[i].language]=Code.objects.get(id=Id.id).code_text
				search_query = User_Search.objects.filter(user=request.user, query=query[i]).exists()
				if not search_query:
					search=User_Search.objects.create(user=request.user, query=query[i], code=Code.objects.get(id=Id.id))
				if query[i].function_description not in func_description.keys():
					func_description[query[i].function_description]=codes
				else:
					func_description[query[i].function_description][query[i].language]=codes[query[i].language]

			functions[query[0].function.title()]=func_description
		else:
			query_txt=option
			query=Query.objects.filter(application=query_txt)
			app_desc=query[0].app_description
			functions={}

			app_desc=query[0].app_description
			for i in range(len(query)):
				if query[i].function.title() not in functions.keys():
					func_title=Query.objects.filter(application=query_txt,function=query[i].function)
					codes={}
					func_description={}
					for j in range(len(func_title)):
						code_query=Code_Query.objects.get(query=func_title[j])
						codes[func_title[j].language]=code_query.code.code_text
						search_query=User_Search.objects.filter(user=request.user, query=func_title[j])
						if len(search_query)==0:
							search=User_Search.objects.create(user=request.user, query=func_title[j], code=code_query.code)
						if func_title[j].function_description not in func_description.keys():
							func_description[func_title[j].function_description]=codes
						else:
							func_description[func_title[j].function_description][func_title[j].language]=codes[func_title[j].language]
					functions[func_title[j].function.title()]=func_description


		feedbacks=Feedback.objects.all()
		feedback_list={}
		for i in range(len(feedbacks)):
			feedback_list[feedbacks[i].user.username]=feedbacks[i].feedback_info
		return render(request, 'searchResult.html', {'code_exists':True,'app_name':option.title(),'app_description':app_desc, 'functions_code':functions,'feedback':feedback_list})

		#for code_object in code_query:
			#if query_id==code_object.query:
				#return render(request, 'searchResult.html', {'code_exists':True, 'code':Code.objects.get(id=code_object.id)})
		return render(request, 'searchResult.html', {'code_exists':False})
def Execute(request):
	if request.method=='POST' and request.user.is_authenticated():
		lang=request.POST.get('language')
		code=request.POST.get('code')
		if lang=="Python":
			fh=open("test.py",'w')
			fh.write(code)
			fh.close()
			try:
				os.system("python test.py > output.txt")
				fh=open("output.txt",'r')
				output_data=fh.read()
				fh.close()
				#os.system("rm test.py output")
				return render(request, 'output.html',{'output':output_data})
			except:
				#os.system('rm test.py output')
				return HttpResponse("Could not execute")
		elif lang=="C":
			fh=open("test.c",'w')
			fh.write(code)
			fh.close()
			try:
				os.system("gcc test.c")
				os.system("./a.out > output.txt")
				fh=open("output.txt",'r')
				output_data=fh.read()
				fh.close()
				#os.system("rm test.c ./a.out output")
				return render(request, 'output.html', {'output':output_data})
			except:
				#os.system('rm test.c ./a.out output')
				return HttpResponse("Could not execute")
		else:
			return HttpResponse("Invalid Language")


def Logout(request):
	logout(request)
	return HttpResponseRedirect('/welcome/')

def addCode(request):
	if request.method=='POST' and request.user.is_authenticated():
			applicationName=request.POST.get('applicationName').lower()
			functionType=request.POST.get('functionType').lower()
			applicationCode=request.POST.get('applicationCode')
			appDescription=request.POST.get('app_description')
			funcDescription=request.POST.get('function_description')
			lang=request.POST.get('language')
			user=User.objects.get(username=request.user.username)
			query=Query.objects.create(application=applicationName, function=functionType, language=lang, app_description=appDescription, function_description=funcDescription)
			code=Code.objects.create(code_text=applicationCode, user=user)
			code_query=Code_Query.objects.create(query=query, code=code)
			return render(request, 'success_add.html')
	elif request.user.is_authenticated():
		if request.user.is_authenticated():
			queries=Query.objects.all()
			applicationName=[]
			functionType=[]
			for query in queries:
				query_text=query.application.title()
				function=query.function.title()
				applicationName.append(query_text)
				try:
					functionType.append(function)
				except:
					continue;
			return render(request, 'addCode.html', {'options_list':applicationName, 'functions_list':functionType, 'user':request.user})
	return HttpResponseRedirect('/login/')

def InsertCode(request):
	if request.method=="POST" and request.user.is_authenticated():
		applicationName=request.POST.get('applicationName').lower()
		functionType=request.POST.get('functionType').lower()
		applicationCode=request.POST.get('applicationCode')
		language=request.POST.get('language1')
		try:
			query=Query.objects.get(application=applicationName, function=functionType, language=language)
		except:
			query=Query.objects.filter(application=applicationName, function=functionType)
			query[0].language=language
		code=insertCode.objects.create(user=request.user, query=query[0],codeText=applicationCode, codeReview=False)
		return render(request, 'success_add.html')
	elif request.user.is_authenticated():
		if request.user.is_authenticated():
			queries=Query.objects.all()
			applicationName=[]
			functionType=[]
			for query in queries:
				query_text=query.application.title()
				function=query.function.title()
				applicationName.append(query_text)
				try:
					functionType.append(function)
				except:
					continue;
		return render(request, 'addCode.html', {'options_list':applicationName, 'functions_list':functionType, 'user':request.user})
	return HttpResponseRedirect('/login/')


def Profile(request):
	if request.user.is_authenticated():
		user_info=userInfo.objects.get(user=request.user)
		insert_code=insertCode.objects.filter(user=request.user)
		new_code=Code.objects.filter(user=request.user)
		codes_added={}
		feedbacks={}
		for i in range(len(insert_code)):
			if insert_code[i].codeReview:
				feedback=Feedback.objects.filter(query=insert_code.query)
				feedbacks={}
				for i in range(len(feedback)):
					feedbacks[feedback[j].query.application]=feedback[j].feedback_info
			codes_added[i]=[insert_code[i].query.application.title(), insert_code[i].query.function.title(), insert_code[i].query.language, insert_code[i].codeText, insert_code[i].codeReview]
			count=i+1
		for i in range(len(new_code)):
			codequery=Code_Query.objects.get(code=new_code[i])
			query_info=Query.objects.get(id=codequery.query.id)
			codes_added[i+count]=[query_info.application.title(), query_info.function.title(), query_info.language.title(), new_code[i].code_text]
			feedback=Feedback.objects.filter(query=codequery.query)
			for j in range(len(feedback)):
				feedbacks[feedback[j].query.application.title()]=feedback[j].feedback_info
		search_history=User_Search.objects.filter(user=request.user)
		search={}
		for i in range(len(search_history)):
			search_app=search_history[i].query.application.title()
			search_func=search_history[i].query.function.title()
			search_code=search_history[i].code.code_text
			search[i]=[search_app, search_func, search_code]


		return render(request, 'profile.html',{'age':user_info.age, 'country':user_info.country,'search_history':search,'code_history':codes_added, 'feedbacks':feedbacks })
	else:
		return HttpResponseRedirect('/login/')

def Settings(request):
	if request.method=='POST' and request.user.is_authenticated():
		username=request.POST.get('username')
		email=request.POST.get('email')
		first_name=request.POST.get('first_name')
		last_name=request.POST.get('last_name')
		age=request.POST.get('age')
		country=request.POST.get('country')
		user_info=userInfo.objects.get(user=request.user)
		user_info.age=age
		user_info.country=country
		user_info.save()
		user_id=User.objects.get(username=request.user.username)
		user_id.username=username
		user_id.email=email
		user_id.first_name=first_name
		user_id.last_name=last_name
		user_id.save()
		return render(request, 'settings.html',{'update_status':"Profile succesfully updated.",'age':user_info.age,'country':user_info.country})
	if request.user.is_authenticated():
		userinfo=userInfo.objects.get(user=request.user)
		return render(request, 'settings.html', {'age':userinfo.age,'country':userinfo.country})
	else:
		return HttpResponseRedirect('/login/')

def password(request):
	updatestatus=""
	if request.method=='POST' and request.user.is_authenticated():
		oldpass=request.POST.get('oldpass')
		newpass=request.POST.get('newpass')
		userinfo=userInfo.objects.get(user=request.user)
		user=User.objects.get(username__exact=request.user.username)
		if user.check_password(oldpass):
			user.set_password(newpass)
			user.save()
			updatestatus="Password Changed"
			return HttpResponseRedirect("/settings/")
		else:
			return render(request,'settings.html',{'update_status':"Incorrect password",'age':userinfo.age,'country':userinfo.country})
def feedback(request):

	if request.method=='POST':
		feedbacks=request.POST.get('feedback')
		app=request.POST.get('application').lower()
		func=request.POST.get('function').lower()
		lang=request.POST.get('language')
		query=Query.objects.get(application=app, function=func, language=lang)
		feedback_id=Feedback.objects.create(feedback_info=feedbacks, user=request.user, query=query)
		return render(request, 'success_feedback.html')
