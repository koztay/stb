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
import environ  # bu çalışırsa yukarıdaki gibi os.getenv kullanımından vazgeçebiliriz.

env = environ.Env()
env.read_env()
# print("I am printing the env.read_env", env.read_env())

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print("base_dir : ", BASE_DIR)
# root of project where manage.py located.

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('DJANGO_SECRET_KEY', default='#rw*tsqd36o=78ydz*lv_v2kkzo_5e8gpid512bnx@it0#a9*c')

print("the fucking secret_key is:", SECRET_KEY)

# DEBUG
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#debug
DEBUG = env.bool('DJANGO_DEBUG', True)
print("the fucking DEBUG setting is:", DEBUG)


# ALLOWED_HOSTS = ["139.59.139.108", "192.168.99.101", "istebu.com", "www.example.com", ]
ALLOWED_HOSTS = env.list('DJANGO_ALLOWED_HOSTS', default=('istebu.com',))
# print("ALLOWED_HOSTS neymiş bakalım görelim niye set edemiyoruz? =>", ALLOWED_HOSTS)
# ALLOWED_HOSTS = ('*',)  # bu değeri enviroment variable olarak girince şuna dikkat etmek gerek:
# Bu parameteryi girerken IP adreslerini tırnak için alma ve virgülle ayırdığın değerlerin arasına
# space ile boşluk koyma.


# EMAIL_HOST = os.environ["EMAIL_HOST"] # bu kesinlikle çalışmıyor.
# EMAIL_HOST = os.getenv('EMAIL_HOST')  # bu çalıştı sanki.
# # EMAIL_HOST = os.environ.get('EMAIL_HOST') # yukarıdaki çalışınca bunun çalışıp çalışmadığını denemedim.
# EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')
# EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')
# EMAIL_PORT = os.getenv('EMAIL_PORT')
# EMAIL_USE_TLS = os.getenv('EMAIL_USE_TLS')

'''
If using gmail, you will need to
unlock Captcha to enable Django
to  send for you:
https://accounts.google.com/displayunlockcaptcha
'''

# Application definition

INSTALLED_APPS = (

    # django core apps
    'suit',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.flatpages',

    # third party apps
    'crispy_forms',
    'data_importer',
    'django_celery_beat',
    'django_celery_results',
    'django_filters',
    'registration',
    'taggit',
    'tinymce',


    # my apps
    'analytics',
    'blog',
    'carts',
    'importer',
    'newsletter',
    'orders',
    'products',
    'vendors',
    'visual_site_elements',

)

# Mail settings
# ------------------------------------------------------------------------------
EMAIL_PORT = 1025
EMAIL_HOST = env("EMAIL_HOST", default='mailhog')
DEFAULT_FROM_EMAIL = env('DJANGO_DEFAULT_FROM_EMAIL',
                         default='istebu <noreply@istebu.com>')
EMAIL_SUBJECT_PREFIX = env('DJANGO_EMAIL_SUBJECT_PREFIX', default='[istebu]')
SERVER_EMAIL = env('DJANGO_SERVER_EMAIL', default=DEFAULT_FROM_EMAIL)

# Anymail with Mailgun
INSTALLED_APPS += ("anymail", )
ANYMAIL = {
    "MAILGUN_API_KEY": env('DJANGO_MAILGUN_API_KEY', default='test_api_key'),
    "MAILGUN_SENDER_DOMAIN": env('MAILGUN_SENDER_DOMAIN', default='test_snder_domain')
}
# yukarıda default değerleri yazmamız gerek. Aksi taktirde ilk önce okumaya çalışıp crash oluyor,
# sonrasında ise docker environment değerlerini set ediyor ve değerler update oluyor.

EMAIL_BACKEND = "anymail.backends.mailgun.MailgunBackend"

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

# Yine benzer şekilde aşağıya default değerleri yazmazsak docker henüz bu environment
# variables değerlerini set edemediği için crash kaçınıömaz oluyor.
DATABASES = {
    'default': {
        'ENGINE': env('DB_ENGINE', default='django.db.backends.sqlite3'),
        'NAME': env('DB_NAME', default='default_database'),
        'USER': env('DB_USER', default='default_user'),
        'PASSWORD': env('DB_PASS', default='default_password'),
        'HOST': env('DB_SERVICE', default='localhost'),
        'PORT': env('DB_PORT', default='1234'),
    },
}

print (DATABASES)

# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'tr_TR'

TIME_ZONE = 'Europe/Istanbul'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# eğer bunu pickle yapmazsan patlıyor:
# http://stackoverflow.com/questions/24229397/django-object-is-not-json-serializable-error-after-upgrading-django-to-1-6-5
SESSION_SERIALIZER = 'django.contrib.sessions.serializers.PickleSerializer'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR), "static_in_env", "static_root")
print("STATIC_ROOT : ", STATIC_ROOT)

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
SITE_ID = 1
LOGIN_REDIRECT_URL = '/'

# django-import-export setting
IMPORT_EXPORT_USE_TRANSACTIONS = True

# celery settings
CELERY_BROKER_URL = os.getenv('CELERY_BROKER_URL')
CELERY_RESULT_BACKEND = 'django-db'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'  # pickle yapmazsak importer çalışmıyor, json yapmazsak da kur çekme çalışmıyor.
CELERY_RESULT_SERIALIZER = 'json'  # pickle yapmazsak importer çalışmıyor, json yapmazsak da kur çekme çalışmıyor.
CELERY_TIMEZONE = TIME_ZONE


# Paynet etc. payment gateway settings will be here
PAYNET_PUBLISHABLE_KEY = env('PAYNET_PUBLISHABLE_KEY', default='string for prevent crash building docker')
PAYNET_SECRET_KEY = env('PAYNET_SECRET_KEY', default='string for prevent crash building docker')
PAYNET_TEST_API_URL = env('PAYNET_TEST_API_URL', default='string for prevent crash building docker')
PAYNET_TEST_PAYNETJS_URL = env('PAYNET_TEST_PAYNETJS_URL', default='string for prevent crash building docker')
PAYNET_PRODUCTION_API_URL = env('PAYNET_PRODUCTION_API_URL', default='string for prevent crash building docker')
PAYNET_PRODUCTION_PAYNETJS_URL = env('PAYNET_PRODUCTION_PAYNETJS_URL', default='string for prevent crash building docker')


# IMPORTER INDIRIM ORANI:
IMPORTER_SALE_PRICE_FACTOR = 1.05
