
# db_router.py

class AppRouter:
    """
    A router to control all database operations for different apps.
    """

    def db_for_read(self, model, **hints):
        """Point all read operations to the appropriate database."""
        if model._app_label == 'app1':
            return 'default'
        elif model._app_label == 'app2':
            return 'db2'
        return None

    def db_for_write(self, model, **hints):
        """Point all write operations to the appropriate database."""
        if model._app_label == 'app1':
            return 'default'
        elif model._app_label == 'app2':
            return 'db2'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """Allow relations if a model in the app1 or app2 is involved."""
        if obj1._app_label == 'app1' or obj1._app_label == 'app2':
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """Make sure the app's models get created in the respective database."""
        if app_label == 'app1':
            return db == 'default'
        elif app_label == 'app2':
            return db == 'db2'
        return None
