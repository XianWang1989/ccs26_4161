
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    },
    'DB1': {
        'ENGINE': 'django.db.backends.mysql',  # example using MySQL
        'NAME': 'db1_name',
        'USER': 'db1_user',
        'PASSWORD': 'db1_password',
        'HOST': 'localhost',
        'PORT': '3306',
    },
    'DB2': {
        'ENGINE': 'django.db.backends.mysql',  # example using MySQL
        'NAME': 'db2_name',
        'USER': 'db2_user',
        'PASSWORD': 'db2_password',
        'HOST': 'localhost',
        'PORT': '3306',
    },
}
