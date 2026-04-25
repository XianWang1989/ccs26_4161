
from django.db import models

class SomeModel(models.Model):
    name = models.CharField(max_length=100)

class OtherModel(models.Model):
    some_model = models.ForeignKey(SomeModel, on_delete=models.SET_NULL, null=True)

# Create an instance of OtherModel
om = OtherModel()

# Optionally save it first so that you can check its foreign key
om.save()

# Check if the foreign key is set
if om.some_model is not None:
    print("Foreign key is set")
else:
    print("Foreign key is not set")
