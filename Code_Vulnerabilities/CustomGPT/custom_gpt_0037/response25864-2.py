
class AppRouter:
    """
    A router to control all database operations on models
    for different applications.
    """

    def db_for_read(self, model, **hints):
        """
        Attempts to read models go to their respective database.
        """
        if model._meta.app_label == 'app1':
            return 'default'
        elif model._meta.app_label == 'app2':
            return 'db2'
        return None

    def db_for_write(self, model, **hints):
        """
        Attempts to write models go to their respective database.
        """
        if model._meta.app_label == 'app1':
            return 'default'
        elif model._meta.app_label == 'app2':
            return 'db2'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if a model in the app is involved.
        """
        if obj1._meta.app_label == 'app1' or obj2._meta.app_label == 'app1':
            return True
        elif obj1._meta.app_label == 'app2' or obj2._meta.app_label == 'app2':
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Ensure that the right app gets its migrations applied to the right database.
        """
        if app_label == 'app1':
            return db == 'default'
        elif app_label == 'app2':
            return db == 'db2'
        return None
