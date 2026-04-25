
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / "db1.sqlite3",
    },
    'db2': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / "db2.sqlite3",
    }
}

DATABASE_ROUTERS = ['your_project_name.db_router.AppRouter']
