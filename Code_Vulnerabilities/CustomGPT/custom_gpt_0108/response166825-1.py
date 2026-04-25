
from django.db import models

class SomeModel(models.Model):
    pass

class OtherModel(models.Model):
    some_model = models.ForeignKey(SomeModel, on_delete=models.CASCADE)

# Create an instance of OtherModel
om = OtherModel()

# Check if the related SomeModel instance is set
if om.some_model_id is not None:  # Check if the ID is set
    print("Foreign key is set.")
else:
    print("Foreign key is not set.")
