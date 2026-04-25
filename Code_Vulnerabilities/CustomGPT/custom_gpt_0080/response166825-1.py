
from django.db import models
from django.shortcuts import get_object_or_404

class SomeModel(models.Model):
    pass

class OtherModel(models.Model):
    some_model = models.ForeignKey(SomeModel, on_delete=models.SET_NULL, null=True)

# Checking if the foreign key is set
def check_some_model(om):
    if om.some_model_id is not None:  # Use the ID directly
        # Foreign key is set
        return True
    return False

# Usage
om = OtherModel()  # This should be fetched from the database
print(check_some_model(om))
