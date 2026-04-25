
class AppRouter:
    def db_for_read(self, model, **hints):
        """Point all read operations to the appropriate database."""
        if model._meta.app_label == 'App1':
            return 'default'
        elif model._meta.app_label == 'App2':
            return 'db2'
        return None

    def db_for_write(self, model, **hints):
        """Point all write operations to the appropriate database."""
        if model._meta.app_label == 'App1':
            return 'default'
        elif model._meta.app_label == 'App2':
            return 'db2'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """Allow relationships if a model in 'App1' is involved."""
        if obj1._meta.app_label == 'App1' or obj2._meta.app_label == 'App1':
            return True
        elif obj1._meta.app_label == 'App2' or obj2._meta.app_label == 'App2':
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """Make sure the right app's models get created in the right database."""
        if app_label == 'App1':
            return db == 'default'
        elif app_label == 'App2':
            return db == 'db2'
        return None
