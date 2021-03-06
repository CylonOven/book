# -*- coding: UTF-8 -*-
from lino_voga.projects.std.settings import *

class Site(Site):
    title = "Lino@prj1"
    server_url = "https://prj1.mydomain.com"
    
SITE = Site(globals())

# locally override attributes of individual plugins
# SITE.plugins.finan.suggest_future_vouchers = True

# MySQL
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'prj1',
        'USER': 'django',
        'PASSWORD': 'My cool password',
        'HOST': 'localhost',                  
        'PORT': 3306,
        'OPTIONS': {
           "init_command": "SET storage_engine=MyISAM",
        }
    }
}
