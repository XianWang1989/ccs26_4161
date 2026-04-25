
from django.db import models

class SomeModel(models.Model):
    # Your fields here
    pass

class OtherModel(models.Model):
    some_model = models.ForeignKey(SomeModel, null=True, on_delete=models.SET_NULL)

    def is_some_model_set(self):
        return self.some_model is not None

# Example usage
om = OtherModel()
if om.is_some_model_set():
    # SomeModel is set
    pass
else:
    # SomeModel is not set
    pass
