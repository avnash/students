from django.conf.urls import patterns, url
from oauth import views

urlpatterns = patterns('',

	url(r'^$', views.index, name='index'),
	url(r'^authorize/', views.authorize, name='authorize'),
	url(r'^authenticate/', views.authenticate, name='authenticate'),
	url(r'^signout', views.signout, name='signout'),
	url(r'^request_token/', views.request_token, name='request_token'),
	url(r'^request_access/', views.request_access, name='request_access'),
	
	url(r'^client_login/', views.authorize, name='client_login'),
	url(r'^client_create/', views.authorize, name='client_create'),
	url(r'^user_login/', views.authorize, name='user_login'),
	url(r'^user_create/', views.authorize, name='user_create'),

)
