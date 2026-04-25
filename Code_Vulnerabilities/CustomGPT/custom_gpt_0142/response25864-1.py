
# settings.py

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',  # Example using SQLite, replace with your DB config
        'NAME': BASE_DIR / 'db1.sqlite3',        # Database for App1
    },
    'db2': {
        'ENGINE': 'django.db.backends.sqlite3',  # Example using SQLite, replace with your DB config
        'NAME': BASE_DIR / 'db2.sqlite3',        # Database for App2
    },
}
