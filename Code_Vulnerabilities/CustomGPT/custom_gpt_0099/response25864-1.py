
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',  # Example for DB1
        'NAME': BASE_DIR / "db1.sqlite3",
    },
    'db2': {
        'ENGINE': 'django.db.backends.sqlite3',  # Example for DB2
        'NAME': BASE_DIR / "db2.sqlite3",
    }
}
