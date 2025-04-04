from .base import *

ALLOWED_HOSTS = ['52.79.152.19']
STATIC_ROOT = BASE_DIR / 'static/'
STATICFILES_DIRS = []
DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'pybo',
        'USER': 'dbmasteruser',
        'PASSWORD': '|EU0Xyce:Uvt*%]z$wLHXn+t`K?>>45A',
        'HOST': 'ls-ec4ed14b345ac1a2d7c87f9f8542f2356ada415e.cr2ic42mkx8y.ap-northeast-2.rds.amazonaws.com',
        'PORT': '5432',
    }
}