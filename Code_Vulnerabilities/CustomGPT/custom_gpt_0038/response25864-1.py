
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / "db.sqlite3",
    },
    'DB1': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / "db1.sqlite3",
    },
    'DB2': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / "db2.sqlite3",
    }
}
