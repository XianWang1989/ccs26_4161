
class AppRouter:
    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'app1':
            return 'DB1'
        elif model._meta.app_label == 'app2':
            return 'DB2'
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label == 'app1':
            return 'DB1'
        elif model._meta.app_label == 'app2':
            return 'DB2'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        if obj1._meta.app_label == 'app1' and obj2._meta.app_label == 'app2':
            return True
        return None

    def get_database(self, model_name):
        if model_name in ('App1Model'):
            return 'DB1'
        elif model_name in ('App2Model'):
            return 'DB2'
        return None
