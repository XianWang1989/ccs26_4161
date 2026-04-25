
from django.db import models

class SomeModel(models.Model):
    # Fields for SomeModel
    pass

class OtherModel(models.Model):
    some_model = models.ForeignKey(SomeModel, on_delete=models.CASCADE, null=True, blank=True)

# Creating an instance of OtherModel
om = OtherModel()

# Check if some_model is set
if om.some_model_id is not None:  # Using the _id field for direct checking
    # Foreign key is set, perform your logic here
    print("Foreign key is set to:", om.some_model_id)
else:
    print("Foreign key is not set.")
