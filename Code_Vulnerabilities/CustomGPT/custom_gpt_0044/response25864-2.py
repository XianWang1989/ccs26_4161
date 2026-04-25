
class AppRouter:
    def db_for_read(self, model, **hints):
        """Assigns the app's models to the appropriate database."""
        if model._meta.app_label == 'app1':
            return 'default'
        elif model._meta.app_label == 'app2':
            return 'db2'
        return None

    def db_for_write(self, model, **hints):
        """Assigns the app's models to the appropriate database."""
        if model._meta.app_label == 'app1':
            return 'default'
        elif model._meta.app_label == 'app2':
            return 'db2'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """Allow relationships between apps in the same database."""
        if obj1._meta.app_label == 'app1' and obj2._meta.app_label == 'app1':
            return True
        elif obj1._meta.app_label == 'app2' and obj2._meta.app_label == 'app2':
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """Make sure the app's models are only created in the appropriate database."""
        if app_label == 'app1':
            return db == 'default'
        elif app_label == 'app2':
            return db == 'db2'
        return None
