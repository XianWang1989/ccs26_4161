
from django.db import models

class SomeModel(models.Model):
    name = models.CharField(max_length=100)

class OtherModel(models.Model):
    some_model = models.ForeignKey(SomeModel, null=True, on_delete=models.SET_NULL)

# Usage
om = OtherModel()

# Check if the foreign key is set
if om.some_model_id is not None:
    some_model_instance = om.some_model  # Now this won't raise an exception
else:
    print("Foreign key is not set.")
