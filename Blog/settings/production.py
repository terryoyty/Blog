from .common import *

DATABASES = {
    # 'default': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    # },
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'blog',
        'USER': 'root',
        'PASSWORD': 'TerryMysql123!@#',
        'HOST': 'mysql',
        'PORT': '3306',
    }

}

HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'app.elasticsearch2_ik_backend.Elasticsearch2IkSearchEngine',
        'URL': 'http://elasticsearch:9200/',
        'INDEX_NAME': 'blog',
    },
}

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ['DJANGO_SECRET_KEY']

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# ALLOWED_HOSTS = ['127.0.0.1', 'www.terryoyty.com']
# ALLOWED_HOSTS = ['www.terryoyty.cn', '43.143.242.93']
ALLOWED_HOSTS = ['www.terryoyty.bj.cn', '120.46.44.197']

QNY_UPLOAD_URL = 'https://qnycdn.terryoyty.bj.cn/'
