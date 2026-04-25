
class AppDatabaseRouter:
    def db_for_read(self, model, **hints):
        """Direct read operations for models of App1 to DB1 and App2 to DB2."""
        if model._meta.app_label == 'app1':
            return 'DB1'
        elif model._meta.app_label == 'app2':
            return 'DB2'
        return None

    def db_for_write(self, model, **hints):
        """Direct write operations for models of App1 to DB1 and App2 to DB2."""
        if model._meta.app_label == 'app1':
            return 'DB1'
        elif model._meta.app_label == 'app2':
            return 'DB2'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """Allow relationships only if a model in the same application is involved."""
        if obj1._meta.app_label == obj2._meta.app_label:
            return True
        elif 'app1' in [obj1._meta.app_label, obj2._meta.app_label]:
            return True
        elif 'app2' in [obj1._meta.app_label, obj2._meta.app_label]:
            return True
        return False

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """Ensure that migrations for App1 go to DB1 and App2 to DB2."""
        if app_label == 'app1':
            return db == 'DB1'
        elif app_label == 'app2':
            return db == 'DB2'
        return None
