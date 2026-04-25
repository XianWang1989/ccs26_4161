
from django.db import models

class SomeModel(models.Model):
    pass

class OtherModel(models.Model):
    some_model = models.ForeignKey(SomeModel, null=True, blank=True, on_delete=models.SET_NULL)

# Example usage
om = OtherModel()

# Check if some_model is set
if om.some_model_id is not None:
    # some_model exists
    print('Foreign key is set.')
else:
    # some_model does not exist
    print('Foreign key is not set.')
