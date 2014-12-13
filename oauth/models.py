from django.db import models

class Usertype(models.Model):
	typename = models.CharField(max_length=50)

class Scope(models.Model):
	scopename = models.CharField(max_length=50)

class User(models.Model):
	username = models.CharField(max_length=100)
	usertypes = models.ManyToManyField(Usertype)
	
	def __unicode__(self):
		return self.username

class Client(models.Model):
	client_id = models.CharField(max_length=40)
	client_uri = models.CharField(max_length=200)
	scopes = models.ManyToManyField(Scope)
	def __unicode__(self):
		return self.client_uri

class UserAuthLog(models.Model):
	user = models.ForeignKey(User)
	client = models.ForeignKey(Client)
	ip = models.CharField(max_length=15)
	timestamp = models.DateTimeField()
	
class UserCred(models.Model):
	user = models.ForeignKey(User)
	encrypt_key = models.CharField(max_length=200)

class ClientCred(models.Model):
	client = models.ForeignKey(Client)
	client_secret = models.CharField(max_length=200)
