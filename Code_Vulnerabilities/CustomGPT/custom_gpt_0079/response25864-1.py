
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',  # Example: Use your own database engine
        'NAME': BASE_DIR / "db1.sqlite3",  # This is DB1
    },
    'db2': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / "db2.sqlite3",  # This is DB2
    }
}
