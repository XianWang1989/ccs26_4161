
class AppRouter:
    """
    A router to control all database operations on models
    for different applications.
    """

    def db_for_read(self, model, **hints):
        """Directs read operations for App1 to db1 and App2 to db2."""
        if model._meta.app_label == 'app1':
            return 'db1'
        elif model._meta.app_label == 'app2':
            return 'db2'
        return None

    def db_for_write(self, model, **hints):
        """Directs write operations for App1 to db1 and App2 to db2."""
        if model._meta.app_label == 'app1':
            return 'db1'
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
        """Ensure that the app1's models get created on db1 and app2's models on db2."""
        if app_label == 'app1':
            return db == 'db1'
        elif app_label == 'app2':
            return db == 'db2'
        return None
