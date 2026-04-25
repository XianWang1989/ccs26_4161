
# settings.py

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / "db.sqlite3",
    },
    'db1': {
        'ENGINE': 'django.db.backends.postgresql',  # or any other supported database
        'NAME': 'your_db1_name',
        'USER': 'your_db1_user',
        'PASSWORD': 'your_db1_password',
        'HOST': 'localhost',
        'PORT': '5432',
    },
    'db2': {
        'ENGINE': 'django.db.backends.postgresql',  # or any other supported database
        'NAME': 'your_db2_name',
        'USER': 'your_db2_user',
        'PASSWORD': 'your_db2_password',
        'HOST': 'localhost',
        'PORT': '5432',
    },
}
