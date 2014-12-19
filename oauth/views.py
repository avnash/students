from django.shortcuts import render, get_object_or_404
from oauth.models import *
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth import hashers
import re
import datetime
import json
import string
import random

def index(request):
	template = 'oauth/index.html'
	user = getUserData(request)
	context = {'user': user,
		  }
	return render(request, template, context )

def authorize(request):
	user = getUserData(request)
	client = getClientData(request.GET)
	if(isClient(client['client_id'])):
		if user['isLoggedIn']:
			auth_code = request.session['auth_code']
			client_redirect_uri = client['redirect_uri']
			state = client['state']
			return redirectWithAuthCode(client_redirect_uri, auth_code, state )
		context = {'client': client}
		template = 'oauth/authorize.html'
		return render(request, template, context )
	return HttpResponseRedirect(client['redirect_uri']+'?state='+client['state'])

def isClient(client_id):
	try:
		client = Client.objects.get(client_id__exact=client_id)
	except Client.DoesNotExist:
		return False
	return True

def isClientAuth(client_id, client_secret):
	try:
		client = Client.objects.get(client_id__exact=client_id)
	except Client.DoesNotExist:
		return False
	try:
		ClientCred.objects.get(client_id__exact=client.id, client_secret=client_secret)
	except ClientCred.DoesNotExist:
		return False
	return True

def redirectWithAuthCode(client_redirect_uri, auth_code, state):
	return HttpResponseRedirect(client_redirect_uri+'?authorization_code='+auth_code + '&state' + state)

def redirecturl(request):
	return 1

def getClientData(requestGET):
	client = {'client_id': requestGET.__getitem__('client_id') if requestGET.__contains__('client_id') else 'home'  }
	client['response_type']= requestGET.__getitem__('response_type') if requestGET.__contains__('response_type') else 'code'
	client['redirect_uri'] = requestGET['redirect_uri'] if requestGET.__contains__('redirect_uri') else 'http://127.0.0.1:8000/oauth/'
	client['scope'] = requestGET['scope'] if requestGET.__contains__('scope') else 'profile'
	client['state'] = requestGET['state'] if requestGET.__contains__('state') else ''
	return client

def getUserData(request):
	if request.session.__contains__('isLoggedIn'):
		user = {'isLoggedIn': request.session.__getitem__('isLoggedIn')}
	else:
		user = {'isLoggedIn': False}
	if(user['isLoggedIn']):
		user['username'] = request.session.__getitem__('username')
		user_temp = User.objects.get(username__exact=user['username'])
		user['firstname'] = user_temp.firstname
		user['lastname'] = user_temp.lastname
		user['id'] = user_temp.id
	return user
def getAuthUri(client):
	return reverse('oauth:authorize')+'?response_type='+client['response_type']+'&client_id='+client['client_id'] +'&redirect_uri='+client['redirect_uri']+'&scope='+client['scope']+'&state='+client['state']

def authenticate(request):
	if request.session.__contains__('isLoggedIn') and request.session['isLoggedIn']:
		auth_code = request.session['auth_code']
		state = request.POST['state']
		client_redirect_uri = request.POST['redirect_uri']
		return redirectWithAuthCode(client_redirect_uri, auth_code, state)
	else:
		username = request.POST['username']
		password = request.POST['password']
		trueCred = userLogin(username, password)
		client = getClientData(request.POST)
		if(trueCred):
			request.session['isLoggedIn'] = True
			request.session['username'] = username
			user = getUserData(request)
			a = True
			while a:
				auth_code = getAuthCode()
				access_token = getAccessToken()
				try:
					UserAuthLog.objects.get(authorization_code__exact=auth_code)
				except UserAuthLog.DoesNotExist:
					try:
						UserAuthLog.objects.get(access_token__exact=access_token)
					except UserAuthLog.DoesNotExist:
						a = False

			request.session['auth_code'] = auth_code
			request.session['access_token'] = access_token
			auth = UserAuthLog(user_id=user['id'], authorization_code=auth_code, access_token=access_token, trash=0, expiry=datetime.datetime.now(), ip='local', timestamp=datetime.datetime.now())
			auth.save()
			client_redirect_uri = client['redirect_uri']
			state = client['state']
			return redirectWithAuthCode(client_redirect_uri, auth_code, state )
		else:
			request.session['isLoggedIn'] = False
			return HttpResponseRedirect(getAuthUri(client))
def getAuthCode():
	auth_code = ''.join(random.choice(string.ascii_uppercase + string.digits + string.ascii_lowercase) for _ in range(40))
	return auth_code

def getAccessToken():
	access_token = ''.join(random.choice(string.ascii_uppercase + string.digits + string.ascii_lowercase) for _ in range(60))
	return access_token

def userLogin(username, password):
	try:
		user = User.objects.get(username__exact=username)
	except User.DoesNotExist:
		return False
	try:
		UserCred.objects.get(encrypt_key__exact=password, user_id__exact=user.id)
	except UserCred.DoesNotExist:
		return False
	return True

def signout(request):
	request.session['isLoggedIn'] = False
	if request.session.__contains__('username'):
		request.session.__delitem__('username')
	return HttpResponseRedirect(reverse('oauth:index'))

def getClientCred(request):
	client = {'client_id': request.GET.__getitem__('client_id')}
	client['client_secret']= request.GET.__getitem__('client_secret')
	client['grant_type'] = request.GET['grant_type']
	client['redirect_uri'] = request.GET['redirect_uri']
	client['authorization_code'] = request.GET['authorization_code']
	return client

def request_token(request):
	#client_auth = getClientCred(request)
	#user = getUserData(request)
	#if(user['isLoggedIn']):
	#	if client_auth['authorization_code'] == request.session['auth_code']:
	access_token = {'access_token':'access_token'}
	access_token_json = json.dumps(access_token)
	context = {'access_token_json':access_token_json}
	template = 'oauth/request_token.html'
	return render(request, template, context )
#	return HttpResponseRedirect(client_auth['redirect_uri'])

def request_access(request):
	#user = getUserData(request)
	user = {'loggedIn':True, 'username':'ae11b016'}
	user_json = json.dumps(user)
	context = {'user_json':user_json}
	template = 'oauth/request_access.html'
	return render(request, template, context )
