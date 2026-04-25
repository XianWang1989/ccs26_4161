
from django.db import models

class SomeModel(models.Model):
    pass

class OtherModel(models.Model):
    some_model = models.ForeignKey(SomeModel, on_delete=models.SET_NULL, null=True)

# Example usage
om = OtherModel()

# Check if some_model is set
if om.some_model_id is not None:  # Use the ID field of the ForeignKey
    print("The foreign key object is set.")
else:
    print("The foreign key object is not set.")
