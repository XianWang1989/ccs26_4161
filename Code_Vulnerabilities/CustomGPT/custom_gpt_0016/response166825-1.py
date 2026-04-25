
from django.db import models

class SomeModel(models.Model):
    # Attributes of SomeModel
    name = models.CharField(max_length=100)

class OtherModel(models.Model):
    some_model = models.ForeignKey(SomeModel, null=True, on_delete=models.SET_NULL)

# Example usage
om = OtherModel()
if om.some_model is not None:
    print("Foreign key is set to:", om.some_model)
else:
    print("Foreign key is not set.")
