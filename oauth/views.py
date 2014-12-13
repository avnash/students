from django.shortcuts import render, get_object_or_404
from oauth.models import User
import re

def index(request):
	template = 'oauth/index.html'
	user = getUserData(request)
	client = getClientData(request)
	context = {'user': user, 
		   'client': client,
		  }
	return render(request, template, context )

def authorize(request):
	context = {'client': getClientData(request), 'user': getUserData(request) }
	template = 'oauth/authorize.html'
	return render(request, template, context )

def getClientData(request):
	client = {'client_id': request.GET.__getitem__('client_id') if request.GET.__contains__('client_id') else 'home'  }
	client['response_type']= request.GET.__getitem__('response_type') if request.GET.__contains__('response_type') else 'code'
	client['redirect_uri'] = request.GET['redirect_uri'] if request.GET.__contains__('redirect_uri') else '127.0.0.1:8000/oauth/'
	client['scope'] = request.GET['scope'] if request.GET.__contains__('scope') else 'profile'
	client['state'] = request.GET['state'] if request.GET.__contains__('state') else ''
        return client

def getUserData(request):
	if request.session.__contains__('isLoggedIn'):
		user = {'isLoggedIn': request.session.__getitem__('isLoggedIn')}
	else:
		user = {'isLoggedIn': False}
	if(user['isLoggedIn']):
		user['username'] = request.session.__getitem__('username')
		user_temp = get_object_or_404(User, username="ae11b016")
	return user
def authenticate(request):
	username = request.POST['username']
	password = request.POST['password']
#	if(normal_login(username, password))

	request.session['username'] = request.POST['username']
	username = request.session['username']
	context = {'username': username}
	template = 'oauth/authenticate.html'
	return render(request, template, context )

def signout(request):
	username = 'avinash'
	context = {'username': username}
	template = 'oauth/signout.html'
	return render(request, template, context )

def request_token(request):
	username = 'avinash'
	context = {'username': username}
	template = 'oauth/request_token.html'
	return render(request, template, context )

def request_access(request):
	username = 'avinash'
	context = {'username': username}
	template = 'oauth/request_access.html'
	return render(request, template, context )

