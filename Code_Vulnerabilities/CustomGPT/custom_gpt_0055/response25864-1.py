
# settings.py
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / "db.sqlite3",
    },
    'DB1': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'database1',
        'USER': 'user1',
        'PASSWORD': 'password1',
        'HOST': 'localhost',
        'PORT': '5432',
    },
    'DB2': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'database2',
        'USER': 'user2',
        'PASSWORD': 'password2',
        'HOST': 'localhost',
        'PORT': '5432',
    },
}
