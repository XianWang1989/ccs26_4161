
from django.db import models

class SomeModel(models.Model):
    pass

class OtherModel(models.Model):
    some_model = models.ForeignKey(SomeModel, null=True, on_delete=models.SET_NULL)

# Example usage
om = OtherModel.objects.create()  # Create an instance of OtherModel

# Check if the ForeignKey is set
if om.some_model_id is not None:  # Directly check the ID of the ForeignKey
    print("some_model is set")
else:
    print("some_model is not set")
