
# settings.py

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',  # Example: change according to your DB
        'NAME': BASE_DIR / "db1.sqlite3",        # DB1 for App1
    },
    'db2': {
        'ENGINE': 'django.db.backends.sqlite3',  # Example: change according to your DB
        'NAME': BASE_DIR / "db2.sqlite3",        # DB2 for App2
    }
}
