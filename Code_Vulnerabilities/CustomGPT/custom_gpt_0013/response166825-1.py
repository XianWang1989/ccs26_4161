
from django.db import models
from django.core.exceptions import ObjectDoesNotExist

class SomeModel(models.Model):
    name = models.CharField(max_length=100)

class OtherModel(models.Model):
    some_model = models.ForeignKey(SomeModel, on_delete=models.CASCADE, null=True)

# Example of checking if the foreign key is set
def is_foreign_key_set(om):
    # Check if the related object exists
    return om.some_model_id is not None

# Creating an instance of OtherModel
om = OtherModel()

# Check if some_model is set
if is_foreign_key_set(om):
    print("Foreign key is set.")
else:
    print("Foreign key is not set.")
