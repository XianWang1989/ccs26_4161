
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / "db.sqlite3",
    },
    'DB1': {
        'ENGINE': 'django.db.backends.postgresql',  # Example for PostgreSQL
        'NAME': 'db1_name',
        'USER': 'username1',
        'PASSWORD': 'password1',
        'HOST': 'localhost',
        'PORT': '5432',
    },
    'DB2': {
        'ENGINE': 'django.db.backends.postgresql',  # Example for PostgreSQL
        'NAME': 'db2_name',
        'USER': 'username2',
        'PASSWORD': 'password2',
        'HOST': 'localhost',
        'PORT': '5432',
    },
}
