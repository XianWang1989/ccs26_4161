
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',  # or any other database
        'NAME': BASE_DIR / "db1.sqlite3",
    },
    'db2': {
        'ENGINE': 'django.db.backends.sqlite3',  # or any other database
        'NAME': BASE_DIR / "db2.sqlite3",
    },
}
