
from django.db import models

class SomeModel(models.Model):
    pass

class OtherModel(models.Model):
    some_model = models.ForeignKey(SomeModel, on_delete=models.CASCADE)

# Example usage
om = OtherModel()

# Check if the foreign key is set
if om.some_model_id is not None:
    # Foreign key is set, you can safely access 'some_model'
    some_model_instance = om.some_model
else:
    # Foreign key is not set
    print("some_model is not set.")
