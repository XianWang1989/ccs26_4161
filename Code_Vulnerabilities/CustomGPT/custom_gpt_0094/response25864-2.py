
class AppRouter:
    """A router to control all database operations on models in the app"""

    def db_for_read(self, model, **hints):
        """Directs read operations to the appropriate database"""
        if model._meta.app_label == 'app1':
            return 'default'  # DB1
        elif model._meta.app_label == 'app2':
            return 'db2'  # DB2
        return None

    def db_for_write(self, model, **hints):
        """Directs write operations to the appropriate database"""
        if model._meta.app_label == 'app1':
            return 'default'  # DB1
        elif model._meta.app_label == 'app2':
            return 'db2'  # DB2
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """Controls whether a relation between two objects is allowed"""
        if obj1._meta.app_label == 'app1' and obj2._meta.app_label == 'app1':
            return True
        elif obj1._meta.app_label == 'app2' and obj2._meta.app_label == 'app2':
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """Controls whether a model is allowed to be migrated."""
        if app_label == 'app1':
            return db == 'default'  # DB1
        elif app_label == 'app2':
            return db == 'db2'  # DB2
        return None
