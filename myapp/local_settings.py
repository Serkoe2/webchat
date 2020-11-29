import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = 'z5u)%2*k8#3ede28d2*&s_4ny_)ro8*58g1%@vzcl'
DEBUG = True

#STATIC_DIR = os.path.join(BASE_DIR , 'static')
STATICFILES_DIRS = [os.path.join(BASE_DIR , 'static')]
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
#STATIC_ROOT = os.path.join(BASE_DIR, 'static')

ALLOWED_HOSTS = ['127.0.0.1' ,]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'webchat',
        'USER' : 'postgres',
        'PASSWORD': 'q',
        'HOST' : 'localhost',
        'PORT' : '5432',
    }
}
