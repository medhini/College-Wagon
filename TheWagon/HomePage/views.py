from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
from django.shortcuts import render_to_response
# Create your views here.

def about(request):
	return render_to_response('about.html')

def contact(request):
	return render_to_response('contact.html')

def home(request):
	return render_to_response('home.html')
	
def login(request):
	return render_to_response('login.html')

def signup(request):
	return render_to_response('signup.html')

def postad(request):
	return render_to_response('postad.html')
