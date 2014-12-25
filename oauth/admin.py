from django.contrib import admin
from oauth.models import *

class ClientAdmin(admin.ModelAdmin):
    list_display = ('id','client_name','client_uri', 'client_id')

class ClientCredAdmin(admin.ModelAdmin):
    list_display = ('id','client', 'client_secret')

class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'firstname', 'lastname', 'hostel', 'room')

class UsertypeAdmin(admin.ModelAdmin):
    list_display = ('id','usertype')

class ScopeAdmin(admin.ModelAdmin):
    list_display = ('id','scope')

class ResponseTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'responsetype')

class HostelAdmin(admin.ModelAdmin):
    list_display = ('id', 'hostel_name')

class UserAuthLogAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'authorization_code', 'access_token', 'trash', 'expiry', 'ip', 'timestamp')
    list_filter = ['timestamp']

class UserCredAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'encrypt_key')

class LoginRequestLogAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'meta_remote_addr', 'timestamp', 'meta_http_host', 'meta_http_referer', 'meta_http_user_agent', 'meta_remote_host', 'meta_request_method')
    readonly_fields = ('id', 'username', 'meta_remote_addr', 'timestamp', 'meta_http_host', 'meta_http_referer', 'meta_http_user_agent', 'meta_remote_host', 'meta_request_method')
    list_filter = ['timestamp', 'username']

class UserLogAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'count')
    ordering = ['-count']
    readonly_fields = ('id', 'username', 'count')

admin.site.register(Client, ClientAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(UserCred, UserCredAdmin)
admin.site.register(ClientCred,ClientCredAdmin)
admin.site.register(UserAuthLog, UserAuthLogAdmin)
admin.site.register(ResponseType, ResponseTypeAdmin)
admin.site.register(Scope, ScopeAdmin)
admin.site.register(Usertype, UsertypeAdmin)
admin.site.register(Hostel, HostelAdmin)
admin.site.register(LoginRequestLog, LoginRequestLogAdmin)
admin.site.register(UserLog, UserLogAdmin)
