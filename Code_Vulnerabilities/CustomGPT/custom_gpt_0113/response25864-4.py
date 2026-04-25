
# settings.py
DATABASES = {
    'default': { ... },  # DB1 settings
    'db2': { ... },      # DB2 settings
}

DATABASE_ROUTERS = ['app1.routers.AppRouter']

# routers.py
class AppRouter:
    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'app1':
            return 'default'
        elif model._meta.app_label == 'app2':
            return 'db2'
        return None

    def db_for_write(self, model, **hints):
        ...

    def allow_relation(self, obj1, obj2, **hints):
        return True

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        ...
