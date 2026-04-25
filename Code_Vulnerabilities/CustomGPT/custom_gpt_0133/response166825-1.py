
from django.db import models

class SomeModel(models.Model):
    # Fields for SomeModel
    name = models.CharField(max_length=100)

class OtherModel(models.Model):
    some_model = models.ForeignKey(SomeModel, on_delete=models.CASCADE, null=True, blank=True)

# Example usage
om = OtherModel()

# Check if the ForeignKey is set
if om.some_model_id is not None:  # Using the _id field to check if it exists
    print(f"SomeModel instance ID: {om.some_model_id}")
else:
    print("The ForeignKey is not set.")
