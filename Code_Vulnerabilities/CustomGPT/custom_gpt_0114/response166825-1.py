
from django.db import models
from django.core.exceptions import ObjectDoesNotExist

class SomeModel(models.Model):
    pass

class OtherModel(models.Model):
    some_model = models.ForeignKey(SomeModel, on_delete=models.SET_NULL, null=True)

# Check if foreign key is set
def is_some_model_set(om):
    return om.some_model_id is not None

# Usage
om = OtherModel()
if is_some_model_set(om):
    # Do something if some_model is set
    print("Foreign key is set.")
else:
    print("Foreign key is not set.")
