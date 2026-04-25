
from django.db import models

class SomeModel(models.Model):
    pass

class OtherModel(models.Model):
    some_model = models.ForeignKey(SomeModel, on_delete=models.SET_NULL, null=True)

# Example usage
om = OtherModel.objects.create()  # Create an instance of OtherModel

# Checking if the foreign key is set
if om.some_model_id is not None:
    # The foreign key object is set
    print("SomeModel is set:", om.some_model)
else:
    # The foreign key object is not set
    print("SomeModel is not set.")
