
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',  # Example: use sqlite
        'NAME': BASE_DIR / "db1.sqlite3",  # First database
    },
    'db2': {
        'ENGINE': 'django.db.backends.sqlite3',  # Example: use sqlite
        'NAME': BASE_DIR / "db2.sqlite3",  # Second database
    },
}
