
from django.db import models

class SomeModel(models.Model):
    pass

class OtherModel(models.Model):
    some_model = models.ForeignKey(SomeModel, on_delete=models.CASCADE, null=True, blank=True)

# Create an instance of OtherModel
om = OtherModel()

# Save the instance to the database to avoid DoesNotExist error when accessing the field
om.save()

# Check if the ForeignKey is set
if om.some_model_id is not None:
    print("Foreign key is set.")
else:
    print("Foreign key is not set.")
