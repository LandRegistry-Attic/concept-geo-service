"""
Django settings for concept_geo_service project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

import dj_database_url

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY', '2ue!jv99=pf$=-4s=336sy%al+0@0*i1%ea&7@v9rlo-@^w2(r')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = (os.environ.get('DEBUG', 'True') == 'True')
TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = filter(None, os.environ.get('ALLOWED_HOSTS', '').split(','))


# Application definition

INSTALLED_APPS = (
    'django.contrib.contenttypes',
    'django.contrib.gis',
    'south',
    'concept_geo_service.titles'
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'concept_geo_service.urls'

WSGI_APPLICATION = 'concept_geo_service.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

# Fig
if 'GEODB_1_PORT_5432_TCP' in os.environ:
    DEFAULT_DATABASE = 'postgis://docker:docker@%s/geo' % os.environ['GEODB_1_PORT_5432_TCP'].replace('tcp://', '')
# Travis
else:
    DEFAULT_DATABASE = 'postgis:///geo'
DATABASES = {
    'default': dj_database_url.config(default=DEFAULT_DATABASE)
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'
