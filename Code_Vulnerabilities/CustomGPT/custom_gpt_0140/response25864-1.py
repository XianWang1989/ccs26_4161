
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / "db.sqlite3",
    },
    'DB1': {
        'ENGINE': 'django.db.backends.postgresql',  # Change as needed
        'NAME': 'your_db1_name',
        'USER': 'your_db1_user',
        'PASSWORD': 'your_db1_password',
        'HOST': 'localhost',
        'PORT': '5432',
    },
    'DB2': {
        'ENGINE': 'django.db.backends.postgresql',  # Change as needed
        'NAME': 'your_db2_name',
        'USER': 'your_db2_user',
        'PASSWORD': 'your_db2_password',
        'HOST': 'localhost',
        'PORT': '5432',
    },
}
