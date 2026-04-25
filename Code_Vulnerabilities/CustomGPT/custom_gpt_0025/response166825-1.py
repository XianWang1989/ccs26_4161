
from django.db import models
from django.core.exceptions import ObjectDoesNotExist

class SomeModel(models.Model):
    name = models.CharField(max_length=100)

class OtherModel(models.Model):
    some_model = models.ForeignKey(SomeModel, on_delete=models.SET_NULL, null=True, blank=True)

# Usage
om = OtherModel()

# Check if the ForeignKey is set
if om.some_model_id is not None:  # This checks the ID directly
    print("Foreign key is set.")
else:
    print("Foreign key is not set.")
