from django.contrib.auth import authenticate, login, get_user_model
from django.http import HttpRequest
from django.shortcuts import render, redirect
from .forms import ContactForm, LoginForm, RegisterForm

def home_page(request):
	context = {
		"title":"Homepages",
		"content":"Welocme to the Home page",
		
	}
	if request.user.is_authenticated():
		context["premium_content"]= "YEAHHHHHHH"
	return render(request, "home.html", context)

def about_page(request):
	context = {
		"title":"AboutPage",
		"content":"welcome to the about us page"
	}
	return render(request, "home.html",context)

def contact_page(request):
	contact_form = ContactForm(request.POST or None)
	context = {
		"title":"ContactPage changed",
		"content":"welcome to the content page",
		"form": contact_form
	}
	if contact_form.is_valid():
		print(contact_form.cleaned_data)

	print(request.POST)
	return render(request, "contact/view.html",context)

def login_page(request):
	form = LoginForm(request.POST or None)
	context ={
		"form":form
	}
	print("user logged in ")
	print(request.user.is_authenticated())
	if form.is_valid():
		print(form.cleaned_data)
		username = form.cleaned_data.get("username")
		password =form.cleaned_data.get("password") 
		user = authenticate(request, username=username , password=password)
		if user is not None:
			login(request, user)
			context['form'] = LoginForm()
			return redirect("/")
			#Redirect page is success
		else:
			#return an 'invalid login' error page
			print('Error')	
		
	return render(request , "auth/login.html",context)
User= get_user_model()
def register_page(request):
	form = RegisterForm(request.POST or None)
	context ={
		"form":form,
	}
	if form.is_valid():
		print(form.cleaned_data)
		username = form.cleaned_data.get("username")
		email = form.cleaned_data.get("email")
		password =form.cleaned_data.get("password") 
		new_user = User.objects.create_user(username,email,password)
		print(new_user)
	return render(request , "auth/login.html",context)