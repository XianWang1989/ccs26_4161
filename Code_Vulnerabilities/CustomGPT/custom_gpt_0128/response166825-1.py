
from django.db import models
from django.core.exceptions import ObjectDoesNotExist

class SomeModel(models.Model):
    pass

class OtherModel(models.Model):
    some_model = models.ForeignKey(SomeModel, null=True, on_delete=models.SET_NULL)

# Example usage
om = OtherModel.objects.get(id=1)  # or however you obtain the instance

# Checking if the foreign key is set
if om.some_model_id is not None:
    # The related SomeModel object is set
    print("Foreign key is set.")
else:
    # The foreign key is not set
    print("Foreign key is not set.")
