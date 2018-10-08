from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.views import View

# Create your views here.

class SignUp(View):
	def get(self, request):
		form = UserCreationForm()
		return render(request, 'signup/signup.html', {'form': form})
	def post(self, request):
		form = UserCreationForm(request.POST)
		if form.is_valid():
            		form.save()
            		username = form.cleaned_data.get('username')
            		raw_password = form.cleaned_data.get('password1')
            		user = authenticate(username=username, password=raw_password)
            		login(request, user)
            		return redirect('home')
	

class SignIn(View):
	def get(self, request):
		return render(request, 'signin/signin.html')
	
	def post(self, request):
		username = request.POST.get('username', False)
		password = request.POST.get('password', False)
		user = authenticate(username=username, password=password)
		if user is not None and user.is_active:
			login(request, user)
			return redirect('home')
		return redirect('signin')