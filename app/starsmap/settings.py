import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

app_stage = os.environ.get('APP_STAGE', 'dev')

SECRET_KEY = os.environ.get('SECRET_KEY', 'secret')

if app_stage == 'prod':
    DEBUG = False
else:
    DEBUG = True

ALLOWED_HOSTS = ['starsmap.ddns.net', '127.0.0.1', 'localhost']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'django_filters',
    'corsheaders',
    'employee.apps.EmployeeConfig',
    'homepage.apps.HomepageConfig',
    'rating.apps.RatingConfig',
    'about.apps.AboutConfig',
    'api.apps.ApiConfig',
    'drf_yasg',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'starsmap.urls'

TEMPLATES_DIR = BASE_DIR / 'templates'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATES_DIR],
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

WSGI_APPLICATION = 'starsmap.wsgi.application'


# Database

if app_stage == 'dev':
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }
elif app_stage == 'prod':
    DATABASES = {
        'default': {
            'ENGINE': os.getenv('DB_ENGINE',
                                default='django.db.backends.postgresql_psycopg2'),
            'NAME': os.getenv('DB_NAME', default='database'),
            'USER': os.getenv('POSTGRES_USER', default='postgres'),
            'PASSWORD': os.getenv('POSTGRES_PASSWORD', default='postgres'),
            'HOST': os.getenv('DB_HOST', default='db'),
            'PORT': os.getenv('DB_PORT', default=5432)
        }
    }

# Password validation

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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Europe/Moscow'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)

STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

STATICFILES_DIRS = [
    BASE_DIR / 'static_dev',
]

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# Custom settings
AUTH_USER_MODEL = 'employee.User'

SWAGGER_SETTINGS = {
    'SECURITY_DEFINITIONS': {
        'Bearer': {
            'type': 'apiKey',
            'name': 'Authorization',
            'in': 'header'
        }
    },
    'DEFAULT_API_URL': 'https://starsmap.ddns.net'
}

CORS_ORIGIN_ALLOW_ALL = True
CORS_URLS_REGEX = r'^/api/.*$'
CORS_ALLOWED_ORIGINS = [
    'http://localhost:3000',
    'https://rosbank-kappa.vercel.app',
    'http://localhost:8000',
    'http://127.0.0.1:8000',
]

PERSONAL_ACCOUNT_URL_NAME = 'me'

CSRF_TRUSTED_ORIGINS = [
    'https://starsmap.ddns.net',
    'http://127.0.0.1',
]

ADMINS = [
    ['admin', 'service@example.com']
]
