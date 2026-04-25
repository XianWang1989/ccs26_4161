
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',  # Default database for fallback
    },
    'db1': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'DB1',
        'USER': 'your_user',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '5432',
    },
    'db2': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'DB2',
        'USER': 'your_user',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '5432',
    },
}
