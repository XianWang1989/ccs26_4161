
class AppDatabaseRouter:
    def db_for_read(self, model, **hints):
        """Point read operations to the relevant database."""
        if model._app_label == 'App1':
            return 'DB1'
        elif model._app_label == 'App2':
            return 'DB2'
        return None

    def db_for_write(self, model, **hints):
        """Point write operations to the relevant database."""
        if model._app_label == 'App1':
            return 'DB1'
        elif model._app_label == 'App2':
            return 'DB2'
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """Ensure that the correct database is used for migrations."""
        if app_label == 'App1':
            return db == 'DB1'
        elif app_label == 'App2':
            return db == 'DB2'
        return None
