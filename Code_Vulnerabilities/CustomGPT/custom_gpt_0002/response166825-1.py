
from django.db import models

class SomeModel(models.Model):
    # Fields for SomeModel
    name = models.CharField(max_length=100)

class OtherModel(models.Model):
    some_model = models.ForeignKey(SomeModel, on_delete=models.CASCADE, null=True, blank=True)

# Example code to check if ForeignKey is set
om = OtherModel.objects.first()  # Get first instance or create one
if om.some_model_id is not None:
    print("SomeModel is set.")
else:
    print("SomeModel is not set.")
