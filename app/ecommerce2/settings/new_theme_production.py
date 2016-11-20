"""
Django settings for ecommerce2 project.

Generated by 'django-admin startproject' using Django 1.8.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
from django.core.exceptions import ImproperlyConfigured


def get_env_variable(var_name):
    print("bu fonk çalışmalı")
    """Get the environment variable or return exception."""
    try:
        return os.environ[var_name]
    except KeyError:
        error_msg = "Set the {} environment variable".format(var_name)
        raise ImproperlyConfigured(error_msg)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# root of project

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('SECRET_KEY')
print("the fucking secret_key is:", SECRET_KEY)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.getenv('DEBUG')
print("the fucking DEBUG setting is:", DEBUG)

ALLOWED_HOSTS = ["istebu.com", "139.59.139.108", "192.168.99.100"]

# EMAIL_HOST = os.environ["EMAIL_HOST"] # bu kesinlikle çalışmıyor.
EMAIL_HOST = os.getenv('EMAIL_HOST')  # bu çalıştı sanki.
# EMAIL_HOST = os.environ.get('EMAIL_HOST') # yukarıdaki çalışınca bunun çalışıp çalışmadığını denemedim.
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')
EMAIL_PORT = os.getenv('EMAIL_PORT')
EMAIL_USE_TLS = os.getenv('EMAIL_USE_TLS')

'''
If using gmail, you will need to
unlock Captcha to enable Django
to  send for you:
https://accounts.google.com/displayunlockcaptcha
'''

# Application definition

INSTALLED_APPS = (
    # django app
    'suit',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # third party apps
    'crispy_forms',
    'django_filters',
    'registration',
    'taggit',
    'tinymce',
    'data_importer',

    # my apps
    'analytics',
    'blog',
    'carts',
    'importer',
    'newsletter',
    'orders',
    'products',
    'static_pages',
    'visual_site_elements',

)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',

)

ROOT_URLCONF = 'ecommerce2.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, "templates_for_new_theme")],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [

                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.core.context_processors.request',
            ],
        },
    },
]

WSGI_APPLICATION = 'ecommerce2.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.getenv('DB_NAME'),
        'USER': os.getenv('DB_USER'),
        'PASSWORD': os.getenv('DB_PASS'),
        'HOST': os.getenv('DB_SERVICE'),
        'PORT': os.getenv('DB_PORT'),
    },
}
# DB_NAME=istebu
# DB_USER=istebu_pg_user
# DB_PASS=5o($rt6ozh7u+ui9zb
# DB_SERVICE=postgres
# DB_PORT=5432

# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'tr_TR'

TIME_ZONE = 'Europe/Istanbul'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# eğer bunu pickle yapmazsan patlıyor :
# http://stackoverflow.com/questions/24229397/django-object-is-not-json-serializable-error-after-upgrading-django-to-1-6-5
SESSION_SERIALIZER = 'django.contrib.sessions.serializers.PickleSerializer'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR), "static_in_env", "static_root")

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static_in_pro", "static_for_new_theme"),
    # os.path.join(BASE_DIR, "static_in_env"),
    # '/var/www/static/',
)

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(os.path.dirname(BASE_DIR), "static_in_env", "media_root")

# Crispy FORM TAGs SETTINGS
CRISPY_TEMPLATE_PACK = 'bootstrap3'

# DJANGO REGISTRATION REDUX SETTINGS
ACCOUNT_ACTIVATION_DAYS = 7
REGISTRATION_AUTO_LOGIN = True
SITE_ID = 2
LOGIN_REDIRECT_URL = '/'

# Braintree Payments Details
BRAINTREE_PUBLIC = "qn3p5n7njksw47r3"
BRAINTREE_PRIVATE = "d14ac944794c0df1c81991ecf49221ff"
BRAINTREE_MERCHANT_ID = "n84nynknvzz3j3sz"
BRAINTREE_ENVIRONEMNT = "Sandbox"