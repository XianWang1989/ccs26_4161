
from django.db import models

class SomeModel(models.Model):
    pass

class OtherModel(models.Model):
    some_model = models.ForeignKey(SomeModel, null=True, on_delete=models.SET_NULL)

# Check if the foreign key is set
om = OtherModel()

# Use a query to check if the foreign key `some_model` is set
if om.some_model_id is not None:
    print("Foreign key is set.")
else:
    print("Foreign key is not set.")
