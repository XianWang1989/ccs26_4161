
from django.db import models
from django.core.exceptions import ObjectDoesNotExist

class SomeModel(models.Model):
    pass

class OtherModel(models.Model):
    some_model = models.ForeignKey(SomeModel, on_delete=models.CASCADE, null=True, blank=True)

# Creating an instance of OtherModel
om = OtherModel()

# Checking if some_model is set without causing an exception
if om.some_model_id is not None:
    # some_model is set
    print("Foreign key is set.")
else:
    # some_model is not set
    print("Foreign key is not set.")
