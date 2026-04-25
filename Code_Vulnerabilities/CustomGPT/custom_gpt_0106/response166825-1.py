
from django.db import models

class SomeModel(models.Model):
    pass

class OtherModel(models.Model):
    some_model = models.ForeignKey(SomeModel, on_delete=models.CASCADE)

# Example usage
om = OtherModel.objects.first()  # Get an instance of OtherModel

# Check if the foreign key is set
if om.some_model_id is not None:  # Use some_model_id to check directly
    print("Foreign key is set.")
else:
    print("Foreign key is not set.")
