
class AppRouter:
    def db_for_model(self, model, **hints):
        """Directs models to their respective databases."""
        if model._meta.app_label == 'app1':
            return 'default'  # Use DB1
        elif model._meta.app_label == 'app2':
            return 'db2'  # Use DB2
        return None

    def db_for_read(self, model, **hints):
        return self.db_for_model(model, **hints)

    def db_for_write(self, model, **hints):
        return self.db_for_model(model, **hints)

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """Ensure that the right database is used for migrations."""
        if app_label == 'app1':
            return db == 'default'
        elif app_label == 'app2':
            return db == 'db2'
        return None
