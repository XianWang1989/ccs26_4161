
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',  # Change according to your actual database
        'NAME': BASE_DIR / "db1.sqlite3",
    },
    'another_db': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / "db2.sqlite3",
    }
}
