
class AppRouter:
    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'App1':
            return 'DB1'
        elif model._meta.app_label == 'App2':
            return 'DB2'
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label == 'App1':
            return 'DB1'
        elif model._meta.app_label == 'App2':
            return 'DB2'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        return True  # Allow relations between apps within the same database

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label == 'App1':
            return db == 'DB1'
        elif app_label == 'App2':
            return db == 'DB2'
        return None
