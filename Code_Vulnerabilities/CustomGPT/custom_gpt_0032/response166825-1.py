
from django.db import models
from django.core.exceptions import ObjectDoesNotExist

class SomeModel(models.Model):
    name = models.CharField(max_length=100)

class OtherModel(models.Model):
    some_model = models.ForeignKey(SomeModel, on_delete=models.SET_NULL, null=True)

# Example usage
om = OtherModel.objects.first()  # Assuming you're getting an instance from the database

if om.some_model_id is not None:
    # some_model is set
    print("The foreign key object is set:", om.some_model)
else:
    # some_model is not set
    print("The foreign key object is not set.")
