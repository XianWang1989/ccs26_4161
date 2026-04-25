
from django.db import models

class SomeModel(models.Model):
    name = models.CharField(max_length=100)

class OtherModel(models.Model):
    some_model = models.ForeignKey(SomeModel, on_delete=models.SET_NULL, null=True)

# Checking if the foreign key object is set
om = OtherModel.objects.select_related('some_model').first()  # Fetch one instance with related data

if om.some_model is not None:
    print("SomeModel is set:", om.some_model.name)
else:
    print("SomeModel is not set")
