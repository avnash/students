from django.contrib import admin
from oauth.models import *

admin.site.register(Client)
admin.site.register(User)
admin.site.register(UserCred)
admin.site.register(ClientCred)
admin.site.register(UserAuthLog)
