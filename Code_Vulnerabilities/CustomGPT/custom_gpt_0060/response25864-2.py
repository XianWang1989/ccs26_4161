
class AppRouter:
    """
    A router to control all database operations on models in the
    App1 and App2 applications.
    """

    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'App1':
            return 'DB1'
        elif model._meta.app_label == 'App2':
            return 'DB2'
        return 'default'

    def db_for_write(self, model, **hints):
        if model._meta.app_label == 'App1':
            return 'DB1'
        elif model._meta.app_label == 'App2':
            return 'DB2'
        return 'default'

    def allow_relation(self, obj1, obj2, **hints):
        if obj1._meta.app_label == 'App1' and obj2._meta.app_label == 'App1':
            return True
        elif obj1._meta.app_label == 'App2' and obj2._meta.app_label == 'App2':
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label == 'App1':
            return db == 'DB1'
        elif app_label == 'App2':
            return db == 'DB2'
        return None
