import os
import sys

sys.path.append('/home/helloworld/Avi/instiwo/students/')

os.environ['DJANGO_SETTINGS_MODULE'] = 'students.settings'

import django.core.handlers.wsgi

application = django.core.handlers.wsgi.WSGIHandler()
