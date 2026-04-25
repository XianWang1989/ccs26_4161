
from django.db import models

class SomeModel(models.Model):
    pass

class OtherModel(models.Model):
    some_model = models.ForeignKey(SomeModel, null=True, on_delete=models.CASCADE)

# Example usage
om = OtherModel()

# Check if the foreign key is set
if om.some_model_id is not None:
    # Do something with om.some_model
    pass
else:
    # Handle the case where some_model is not set
    pass
