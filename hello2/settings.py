"""
Django settings for Hello project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""
import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '^pof(fakcox5^bb5d1x^wuh@xk+0#o(a&yrz*_+of4pn50rl%+'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False
TEMPLATE_CONTEXT_PROCESSORS = ('django.core.context_processors.request',
                               'django.contrib.auth.context_processors.auth')
TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []
AUTH_USER_MODEL='user.MyUser'
# Application definition
INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'crispy_forms',
    'user',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'hello2.urls'
WSGI_APPLICATION = 'hello2.wsgi.application'
CRISPY_TEMPLATE_PACK = 'bootstrap3'
# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True
# Parse database configuration from $DATABASE_URL
import dj_database_url
DATABASES = {
    "default": dj_database_url.config(default='postgres://localhost'),
}
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': 'django',
#         'USER': 'postgres',
#         'PASSWORD': 'sasidhar',
#         'HOST': 'localhost',
#         'PORT': '5432',
#     }
# }
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }
# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
# Allow all host headers
ALLOWED_HOSTS = ['*']
# Static asset configuration
STATIC_URL = '/static/'
TEMPLATE_DIRS=(
    os.path.join(os.path.dirname(BASE_DIR),"sin","templates"),
)

STATIC_ROOT = os.path.join(BASE_DIR,'sin')

if DEBUG:
    # STATIC_ROOT=os.path.join(os.path.dirname(BASE_DIR),"static","static-only")
    # STATICFILES_DIRS=(
    #                   os.path.join(os.path.dirname(BASE_DIR),"static","static"),
    #                   )
    STATIC_ROOT='C:\\Users\\sapurana.FAREAST\\work\\arcanecove1279\\arcane-cove-1279\\sin'
    STATICFILES_DIRS= ( 'C:\\Users\\sapurana.FAREAST\\work\\arcanecove1279\\arcane-cove-1279\\sin\\css',)
