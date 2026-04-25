
class AppRouter:
    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'app1':
            return 'default'  # Use DB1
        elif model._meta.app_label == 'app2':
            return 'db2'  # Use DB2

    def db_for_write(self, model, **hints):
        if model._meta.app_label == 'app1':
            return 'default'
        elif model._meta.app_label == 'app2':
            return 'db2'

    def allow_relation(self, obj1, obj2, **hints):
        if obj1._meta.app_label == 'app1' and obj2._meta.app_label == 'app1':
            return True
        elif obj1._meta.app_label == 'app2' and obj2._meta.app_label == 'app2':
            return True
        return False

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label == 'app1':
            return db == 'default'  # Only DB1 for App1 migrations
        elif app_label == 'app2':
            return db == 'db2'  # Only DB2 for App2 migrations
        return None
