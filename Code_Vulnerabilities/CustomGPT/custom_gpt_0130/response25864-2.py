
class AppRouter:
    """
    A router to control all database operations on models in
    the App1 and App2 applications.
    """
    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'app1':
            return 'default'  # DB1
        elif model._meta.app_label == 'app2':
            return 'db2'      # DB2
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label == 'app1':
            return 'default'
        elif model._meta.app_label == 'app2':
            return 'db2'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        return True

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label == 'app1':
            return db == 'default'
        elif app_label == 'app2':
            return db == 'db2'
        return None
