
from django.db import models

class SomeModel(models.Model):
    name = models.CharField(max_length=100)

class OtherModel(models.Model):
    some_model = models.ForeignKey(SomeModel, on_delete=models.SET_NULL, null=True)

# Example usage
om = OtherModel.objects.first()  # Assuming you fetch an instance

if om.some_model_id is not None:  # Check the ID instead of the object
    print("Foreign key is set")
else:
    print("Foreign key is not set")
