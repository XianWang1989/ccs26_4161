
class AppRouter:
    def db_for_read(self, model, **hints):
        """Attempts to read app1 models go to db1."""
        if model._meta.app_label == 'app1':
            return 'default'
        elif model._meta.app_label == 'app2':
            return 'db2'
        return None

    def db_for_write(self, model, **hints):
        """Attempts to write app1 models go to db1."""
        if model._meta.app_label == 'app1':
            return 'default'
        elif model._meta.app_label == 'app2':
            return 'db2'
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """Ensure the right app is created in the correct database."""
        if app_label == 'app1':
            return db == 'default'
        elif app_label == 'app2':
            return db == 'db2'
        return None
