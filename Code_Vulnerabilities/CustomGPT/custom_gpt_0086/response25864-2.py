
# db_router.py

class AppRouter:
    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'app1':
            return 'default'  # Use DB1 for App1
        elif model._meta.app_label == 'app2':
            return 'db2'  # Use DB2 for App2
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label == 'app1':
            return 'default'
        elif model._meta.app_label == 'app2':
            return 'db2'
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label == 'app1':
            return db == 'default'  # Only allow migrations for App1 in DB1
        elif app_label == 'app2':
            return db == 'db2'  # Only allow migrations for App2 in DB2
        return None
