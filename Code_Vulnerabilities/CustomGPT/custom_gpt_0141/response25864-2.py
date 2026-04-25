
# db_router.py

class AppRouter:
    """
    A router to control all database operations on models of
    different applications.
    """

    def db_for_read(self, model, **hints):
        """Attempts to read app1 models go to DB1, app2 models to DB2."""
        if model._meta.app_label == 'app1':
            return 'default'  # DB1
        elif model._meta.app_label == 'app2':
            return 'db2'      # DB2
        return None

    def db_for_write(self, model, **hints):
        """Attempts to write app1 models go to DB1, app2 models to DB2."""
        if model._meta.app_label == 'app1':
            return 'default'  # DB1
        elif model._meta.app_label == 'app2':
            return 'db2'      # DB2
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """Make sure the app1 models get created on the right database."""
        if app_label == 'app1':
            return db == 'default'  # Migrate app1 models to DB1
        elif app_label == 'app2':
            return db == 'db2'      # Migrate app2 models to DB2
        return None
