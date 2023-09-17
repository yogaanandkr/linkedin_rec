"""
Django settings for linkedin_recommendations project.

Generated by 'django-admin startproject' using Django 4.2.4.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-p4racoxi#8m2*y4wq87i9#y$^h*vw2uz420=t$j57w63c#jiep'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

SITE_ID = 4# TO MENTION WHICH SITE WE ARE USING FOR LOGIN

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'users',
    'django.contrib.sites',  #  allows you to associate your Django project with multiple sites
    'allauth', #'allauth' and 'allauth.account':  are used to implement user authentication and registration systems with features like email confirmation, password reset, and more. They are highly customizable and provide a solid foundation for user management.
    'allauth.account',
    'allauth.socialaccount', # 'allauth.socialaccount' extends 'allauth' to enable social authentication, making it easy for users to sign in with their social media accounts.
    'allauth.socialaccount.providers.google' #is a specific provider package that adds Google authentication to your site. By integrating it, you allow users to sign in or register using their Google credentials.
]
import os
SOCIALACCOUNT_PROVIDERS = {
	"google":{
        # "APP": {
        #     "client_id": os.getenv("684025040233-l6elp5tarpck4bnu0moik18va80h79ij.apps.googleusercontent.com"),
        #     "secret": os.getenv("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"),
        #     "key": ""
        # },
        "SCOPE":[
            "profile",
            "email"
        ],
        "AUTH_PARAMS": {
        "access_type": "online"
        },
	}
}



MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'linkedin_recommendations.urls'

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
            ],
        },
    },
]

WSGI_APPLICATION = 'linkedin_recommendations.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


AUTHENTICATION_BACKENDS = ( # here we are specifying that we are using both  the django backend and allauth backends
    "django.contrib.auth.backends.ModelBackend",
    "allauth.account.auth_backends.AuthenticationBackend"
)

LOGIN_REDIRECT_URL = "/"
LOGOUT_REDIRECT_URL = "/"


MEDIA_ROOT = BASE_DIR / "uploads"
MEDIA_URL = "/files/"



DATETIME_FORMAT = 'd-m-y'