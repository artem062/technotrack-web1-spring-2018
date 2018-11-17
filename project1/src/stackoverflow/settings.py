"""
Django settings for stackoverflow project.

Generated by 'django-admin startproject' using Django 1.11.11.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os
import sys
import storages

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'a)116tm#wao(5&v(3gnc-!klqzgk%3c5s12u!*)8k((krwni&p'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # 'debug_toolbar',
    'core.apps.CoreConfig',
    'categories.apps.CategoriesConfig',
    'questions.apps.QuestionsConfig',
    'likes.apps.LikesConfig',
    'crispy_forms',
    'social_django',
    'adjacent',
]

AUTH_USER_MODEL = 'core.User'

MIDDLEWARE = [
    # 'debug_toolbar.middleware.DebugToolbarMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django_cprofile_middleware.middleware.ProfilerMiddleware',
]

ROOT_URLCONF = 'stackoverflow.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'core.context_data.stats',
                'social_django.context_processors.backends',
            ],
        },
    },
]

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11211',
    }
}

WSGI_APPLICATION = 'stackoverflow.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'DB1',
        'USER': 'artem',
        'PASSWORD': '761804',
        'HOST': 'localhost',
        # 'NAME': os.environ.get('DB_NAME'),
        # 'USER': os.environ.get('DB_USER'),
        # 'PASSWORD': os.environ.get('DB_PASSWORD'),
        # 'HOST': os.environ.get('DB_HOST')
    }
}

# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'

INTERNAL_IPS = ['127.0.0.1', ]

LOGIN_URL = 'core:login'

LOGOUT_URL = 'core:logout'

REGISTER_URL = 'core:register'

LOGIN_REDIRECT_URL = 'core:profile'

CRISPY_TEMPLATE_PACK = 'bootstrap4'

DEFAULT_FILE_STORAGE = 'django.core.files.storage.FileSystemStorage'
# STATICFILES_STORAGE = 'django.core.files.storage.FileSystemStorage'
# DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
# STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

# AWS_S3_ENDPOINT_URL = 'https://hb.bizmrg.com'
# AWS_ACCESS_KEY_ID = 'kzABZBUVnpuDqiYd5BPMHA'
# AWS_SECRET_ACCESS_KEY = 'bDt94aBqJWq5P91vBm9bowxoupWt3V8x3PaGGSVkYQBG'
# AWS_STORAGE_BUCKET_NAME = 'backend'

# MEDIA_ROOT = os.path.join(BASE_DIR, 'storage', 'media')
# MEDIA_URL = '/media/'

STATIC_ROOT = os.path.join(BASE_DIR, 'storage', 'static')
# STATIC_URL = '/static/'
# STATICFILES_DIRS = ('core/static', )

TESTING = 'test' in sys.argv

if TESTING:
    DATABASES['default'] = {'ENGINE': 'django.db.backends.sqlite3'}
    DEFAULT_FILE_STORAGE = 'django.core.files.storage.FileSystemStorage'
    STATICFILES_STORAGE = 'django.core.files.storage.FileSystemStorage'


AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'social_core.backends.vk.VKOAuth2',
    'social_core.backends.github.GithubOAuth2',
    'social_core.backends.facebook.FacebookOAuth2',
)
LOGIN_REDIRECT_URL = '/'

SOCIAL_AUTH_VK_OAUTH2_KEY = '6723064'
SOCIAL_AUTH_VK_OAUTH2_SECRET = 'ssoDAfPrTo5OFRczveia'
SOCIAL_AUTH_VK_OAUTH2_SCOPE = ['email']


SOCIAL_AUTH_GITHUB_KEY = '40ce80326df20f71400e'
SOCIAL_AUTH_GITHUB_SECRET = '7d2abcf0928d630409075ac2d11e898ca3f413b2'
SOCIAL_AUTH_GITHUB_SCOPE = ['email']

SOCIAL_AUTH_FACEBOOK_KEY = '476705162821154'
SOCIAL_AUTH_FACEBOOK_SECRET = 'fa3fc8f85a8f15b3459d5b635fe62c39'
SOCIAL_AUTH_FACEBOOK_SCOPE = ['email']

CENTRIFUGE_ADDRESS = 'http://localhost:8080'
CENTRIFUGE_SECRET = 'c74900d9-462a-4244-80ef-8c30ec8692ad'
CENTRIFUGE_TIMEOUT = 10
