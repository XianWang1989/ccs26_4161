
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    },
    'db1': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'DB1',
        'USER': 'user1',
        'PASSWORD': 'password1',
        'HOST': 'localhost',
        'PORT': '5432',
    },
    'db2': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'DB2',
        'USER': 'user2',
        'PASSWORD': 'password2',
        'HOST': 'localhost',
        'PORT': '5432',
    },
}
