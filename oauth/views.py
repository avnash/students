from django.shortcuts import render, get_object_or_404
from oauth.models import *
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth import hashers
import re, datetime, json

from utilities import *

def index(request):
	template = 'oauth/index.html'
	user = getUserData(request)
	context = {'user': user,
		  }
	return render(request, template, context )

def authorize(request):
	user = getUserData(request)
	client = getClientData(request.GET)
	if(isClient(client)):
		if user['loggedIn']:
			auth_code = request.session['auth_code']
			client_redirect_uri = client['redirect_uri']
			state = client['state']
			return redirectWithAuthCode(client_redirect_uri, auth_code, state )
		msg_num = request.GET['msg'] if request.GET.__contains__('msg') else 0
		if(msg_num=='1'):
			message='Valid Username and Password required'
		else:
			message=False
		context = {'client': client, 'message':message}
		template = 'oauth/authorize.html'
		return render(request, template, context )
	return HttpResponseRedirect(client['redirect_uri']+'?state='+client['state'])

def authenticate(request):
	if request.session.__contains__('loggedIn') and request.session['loggedIn']:
		auth_code = request.session['auth_code']
		state = request.POST['state']
		client_redirect_uri = request.POST['redirect_uri']
		return redirectWithAuthCode(client_redirect_uri, auth_code, state)
	else:
		username = request.POST['username']
		password = request.POST['password']
		loginRequestLog(request)
		trueCred = userLogin(username, password)
		client = getClientData(request.POST)
		if(trueCred):
			request.session['loggedIn'] = True
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
			auth = UserAuthLog(user_id=user['id'], authorization_code=auth_code, access_token=access_token, trash=0, expiry=datetime.datetime.now()+datetime.timedelta(days=30), ip=request.META.get('REMOTE_ADDR'), timestamp=datetime.datetime.now())
			auth.save()
			client_redirect_uri = client['redirect_uri']
			state = client['state']
			return redirectWithAuthCode(client_redirect_uri, auth_code, state )
		else:
			request.session['loggedIn'] = False
			message='1'
			return HttpResponseRedirect(getAuthUri(client, message))

def request_token(request):
	client_auth = getClientCred(request)
	if(isClientAuth(client_auth)):
		try:
			auth = UserAuthLog.objects.get(authorization_code__exact=client_auth['authorization_code'])
		except UserAuthLog.DoesNotExist:
			return 0
		if auth.trash==0:
			access_token = {'access_token':auth.access_token}
			access_token_json = json.dumps(access_token)
			return HttpResponse(access_token_json, content_type='application/json')
		else:
			return 0
	else:
		return 0

def request_access(request):
	client_auth = getClientCredToken(request)
	if(isClientAuth(client_auth)):
		try:
			auth = UserAuthLog.objects.get(access_token__exact=client_auth['access_token'])
		except UserAuthLog.DoesNotExist:
			return 0
		if auth.trash==0:
			user_id = auth.user_id
			user_temp = User.objects.get(pk=user_id)
			user = {'loggedIn':True,'username':user_temp.username}
			user_json = json.dumps(user)
			return HttpResponse(user_json, content_type='application/json')
		else:
			return 0
	else:
		return 0

def signout(request):
	request.session['loggedIn'] = False
	if request.session.__contains__('username'):
		request.session.__delitem__('username')
	auth = UserAuthLog.objects.get(authorization_code__exact=request.session['auth_code'])
	auth.trash=1
	auth.save()
	if request.session.__contains__('auth_code'):
		request.session.__delitem__('auth_code')

	client = getClientData(request.GET)
	return HttpResponseRedirect(client['redirect_uri']+'?state='+client['state'])
