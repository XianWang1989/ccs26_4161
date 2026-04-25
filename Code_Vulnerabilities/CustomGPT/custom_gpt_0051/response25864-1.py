
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    },
    'DB1': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'db1_name',
        'USER': 'user1',
        'PASSWORD': 'password1',
        'HOST': 'localhost',
        'PORT': '5432',
    },
    'DB2': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'db2_name',
        'USER': 'user2',
        'PASSWORD': 'password2',
        'HOST': 'localhost',
        'PORT': '5432',
    },
}
