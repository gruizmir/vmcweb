# -*- coding: utf-8 -*-
"""
Django settings for vmcweb project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

try:
    import secrets
    CONFIG = secrets.CONFIG
except:
    CONFIG = {}


ADMIN_CONFIGS = CONFIG.get('administration', {})
ADMINS = ADMIN_CONFIGS.get('admins', ())

BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = CONFIG.get('secret_key', {})

DEBUG = CONFIG.get('debug', True)
TEMPLATE_DEBUG = DEBUG
ALLOWED_HOSTS = CONFIG.get('allowed_hosts', [])
BASE_URL = CONFIG.get('base_url', 'http://localhost:8000')

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'main',
    'rest_framework',
    'rest_framework.authtoken',
    'debug_toolbar'
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'vmcweb.urls'

WSGI_APPLICATION = 'vmcweb.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases
DB_CONFIG = CONFIG.get('databases', {})
DB_DEFAULT = DB_CONFIG.get('default', {})

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': DB_DEFAULT.get('name', ''),
        'USER': DB_DEFAULT.get('user', ''),
        'PASSWORD': DB_DEFAULT.get('password', ''),
        'HOST': DB_DEFAULT.get('host', ''),
        'PORT': DB_DEFAULT.get('port', '3306')
    },
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'es-cl'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'templates'),
)

DEFAULT_FROM_EMAIL = 'valpo.mobile.conf@gmail.com'

MAX_THUMBNAIL_SIZE = 150

EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.sendgrid.net'
EMAIL_HOST_USER = 'valpomobileconf'
EMAIL_HOST_PASSWORD = 'kenolamasca2veces'
EMAIL_PORT = 587

# Communication systems
EMAIL_CONFIGS = CONFIG.get('email', {}).get('smtp', {})
EMAIL_USE_TLS = EMAIL_CONFIGS.get('use_tls', True)
EMAIL_HOST = EMAIL_CONFIGS.get('host', '')
EMAIL_HOST_USER = EMAIL_CONFIGS.get('user', '')
EMAIL_HOST_PASSWORD = EMAIL_CONFIGS.get('password', '')
EMAIL_PORT = EMAIL_CONFIGS.get('port', 587)

DEFAULT_FROM_EMAIL = u'Valparaíso Mobile Conf<valpo.mobile.conf@gmail.com>'
CONTACT_EMAIL = 'valpo.mobile.conf@gmail.com'
COMMUNICATIONS_EMAIL_SUBJECT_PREFIX = u'[VMC-2016]'