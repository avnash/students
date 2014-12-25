from django.db import models
import datetime

class Usertype(models.Model):
	usertype = models.CharField(max_length=50)

	def __unicode__(self):
		return self.usertype

class Scope(models.Model):
	scope = models.CharField(max_length=50)

	def __unicode__(self):
		return self.scope

class Hostel(models.Model):
	hostel_name = models.CharField(max_length=20)

	def __unicode__(self):
		return self.hostel_name

class ResponseType(models.Model):
	responsetype = models.CharField(max_length=50, default='code')

	def __unicode__(self):
		return self.responsetype

class User(models.Model):
	username = models.CharField(max_length=100)
	firstname = models.CharField(max_length=100)
	lastname = models.CharField(max_length=100)
	usertypes = models.ManyToManyField(Usertype)
	hostel = models.ForeignKey(Hostel)
	room = models.IntegerField(default=0)

	def __unicode__(self):
		return self.username

class Client(models.Model):
	client_id = models.CharField(max_length=40)
	client_uri = models.CharField(max_length=200)
	responsetypes = models.ManyToManyField(ResponseType)
	managers = models.ManyToManyField(User)
	scopes = models.ManyToManyField(Scope)
	client_name = models.CharField(max_length=40)

	def __unicode__(self):
		return self.client_uri

class UserAuthLog(models.Model):
	user = models.ForeignKey(User)
	authorization_code = models.CharField(max_length=40)
	access_token = models.CharField(max_length=60)
	trash = models.IntegerField(default=0)
	expiry = models.DateTimeField()
	ip = models.CharField(max_length=15)
	timestamp = models.DateTimeField()

class UserCred(models.Model):
	user = models.ForeignKey(User)
	encrypt_key = models.CharField(max_length=200)

class ClientCred(models.Model):
	client = models.ForeignKey(Client)
	client_secret = models.CharField(max_length=200)

class UserLog(models.Model):
	username = models.TextField()
	count = models.BigIntegerField()

class LoginRequestLog(models.Model):
	username = models.TextField()
	meta_http_host = models.TextField()
	meta_http_referer = models.TextField()
	meta_http_user_agent = models.TextField()
	meta_query_string = models.TextField()
	meta_remote_addr = models.TextField()
	meta_remote_host = models.TextField()
	meta_request_method = models.TextField()
	timestamp = models.DateTimeField()

	def __unicode__(self):
		return self.username
