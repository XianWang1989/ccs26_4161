
from django.db import models

class SomeModel(models.Model):
    name = models.CharField(max_length=100)

class OtherModel(models.Model):
    some_model = models.ForeignKey(SomeModel, on_delete=models.SET_NULL, null=True)

# Example usage
om = OtherModel.objects.get(id=1)  # Fetch an instance

# Check if some_model is set
if om.some_model_id is not None:  # Using .some_model_id directly
    print("Foreign key is set:", om.some_model)
else:
    print("Foreign key is not set.")
