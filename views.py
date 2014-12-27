from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
from django.shortcuts import render_to_response
# Create your views here.

#def hello(request):
#	name = "Anant"
#	html = "<html><body>Hello %s! This seems to have worked.</body></html>" %name
	#return HttpResponse(html)

def about(request):
	t = get_template('about.html')
	html = t.render(Context())
	return HttpResponse(html)

def contact(request):
	r=get_template('contact.html')
	html = r.render(Context())
	return HttpResponse(html)

def home(request):
	return render_to_response('home.html')
	
def login(request):
	return render_to_response('login.html')

def signup(request):
	return render_to_response('signup.html')

def postad(request):
	return render_to_response('postad.html')
