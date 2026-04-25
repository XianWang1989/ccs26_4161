
from django.db import models

class SomeModel(models.Model):
    pass

class OtherModel(models.Model):
    some_model = models.ForeignKey(SomeModel, on_delete=models.SET_NULL, null=True)

# Example usage
om = OtherModel()

# Check if the ForeignKey is set
if om.some_model_id is not None:
    # The related SomeModel object is set
    print("SomeModel is set:", om.some_model)
else:
    print("SomeModel is not set.")
