
class AppRouter:
    def db_for_read(self, model, **hints):
        """Point all read operations to the appropriate database."""
        if model._meta.app_label == 'app1':
            return 'default'
        elif model._meta.app_label == 'app2':
            return 'db2'
        return None

    def db_for_write(self, model, **hints):
        """Point all write operations to the appropriate database."""
        if model._meta.app_label == 'app1':
            return 'default'
        elif model._meta.app_label == 'app2':
            return 'db2'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """Allow relations if a model in the same database."""
        db_list = (obj1._state.db, obj2._state.db)
        if 'default' in db_list and 'db2' in db_list:
            return False
        return True

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """Ensure apps only appear in their respective database."""
        if app_label == 'app1':
            return db == 'default'
        elif app_label == 'app2':
            return db == 'db2'
        return None
