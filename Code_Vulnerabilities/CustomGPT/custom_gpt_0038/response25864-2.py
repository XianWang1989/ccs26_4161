
class AppRouter:
    def db_for_read(self, model, **hints):
        """Directs read operations for models to their respective databases."""
        if model._meta.app_label == 'app1':
            return 'DB1'
        elif model._meta.app_label == 'app2':
            return 'DB2'
        return None

    def db_for_write(self, model, **hints):
        """Directs write operations for models to their respective databases."""
        if model._meta.app_label == 'app1':
            return 'DB1'
        elif model._meta.app_label == 'app2':
            return 'DB2'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """Allow relations if a model in the same database."""
        if obj1._meta.app_label == obj2._meta.app_label:
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """Ensure the app's migrations go to the correct database."""
        if app_label == 'app1':
            return db == 'DB1'
        elif app_label == 'app2':
            return db == 'DB2'
        return None
