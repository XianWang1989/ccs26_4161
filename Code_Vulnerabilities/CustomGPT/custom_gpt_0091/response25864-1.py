
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',  # or another DB backend
        'NAME': BASE_DIR / "db1.sqlite3",
    },
    'db2': {
        'ENGINE': 'django.db.backends.sqlite3',  # or another DB backend
        'NAME': BASE_DIR / "db2.sqlite3",
    }
}
