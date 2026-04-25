
from django.db import models

class SomeModel(models.Model):
    pass

class OtherModel(models.Model):
    some_model = models.ForeignKey(SomeModel, on_delete=models.CASCADE, null=True, blank=True)

# Example: Creating an instance of OtherModel without setting a foreign key
om = OtherModel()

# Check if the foreign key is set
if om.some_model_id is not None:
    # Access the related object safely
    related_object = om.some_model
else:
    print("The foreign key 'some_model' is not set.")
