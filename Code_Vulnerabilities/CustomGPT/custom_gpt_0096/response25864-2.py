
class AppRouter:
    """
    A router to control all database operations for
    different applications in a Django project.
    """

    def db_for_read(self, model, **hints):
        """
        Directs read operations for App1 to DB1 and App2 to DB2.
        """
        if model._meta.app_label == 'app1':
            return 'default'
        elif model._meta.app_label == 'app2':
            return 'db2'
        return None

    def db_for_write(self, model, **hints):
        """
        Directs write operations for App1 to DB1 and App2 to DB2.
        """
        if model._meta.app_label == 'app1':
            return 'default'
        elif model._meta.app_label == 'app2':
            return 'db2'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if a model in the app1 is involved.
        """
        if obj1._meta.app_label == 'app1' or obj2._meta.app_label == 'app1':
            return True
        elif obj1._meta.app_label == 'app2' or obj2._meta.app_label == 'app2':
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Ensure that the correct apps are migrated to the appropriate database.
        """
        if app_label == 'app1':
            return db == 'default'
        elif app_label == 'app2':
            return db == 'db2'
        return None
