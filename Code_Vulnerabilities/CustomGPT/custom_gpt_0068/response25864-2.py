
class AppRouter:
    def db_for_read(self, model, **hints):
        """Point read operations to the appropriate database."""
        if model._app_label == 'app1':
            return 'DB1'
        elif model._app_label == 'app2':
            return 'DB2'
        return None

    def db_for_write(self, model, **hints):
        """Point write operations to the appropriate database."""
        if model._app_label == 'app1':
            return 'DB1'
        elif model._app_label == 'app2':
            return 'DB2'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """Allow relations if a model in the app1 or app2 is involved."""
        if obj1._app_label == 'app1' or obj2._app_label == 'app1':
            return True
        if obj1._app_label == 'app2' or obj2._app_label == 'app2':
            return True
        return None

    def get_common_db(self, model, **hints):
        """Fallback database if no specific routing is defined."""
        return None
