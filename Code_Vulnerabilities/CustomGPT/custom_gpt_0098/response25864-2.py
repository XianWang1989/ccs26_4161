
class AppRouter:
    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'App1':
            return 'default'
        elif model._meta.app_label == 'App2':
            return 'db2'
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label == 'App1':
            return 'default'
        elif model._meta.app_label == 'App2':
            return 'db2'
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label == 'App1':
            return db == 'default'
        elif app_label == 'App2':
            return db == 'db2'
        return None
