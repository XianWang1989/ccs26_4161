
# routers.py
class AppRouter:
    def db_for_read(self, model, **hints):
        """Prefer reading from the 'db2' if the app is App2."""
        if model._meta.app_label == 'app2':
            return 'db2'
        return 'default'

    def db_for_write(self, model, **hints):
        """Prefer writing to the 'db2' if the app is App2."""
        if model._meta.app_label == 'app2':
            return 'db2'
        return 'default'

    def allow_relation(self, obj1, obj2, **hints):
        """Allow relations if a model in the app2 is involved."""
        if obj1._meta.app_label == 'app2' or obj2._meta.app_label == 'app2':
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """Make sure the app2 models get created on the 'db2'."""
        if app_label == 'app2':
            return db == 'db2'
        return db == 'default'
