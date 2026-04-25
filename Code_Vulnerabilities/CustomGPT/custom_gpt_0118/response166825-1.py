
from django.db import models

class SomeModel(models.Model):
    # Define fields for SomeModel
    name = models.CharField(max_length=100)

class OtherModel(models.Model):
    some_model = models.ForeignKey(SomeModel, on_delete=models.SET_NULL, null=True)

# Example usage
om = OtherModel.objects.first()  # Assume we are fetching an instance

# Check if the foreign key object is set
if om.some_model_id is not None:  # Checking the ID directly
    # Foreign key is set; you can safely access it.
    related_object = om.some_model
else:
    # Foreign key is not set
    related_object = None
