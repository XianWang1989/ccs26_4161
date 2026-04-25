
class AppRouter:
    def db_for_read(self, model, **hints):
        """Point all read operations for app1 to 'default' (DB1) and app2 to 'db2'."""
        if model._app_label == 'app1':
            return 'default'
        elif model._app_label == 'app2':
            return 'db2'
        return None

    def db_for_write(self, model, **hints):
        """Point all write operations for app1 to 'default' (DB1) and app2 to 'db2'."""
        if model._app_label == 'app1':
            return 'default'
        elif model._app_label == 'app2':
            return 'db2'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """Allow relation if a model in the app1 or app2 is involved."""
        if obj1._app_label == 'app1' and obj2._app_label == 'app1':
            return True
        elif obj1._app_label == 'app2' and obj2._app_label == 'app2':
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """Make sure the app1 models get created on the 'default' db and app2 on 'db2'."""
        if app_label == 'app1':
            return db == 'default'
        elif app_label == 'app2':
            return db == 'db2'
        return None
