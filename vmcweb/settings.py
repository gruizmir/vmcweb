# -*- coding: utf-8 -*-
u"""
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
LOCAL_DEPLOY = CONFIG.get('local_deploy', True)

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django_gulp',
    'django.contrib.staticfiles',
    'ckeditor',
    'main',
    'rest_framework',
    'rest_framework.authtoken',
    'debug_toolbar',
    'corsheaders',
    'storages',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
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

CORS_ORIGIN_ALLOW_ALL = True

AWS_CONFIGS = CONFIG.get('aws', {})

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

#STATIC_URL = '/static/'
#STATIC_ROOT = os.path.join(BASE_DIR, 'vmcweb/static')

if LOCAL_DEPLOY:
    STATIC_URL = '/static/'
    STATIC_ROOT = os.path.join(BASE_DIR, 'vmcweb/static')

    MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
    MEDIA_URL = '/media/'
else:
    # Serving static files from AWS S3.
    # Boto: Include this headers in the response when serving from S3
    AWS_HEADERS = {
        'Expires': '7d',
        'Cache-Control': 'max-age=604800',
    }
    AWS_STORAGE_BUCKET_NAME = AWS_CONFIGS.get('static_bucket_name', '')
    AWS_MEDIA_BUCKET_NAME = AWS_CONFIGS.get('media_bucket_name', '')
    AWS_ACCESS_KEY_ID = AWS_CONFIGS.get('access_key_id', '')
    AWS_SECRET_ACCESS_KEY = AWS_CONFIGS.get('secret_access_key', '')

    # Tell django-storages that when coming up with the URL for an item in S3
    # storage, keep it simple - just use this domain plus the path. (If this
    # isn't set, things get complicated).
    # This controls how the `static` template tag from `staticfiles` gets
    # expanded, if you're using it. We also use it in the next setting.

    AWS_S3_CUSTOM_DOMAIN = AWS_CONFIGS.get('static_service_domain',
                            '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME)

    # This is used by the `static` template tag from `static`, if you're
    # using that. Or if anything else refers directly to STATIC_URL. So it's
    # safest to always set it.
    STATIC_ROOT = 'staticfiles'

    # Tell the staticfiles app to use S3Boto storage when writing the collected
    # static files (when you run `collectstatic`).
    STATICFILES_LOCATION = 'static'
    STATICFILES_STORAGE = 'main.custom_storages.StaticStorage'
    STATIC_URL = "https://%s/" % (AWS_S3_CUSTOM_DOMAIN)
    STATIC_DIRECTORY = '/static/'

    AWS_S3_MEDIA_DOMAIN = '%s.s3.amazonaws.com' % AWS_MEDIA_BUCKET_NAME
    MEDIA_URL = "https://%s/" % (AWS_S3_MEDIA_DOMAIN)
    MEDIA_ROOT = MEDIA_URL
    DEFAULT_FILE_STORAGE = 'main.custom_storages.MediaStorage'


TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'templates'),
)

# Communication systems
EMAIL_CONFIGS = CONFIG.get('email', {}).get('smtp', {})
EMAIL_USE_TLS = EMAIL_CONFIGS.get('use_tls', True)
EMAIL_HOST = EMAIL_CONFIGS.get('host', '')
EMAIL_HOST_USER = EMAIL_CONFIGS.get('user', '')
EMAIL_HOST_PASSWORD = EMAIL_CONFIGS.get('password', '')
EMAIL_PORT = EMAIL_CONFIGS.get('port', 587)
DEFAULT_FROM_EMAIL = CONFIG.get('email', {}).get('default_from', '')
CONTACT_EMAIL = DEFAULT_FROM_EMAIL
COMMUNICATIONS_EMAIL_SUBJECT_PREFIX = u'[VMC-2016]'
AWS_CONFIGS = CONFIG.get('aws', {})

MAX_THUMBNAIL_SIZE = 250
MAX_PHOTO_SIZE = 500
MAX_LOGO_SIZE = 500
MAX_ARTICLE_IMAGE_SIZE = 700
