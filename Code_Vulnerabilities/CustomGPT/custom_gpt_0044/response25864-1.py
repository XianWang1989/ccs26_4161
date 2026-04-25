
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',  # Use your desired database engine
        'NAME': BASE_DIR / 'db1.sqlite3',        # Database for App1
    },
    'db2': {
        'ENGINE': 'django.db.backends.sqlite3',  # Use your desired database engine
        'NAME': BASE_DIR / 'db2.sqlite3',        # Database for App2
    },
}
