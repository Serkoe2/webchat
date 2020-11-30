import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = 'z5u)%2*k8#3ede28d2*&s_4ny_)ro8*58g1%@vzcl'
DEBUG = False

#STATIC_DIR = os.path.join(BASE_DIR , 'static')
#STATICFILES_DIRS = [STATIC_DIR]
#STATIC_ROOT = os.path.join(BASE_DIR, 'static')

ALLOWED_HOSTS = ['127.0.0.1' , '194.58.108.67']


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'app',
        'USER' : 'postgres',
        'PASSWORD': 'q',
        'HOST' : 'localhost',
        'PORT' : '5432',
    }
}


sudo nano /etc/nginx/sites-available/default
sudo nano /var/log/nginx/error.log
sudo nano ~/webchat/logs/debug.txt

sudo supervisorctl restart webchat
sudo systemctl restart nginx

app_user Qwerty


a3d31