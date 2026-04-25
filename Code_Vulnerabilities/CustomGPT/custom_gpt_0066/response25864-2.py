
class App1Router:
    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'app1':
            return 'default'
        return 'db2'

    def db_for_write(self, model, **hints):
        if model._meta.app_label == 'app1':
            return 'default'
        return 'db2'

    def allow_relation(self, obj1, obj2, **hints):
        if obj1._meta.app_label == 'app1' and obj2._meta.app_label == 'app1':
            return True
        elif obj1._meta.app_label == 'app2' and obj2._meta.app_label == 'app2':
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label == 'app1':
            return db == 'default'
        elif app_label == 'app2':
            return db == 'db2'
        return None
