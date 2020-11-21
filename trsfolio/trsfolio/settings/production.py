from trsfolio.settings.base import *

with open('/etc/secret_key.txt') as f:
    SECRET_KEY = f.read().strip()

DEBUG = False

ALLOWED_HOSTS = ['hugotrs.com', '68.183.46.49']

with open('/etc/postgres_password.txt') as f:
    postgres_pwd = f.read().strip()

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'trsfolio',
        'USER': 'trs',
        'PASSWORD': postgres_pwd,
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static/')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')

# Email
with open('/etc/email_password.txt') as f:
    EMAIL_HOST_PASSWORD = f.read().strip()

EMAIL_HOST = 'smtp.ionos.mx'
EMAIL_HOST_USER = 'spam@hugotrs.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = 'spam@hugotrs.com'