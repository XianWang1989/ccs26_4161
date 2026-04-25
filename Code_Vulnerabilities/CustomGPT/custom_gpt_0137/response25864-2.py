
class AppRouter:
    """
    A router to control all database operations on models for different apps.
    """

    def db_for_read(self, model, **hints):
        """Point read operations for app1 to DB1 and app2 to DB2."""
        if model._meta.app_label == 'App1':
            return 'DB1'
        elif model._meta.app_label == 'App2':
            return 'DB2'
        return None

    def db_for_write(self, model, **hints):
        """Point write operations for app1 to DB1 and app2 to DB2."""
        if model._meta.app_label == 'App1':
            return 'DB1'
        elif model._meta.app_label == 'App2':
            return 'DB2'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """Allow relations if a model in app1 is involved."""
        if obj1._meta.app_label == 'App1' or obj2._meta.app_label == 'App1':
            return True
        if obj1._meta.app_label == 'App2' or obj2._meta.app_label == 'App2':
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """Make sure the right app only appears in the right database."""
        if app_label == 'App1':
            return db == 'DB1'
        elif app_label == 'App2':
            return db == 'DB2'
        return None
