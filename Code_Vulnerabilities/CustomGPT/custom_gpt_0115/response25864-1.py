
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',  # or your database of choice
        'NAME': BASE_DIR / "db1.sqlite3",  # DB1
    },
    'db2': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / "db2.sqlite3",  # DB2
    },
}
