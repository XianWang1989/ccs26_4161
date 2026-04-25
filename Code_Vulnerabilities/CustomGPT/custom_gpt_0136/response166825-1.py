
from django.db import models

class SomeModel(models.Model):
    pass

class OtherModel(models.Model):
    some_model = models.ForeignKey(SomeModel, on_delete=models.SET_NULL, null=True)

# Assume we have an instance of OtherModel
om = OtherModel()

# Check if the foreign key object is set
if om.some_model_id is not None:  # Use the _id attribute for a lightweight check
    # The foreign key is set
    print("Foreign key is set.")
else:
    # The foreign key is not set
    print("Foreign key is not set.")
