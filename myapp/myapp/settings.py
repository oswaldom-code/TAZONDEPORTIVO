from pathlib import Path
import os
import environ
import dj_database_url 


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/


env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False)
)

# Take environment variables from .env file
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

if DEBUG is True:
    ALLOWED_HOSTS = ['127.0.0.1:8000', '*']

if DEBUG is False:
    ALLOWED_HOSTS = ['tazon-deportivo.herokuapp.com']

# Application definition

INSTALLED_APPS = [
    'admin_interface',  #   Necesario para personalizar el admin
    'colorfield',  #   Necesario para personalizar el admin
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'import_export',  # Importar y exportar datos
    'ckeditor',  # Editor de texto
    'apps.blog'
]

X_FRAME_OPTIONS = 'SAMEORIGIN'  # Necesario para personalizar el admin

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'myapp.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media',
            ],
        },
    },
]

WSGI_APPLICATION = 'myapp.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases
if DEBUG is True:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'USER':  env('DB_USER'),
            'PASSWORD':  env('DB_PASSWORD'),
            'NAME':  env('DB_NAME'),
            'HOST':  env('DB_HOST'),
            'PORT':  env('DB_PORT'),
        }
    }
if DEBUG is False:
    db_from_env = dj_database_url.config(conn_max_age=500)  
    DATABASES['default'].update(db_from_env)

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME':
        'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME':
        'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME':
        'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME':
        'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

## Custon CKEDITOR
CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'full',
    },
}

# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'es-Es'

TIME_ZONE = 'UTC'

USE_I18N = True  # Django debe activar la traducción

USE_L10N = True

USE_TZ = True

STATIC_URL = '/static/'

#Base url to serve media files
MEDIA_URL = '/media/'

# Path where media is stored, upload users file
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')

# Static files (CSS, JavaScript, Images)


STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

STATIC_ROOT = os.path.join(BASE_DIR, 'static')

MIDDLEWARE_CLASSES = (
    # Simplified static file serving.
    # https://warehouse.python.org/project/whitenoise/ 
    'whitenoise.middleware.WhiteNoiseMiddleware',)

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
