"""
Django settings for mvm project.

Generated by 'django-admin startproject' using Django 4.0.10.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

import json
import locale
import os, certifi
from pathlib import Path

import django_heroku
import dj_database_url

os.environ["SSL_CERT_FILE"] = certifi.where()

# Build paths inside the project like this: BASE_DIR / "subdir".
BASE_DIR = Path(__file__).resolve().parent.parent


BASE_PATHS = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

LOCALE_PATHS = [
    os.path.join(BASE_PATHS, 'apps', 'authentication', 'locale'),
    os.path.join(BASE_PATHS, 'apps', 'general', 'locale'),
    os.path.join(BASE_PATHS, 'apps', 'travel', 'locale'),
]

SECRETS = {}

environ_variable_list = list(os.environ)
if "MVM_APP_SECRET_KEY" in environ_variable_list:
    for environ_variable in environ_variable_list:
        if environ_variable.startswith("MVM_APP_"):
            if environ_variable in [
                "MVM_APP_ALLOWED_HOSTS",
                "MVM_APP_CSRF_TRUSTED_ORIGINS",
            ]:
                SECRETS[environ_variable] = os.environ.get(environ_variable, "").split(",")
            else:
                SECRETS[environ_variable] = os.environ.get(environ_variable)
else:
    try:
        with Path(BASE_DIR).joinpath("secrets.json").open() as handle:
            SECRETS = json.load(handle)
    except OSError:
        SECRETS = {
            "MVM_APP_SECRET_KEY": "",
            "MVM_APP_ALLOWED_HOSTS": [],
            "MVM_APP_CSRF_TRUSTED_ORIGINS": [],
            "MVM_APP_DEBUG": True,
            "MVM_APP_DATABASES_DEFAULT_NAME": "",
            "MVM_APP_DATABASES_DEFAULT_USER": "",
            "MVM_APP_DATABASES_DEFAULT_PASSWORD": "",
            "MVM_APP_DATABASES_DEFAULT_HOST": "",
            "MVM_APP_DATABASES_DEFAULT_PORT": 5432
        }


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = SECRETS["MVM_APP_SECRET_KEY"]

# SECURITY WARNING: don"t run with debug turned on in production!
DEBUG = SECRETS["MVM_APP_DEBUG"]

ALLOWED_HOSTS = SECRETS["MVM_APP_ALLOWED_HOSTS"]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

INSTALLED_APPS_MVM = [
    "apps.authentication",
    "apps.general",
    "apps.travel",
]

INSTALLED_APPS_THIRD_PARTY = [
    "django_ses",
    "dj_rest_auth",
    "dj_rest_auth.registration",
    "rest_framework.authtoken",
    "spectrum",
    "django_better_admin_arrayfield",
    "django_jsonform",
    "whitenoise.runserver_nostatic",
]

INSTALLED_APPS += INSTALLED_APPS_MVM + INSTALLED_APPS_THIRD_PARTY

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    "whitenoise.middleware.WhiteNoiseMiddleware",
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.locale.LocaleMiddleware',
]

ROOT_URLCONF = 'mvm.urls'

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "mvm.wsgi.application"
ASGI_APPLICATION = "mvm.asgi.application"

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "dj_db_conn_pool.backends.postgresql",
        "NAME": str(SECRETS["MVM_APP_DATABASES_DEFAULT_NAME"]),
        "USER": str(SECRETS["MVM_APP_DATABASES_DEFAULT_USER"]),
        "PASSWORD": str(SECRETS["MVM_APP_DATABASES_DEFAULT_PASSWORD"]),
        "HOST": str(SECRETS["MVM_APP_DATABASES_DEFAULT_HOST"]),
        "PORT": str(SECRETS["MVM_APP_DATABASES_DEFAULT_PORT"]),
    }
}

# AUTHENTICATION

AUTH_USER_MODEL = "authentication.User"

LOGIN_URL = "/auth/login/"

LOGIN_REDIRECT_URL = ""

LOGOUT_REDIRECT_URL = None

# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/
try:
    locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')
except locale.Error:
    locale.setlocale(locale.LC_TIME, 'C')


LANGUAGE_CODE = 'es'

LANGUAGES = [
    ('es', 'Spanish'),
]

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/


STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

STATICFILES_DIRS = [
    BASE_DIR / "static",
]
STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(BASE_DIR, 'static_root')
django_heroku.settings(locals())

# Media

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = str(SECRETS["MVM_APP_FROM_EMAIL"])
EMAIL_HOST_PASSWORD = str(SECRETS["MVM_APP_EMAIL_PASSWORD"])
EMAIL_SSL_NO_VERIFY = True
