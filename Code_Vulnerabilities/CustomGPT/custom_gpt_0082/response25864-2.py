
# app1/db_router.py

class AppRouter:
    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'app1':
            return 'default'  # First database for App1
        elif model._meta.app_label == 'app2':
            return 'db2'  # Second database for App2
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label == 'app1':
            return 'default'
        elif model._meta.app_label == 'app2':
            return 'db2'
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label == 'app1':
            return db == 'default'
        elif app_label == 'app2':
            return db == 'db2'
        return None
