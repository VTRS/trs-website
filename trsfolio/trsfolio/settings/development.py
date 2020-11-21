from trsfolio.settings.base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '($rng7_zh-w#c5lgfkzes&y+2&vwlc-plb0a@p@8z1e0f32o1b'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

DEBUG = True

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'trsfolio',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}
# Email
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'