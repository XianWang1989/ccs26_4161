
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',  # For example, use SQLite or another DB
        'NAME': BASE_DIR / 'db.sqlite3',
    },
    'DB1': {
        'ENGINE': 'django.db.backends.postgresql',  # Change according to your DB
        'NAME': 'database1',
        'USER': 'yourusername',
        'PASSWORD': 'yourpassword',
        'HOST': 'localhost',
        'PORT': '5432',
    },
    'DB2': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'database2',
        'USER': 'yourusername',
        'PASSWORD': 'yourpassword',
        'HOST': 'localhost',
        'PORT': '5432',
    },
}
