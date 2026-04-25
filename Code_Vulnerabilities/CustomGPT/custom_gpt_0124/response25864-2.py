
class AppRouter:
    def db_for_read(self, model, **hints):
        """Directs read operations to the appropriate database based on the app."""
        if model._meta.app_label == 'app1':
            return 'DB1'
        elif model._meta.app_label == 'app2':
            return 'DB2'
        return None

    def db_for_write(self, model, **hints):
        """Directs write operations to the appropriate database based on the app."""
        if model._meta.app_label == 'app1':
            return 'DB1'
        elif model._meta.app_label == 'app2':
            return 'DB2'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """Controls whether a relation is allowed between two models."""
        if obj1._meta.app_label == 'app1' and obj2._meta.app_label == 'app1':
            return True
        elif obj1._meta.app_label == 'app2' and obj2._meta.app_label == 'app2':
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """Restricts migrations to the appropriate database."""
        if app_label == 'app1':
            return db == 'DB1'
        elif app_label == 'app2':
            return db == 'DB2'
        return None
