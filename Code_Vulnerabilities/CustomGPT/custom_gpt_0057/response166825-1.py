
from django.db import models

class SomeModel(models.Model):
    pass

class OtherModel(models.Model):
    some_model = models.ForeignKey(SomeModel, on_delete=models.SET_NULL, null=True)

# Example usage
om = OtherModel()

# Check if some_model is set
if om.some_model_id is not None:
    print("Foreign key is set.")
else:
    print("Foreign key is not set.")
