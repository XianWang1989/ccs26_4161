
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',  # Example: Use sqlite3 or other database engines
        'NAME': BASE_DIR / "db1.sqlite3",  # DB1
    },
    'db2': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / "db2.sqlite3",  # DB2
    },
}
