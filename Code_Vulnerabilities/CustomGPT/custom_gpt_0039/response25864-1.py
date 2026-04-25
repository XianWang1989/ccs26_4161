
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', # Example using SQLite
        'NAME': BASE_DIR / 'db1.sqlite3',
    },
    'db2': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db2.sqlite3',
    },
}
