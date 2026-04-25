
from django.db import models

class SomeModel(models.Model):
    name = models.CharField(max_length=100)

class OtherModel(models.Model):
    some_model = models.ForeignKey(SomeModel, null=True, on_delete=models.SET_NULL)

# Usage
om = OtherModel()

# Check if related object is set
if om.some_model_id is not None:
    # Foreign key is set
    print("Foreign key is set")
else:
    # Foreign key is not set
    print("Foreign key is not set")
