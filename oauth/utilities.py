from django.shortcuts import render, get_object_or_404
from oauth.models import *
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth import hashers
import re
import datetime
import json
import string
import random,ldap

def isClient(client):
	try:
		client = Client.objects.get(client_id__exact=client['client_id'])
	except Client.DoesNotExist:
		return False
	return True

def isClientAuth(client_auth):
	client_id = client_auth['client_id']
	client_secret = client_auth['client_secret']
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

def getClientData(requestGET):
	client = {'client_id': requestGET['client_id']}
	client['response_type']= requestGET['response_type']
	client['redirect_uri'] = requestGET['redirect_uri']
	client['scope'] = requestGET['scope']
	client['state'] = requestGET['state']
	return client

def getUserData(request):
	if request.session.__contains__('loggedIn'):
		user = {'loggedIn': request.session['loggedIn']}
	else:
		user = {'loggedIn': False}
	if(user['loggedIn']):
		user['username'] = request.session.__getitem__('username')
		user_temp = User.objects.get(username__exact=user['username'])
		user['firstname'] = user_temp.firstname
		user['lastname'] = user_temp.lastname
		user['id'] = user_temp.id
	return user

def getAuthUri(client,message=''):
	return reverse('oauth:authorize')+'?response_type='+client['response_type']+'&client_id='+client['client_id'] +'&redirect_uri='+client['redirect_uri']+'&scope='+client['scope']+'&state='+client['state']+'&msg='+message

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

	ldapServer = "ldap://ldap.iitm.ac.in"
	ldapPort = '389'
	ld = ldap.initialize(ldapServer+':'+ldapPort)
	ldapPass = "rE11Bg_oO~iC"
	ldapDn = "cn=students,ou=bind,dc=ldap,dc=iitm,dc=ac,dc=in"
	ld.simple_bind_s(ldapDn,ldapPass)
	ldapDn = "dc=ldap,dc=iitm,dc=ac,dc=in"
	searchScope = ldap.SCOPE_SUBTREE
	retrieveAttributes = None
	searchFilter = "uid="+username
	ldap_result_id = ld.search(ldapDn,searchScope,searchFilter, retrieveAttributes)
	dn = ld.result(ldap_result_id,0)[1][0][0]
	try:
		ld.simple_bind_s(dn,password)

	except ldap.LDAPError, e:
		try:
			UserCred.objects.get(encrypt_key__exact=password, user_id__exact=user.id)
		except UserCred.DoesNotExist:
			return False
	return True


def getClientCred(request):
	client = {'client_id': request.GET['client_id']}
	client['client_secret']= request.GET['client_secret']
	client['grant_type'] = request.GET['grant_type']
	client['redirect_uri'] = request.GET['redirect_uri']
	client['authorization_code'] = request.GET['authorization_code']
	return client

def getClientCredToken(request):
	client = {'client_id': request.GET['client_id']}
	client['client_secret']= request.GET['client_secret']
	client['access_token'] = request.GET['access_token']
	return client

def loginRequestLog(request):
	username = request.POST['username'] if request.POST.__contains__('username') else 'error'
	try:
		user = UserLog.objects.get(username__exact=username)
		user.count = 1+user.count
	except UserLog.DoesNotExist:
		user = UserLog(username=username, count=1)
	user.save()
	meta_http_host = request.META['HTTP_HOST']
	meta_http_referer = request.META['HTTP_REFERER']
	meta_http_user_agent = request.META['HTTP_USER_AGENT']
	meta_query_string = request.META['QUERY_STRING']
	meta_remote_addr = request.META['REMOTE_ADDR']
	meta_remote_host = request.META['REMOTE_HOST'] if request.META.__contains__('REMOTE_HOST') else 'error'
	meta_request_method = request.META['REQUEST_METHOD']
	loginRequestLog = LoginRequestLog(
							username=username,
							meta_http_host = meta_http_host,
							meta_http_referer = meta_http_referer,
							meta_http_user_agent = meta_http_user_agent,
							meta_query_string = meta_query_string,
							meta_remote_addr = meta_remote_addr,
							meta_remote_host = meta_remote_host,
							meta_request_method = meta_request_method,
							timestamp = datetime.datetime.now()
						)
	loginRequestLog.save()
