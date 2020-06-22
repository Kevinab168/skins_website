DEBUG = True

SECRET_KEY = 'Secret'

ROOT_URLCONF = 'urls'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'counter.db',
    }
}


INSTALLED_APPS = [
    'counter'
]

STATIC_URL = '/static/'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'APP_DIRS': True,
    }
]
