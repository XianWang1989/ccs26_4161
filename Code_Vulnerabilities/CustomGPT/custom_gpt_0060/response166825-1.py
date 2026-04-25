
from django.db import models

class SomeModel(models.Model):
    name = models.CharField(max_length=100)

class OtherModel(models.Model):
    some_model = models.ForeignKey(SomeModel, on_delete=models.SET_NULL, null=True)

# Creating an instance of OtherModel without linking to SomeModel
om = OtherModel()  # some_model will be None initially

# Check if some_model is set
if om.some_model is not None:
    print("The foreign key is set.")
else:
    print("The foreign key is not set.")
