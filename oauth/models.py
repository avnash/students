from django.db import models
import datetime

class Usertype(models.Model):
	usertype = models.CharField(max_length=50)

class Scope(models.Model):
	scope = models.CharField(max_length=50)

class ResponseType(models.Model):
	responsetype = models.CharField(max_length=50, default='code')

class User(models.Model):
	username = models.CharField(max_length=100)
	firstname = models.CharField(max_length=100)
	lastname = models.CharField(max_length=100)
	usertypes = models.ManyToManyField(Usertype)

	def __unicode__(self):
		return self.username

class Client(models.Model):
	client_id = models.CharField(max_length=40)
	client_uri = models.CharField(max_length=200)
	responsetypes = models.ManyToManyField(ResponseType)
	managers = models.ManyToManyField(User)
	scopes = models.ManyToManyField(Scope)

	def __unicode__(self):
		return self.client_uri

class UserAuthLog(models.Model):
	user = models.ForeignKey(User)
	authorization_code = models.CharField(max_length=40)
	access_token = models.CharField(max_length=60)
	trash = models.IntegerField(default=0)
	expiry = models.DateTimeField()
	ip = models.CharField(max_length=15)
	timestamp = models.DateTimeField(default=datetime.datetime.now())

class UserCred(models.Model):
	user = models.ForeignKey(User)
	encrypt_key = models.CharField(max_length=200)

class ClientCred(models.Model):
	client = models.ForeignKey(Client)
	client_secret = models.CharField(max_length=200)
