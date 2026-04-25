
# db_router.py

class AppRouter:
    def db_for_read(self, model, **hints):
        """Point read operations for App1 to 'default' and for App2 to 'db2'."""
        if model._meta.app_label == 'app1':
            return 'default'
        elif model._meta.app_label == 'app2':
            return 'db2'
        return None

    def db_for_write(self, model, **hints):
        """Point write operations for App1 to 'default' and for App2 to 'db2'."""
        if model._meta.app_label == 'app1':
            return 'default'
        elif model._meta.app_label == 'app2':
            return 'db2'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """Allow relations if a model in app1 is involved."""
        if obj1._meta.app_label == 'app1' or obj2._meta.app_label == 'app1':
            return True
        if obj1._meta.app_label == 'app2' or obj2._meta.app_label == 'app2':
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """Make sure the right apps get migrated to the right databases."""
        if app_label == 'app1':
            return db == 'default'
        elif app_label == 'app2':
            return db == 'db2'
        return None
