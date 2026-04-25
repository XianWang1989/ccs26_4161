
# routers.py

class AppRouter:
    """
    A router to control all database operations on models for
    different applications.
    """

    def db_for_read(self, model, **hints):
        """Direct read operations for app1 to db1 and app2 to db2."""
        if model._meta.app_label == 'app1':
            return 'default'
        elif model._meta.app_label == 'app2':
            return 'db2'
        return None

    def db_for_write(self, model, **hints):
        """Direct write operations for app1 to db1 and app2 to db2."""
        if model._meta.app_label == 'app1':
            return 'default'
        elif model._meta.app_label == 'app2':
            return 'db2'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """Allow relations between apps when a model in each db."""
        if obj1._meta.app_label == 'app1' and obj2._meta.app_label == 'app2':
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """Ensure migrations are applied to the correct database."""
        if app_label == 'app1':
            return db == 'default'
        elif app_label == 'app2':
            return db == 'db2'
        return None
