
from django.db import models

class SomeModel(models.Model):
    # Add fields here
    pass

class OtherModel(models.Model):
    some_model = models.ForeignKey(SomeModel, null=True, on_delete=models.SET_NULL)

# Example usage
om = OtherModel()

if om.some_model_id is not None:
    # The foreign key is set
    print("Foreign key is set!")
else:
    # The foreign key is not set
    print("Foreign key is not set.")
