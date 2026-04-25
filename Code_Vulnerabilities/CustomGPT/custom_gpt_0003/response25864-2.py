
class AppRouter:
    def db_for_read(self, model, **hints):
        """Point read operations for App1 to DB1 and for App2 to DB2."""
        if model._meta.app_label == 'app1':
            return 'DB1'
        elif model._meta.app_label == 'app2':
            return 'DB2'
        return None

    def db_for_write(self, model, **hints):
        """Point write operations for App1 to DB1 and for App2 to DB2."""
        if model._meta.app_label == 'app1':
            return 'DB1'
        elif model._meta.app_label == 'app2':
            return 'DB2'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """Allow relationships if a model in the app1 is involved."""
        if obj1._meta.app_label == 'app1' or obj2._meta.app_label == 'app1':
            return True
        if obj1._meta.app_label == 'app2' or obj2._meta.app_label == 'app2':
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """Ensure the app1's models get created on DB1 and app2's on DB2."""
        if app_label == 'app1':
            return db == 'DB1'
        elif app_label == 'app2':
            return db == 'DB2'
        return None
