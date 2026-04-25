
from django.db import models
from django.db.models import Q

class SomeModel(models.Model):
    name = models.CharField(max_length=100)

class OtherModel(models.Model):
    some_model = models.ForeignKey(SomeModel, null=True, on_delete=models.SET_NULL)

# Example check
om = OtherModel.objects.first()  # Get the first instance of OtherModel

if om.some_model_id is not None:  # Check if the ForeignKey is set
    print("SomeModel is set:", om.some_model)
else:
    print("SomeModel is not set.")
