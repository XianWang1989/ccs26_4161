
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',  # or your chosen database engine
        'NAME': BASE_DIR / "db.sqlite3",
    },
    'db1': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / "db1.sqlite3",
    },
    'db2': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / "db2.sqlite3",
    }
}
