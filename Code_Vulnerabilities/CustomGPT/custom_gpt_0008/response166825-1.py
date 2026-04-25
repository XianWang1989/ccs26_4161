
from django.db import models

class SomeModel(models.Model):
    name = models.CharField(max_length=100)

class OtherModel(models.Model):
    some_model = models.ForeignKey(SomeModel, on_delete=models.SET_NULL, null=True)

# Create an instance of OtherModel
om = OtherModel()

# Check if the foreign key is set
if om.some_model_id is not None:  # or use om.is_valid() if contextually appropriate
    # The foreign key is set
    print("The foreign key is set.")
else:
    # The foreign key is not set
    print("The foreign key is not set.")
