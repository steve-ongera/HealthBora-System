
from pathlib import Path
import os
import environ
# django-environ

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

### setting up env
env = environ.Env()

environ.Env.read_env(os.path.join(BASE_DIR, '.env'))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
#SECRET_KEY = env('SECRET_KEY')

SECRET_KEY = 'django-insecure-^3@#9g!@#e@1$%y5^q!m7b8_1^&w$s5@w6x*5v#4!h^+u!g9r'


# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = env('DEBUG')
DEBUG = True

ALLOWED_HOSTS = ['192.168.0.100', '127.0.0.1','5749-103-109-53-5.in.ngrok.io']
# ALLOWED_HOSTS = ['mobile view', 'local host','ngrok -- keeps on changing']

# Application definition
DEBUG_TOOLBAR = False


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'hospital.apps.HospitalConfig',
    'hospital_admin.apps.HospitalAdminConfig',
    'doctor.apps.DoctorConfig',
    'pharmacy.apps.PharmacyConfig',
    'sslcommerz.apps.SslcommerzConfig',
    'widget_tweaks',
    'rest_framework',
    'ChatApp.apps.ChatappConfig',
    
 

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    
]

INTERNAL_IPS = [
    "127.0.0.1",
]

ROOT_URLCONF = 'healthstack.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates')
        ],
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

WSGI_APPLICATION = 'healthstack.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Africa/Nairobi'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'
MEDIA_URL = '/images/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'static/images')

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]

### SSLCOMMERZ env variables
#VARIABLE should be in capital letter.
# STORE_ID = env('STORE_ID')
# STORE_PASSWORD = env('STORE_PASSWORD')
# STORE_NAME = env('STORE_NAME')

STORE_ID='38881818'
STORE_PASSWORD='cp7kvt2021'
STORE_NAME='jumia'

###Mailtrap env Variables
# SMTP_HOST = env('SMTP_HOST')
# SMTP_PORT = env('SMTP_PORT')
# SMTP_USER = env('SMTP_USER')
# SMTP_PASSWORD = env('SMTP_PASSWORD')

SMTP_HOST="smtp.mailtrap.io"
SMTP_PORT=587
SMTP_USER="1234567890abcdef " # Replace with your actual SMTP user
SMTP_PASSWORD="abcdef1234567890 " # Replace with your actual SMTP password

# EMAIL

# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST = 'smtp.mailtrap.io'
# EMAIL_PORT = SMTP_PORT
# EMAIL_HOST_USER = SMTP_USER
# EMAIL_HOST_PASSWORD = SMTP_PASSWORD
# EMAIL_USE_TLS = True
# EMAIL_USE_SSL = False



# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
AUTH_USER_MODEL = 'hospital.User'


# SESSION AGE 45 Minutes
SESSION_COOKIE_AGE = 45*60
SESSION_SAVE_EVERY_REQUEST = True