
from django.db import models
from django.core.exceptions import ObjectDoesNotExist

class SomeModel(models.Model):
    name = models.CharField(max_length=100)

class OtherModel(models.Model):
    some_model = models.ForeignKey(SomeModel, on_delete=models.SET_NULL, null=True)

# Assuming you have an instance of OtherModel
om = OtherModel()

# Check if foreign key is set using queryset
if om.some_model_id is not None:
    # some_model is set
    print("Foreign key is set:", om.some_model)
else:
    # some_model is not set
    print("Foreign key is not set.")
