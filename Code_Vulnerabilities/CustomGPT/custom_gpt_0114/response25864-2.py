
class AppDatabaseRouter:
    def db_for_read(self, model, **hints):
        """Point read operations for App1 to DB1 and App2 to DB2."""
        if model._app_label == 'app1':
            return 'default'
        elif model._app_label == 'app2':
            return 'db2'
        return None

    def db_for_write(self, model, **hints):
        """Point write operations for App1 to DB1 and App2 to DB2."""
        if model._app_label == 'app1':
            return 'default'
        elif model._app_label == 'app2':
            return 'db2'
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """Ensure that the apps only appear in their respective databases."""
        if app_label == 'app1':
            return db == 'default'
        elif app_label == 'app2':
            return db == 'db2'
        return None
