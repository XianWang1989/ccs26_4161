
class AppRouter:
    def db_for_model(self, model, **hints):
        if model._meta.app_label == 'app1':
            return 'default'
        elif model._meta.app_label == 'app2':
            return 'db2'
        return None
