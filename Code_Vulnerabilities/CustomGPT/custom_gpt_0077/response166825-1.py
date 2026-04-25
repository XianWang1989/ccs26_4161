
from django.db import models

class SomeModel(models.Model):
    name = models.CharField(max_length=100)

class OtherModel(models.Model):
    some_model = models.ForeignKey(SomeModel, on_delete=models.CASCADE)

# Example usage
om = OtherModel()

# Assuming you want to check if the related SomeModel object exists
if om.some_model_id is not None:  # Check if the ForeignKey ID is set
    print("Related SomeModel exists.")
else:
    print("Related SomeModel does not exist.")
