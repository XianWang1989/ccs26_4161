
from django.db import models

class SomeModel(models.Model):
    # Fields for SomeModel
    name = models.CharField(max_length=100)

class OtherModel(models.Model):
    some_model = models.ForeignKey(SomeModel, on_delete=models.CASCADE, null=True)

# Example code to check if the ForeignKey is set
om = OtherModel()

# Using isnull() to check if ForeignKey is set
if om.some_model_id is not None:
    # Foreign key is set
    print("Foreign key is set.")
else:
    # Foreign key is not set
    print("Foreign key is not set.")
