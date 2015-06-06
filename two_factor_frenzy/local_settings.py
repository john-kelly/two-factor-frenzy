"""Local Settings."""

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'local',
        'USER': 'postgres',
        'PASSWORD': '',
        'HOST': 'local:',
        'PORT': '5432',
    }
}
