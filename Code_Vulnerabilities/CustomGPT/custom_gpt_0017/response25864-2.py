
class AppDatabaseRouter:
    def db_for_model(self, model, **hints):
        if model._meta.app_label == 'App1':
            return 'default'  # Use DB1
        elif model._meta.app_label == 'App2':
            return 'db2'      # Use DB2
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label == 'App1':
            return db == 'default'
        elif app_label == 'App2':
            return db == 'db2'
        return None
