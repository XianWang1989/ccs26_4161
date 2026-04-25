
from django.db import models

class SomeModel(models.Model):
    pass

class OtherModel(models.Model):
    some_model = models.ForeignKey(SomeModel, on_delete=models.CASCADE, null=True, blank=True)

# Example usage
om = OtherModel()

# Check if the related object is set
if om.some_model_id is not None and SomeModel.objects.filter(id=om.some_model_id).exists():
    # The foreign key is set and the object exists
    print("Related SomeModel object is set.")
else:
    print("Related SomeModel object is not set.")
