
from django.db import models

class SomeModel(models.Model):
    # Your fields here
    name = models.CharField(max_length=100)

class OtherModel(models.Model):
    some_model = models.ForeignKey(SomeModel, null=True, on_delete=models.SET_NULL)  # Allow null

# Create an instance of OtherModel
om = OtherModel()

# Check if the foreign key is set
if om.some_model_id is not None:  # Check the ID directly
    print("Foreign key is set.")
else:
    print("Foreign key is not set.")
