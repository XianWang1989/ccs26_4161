
from django.db import models

class SomeModel(models.Model):
    pass

class OtherModel(models.Model):
    some_model = models.ForeignKey(SomeModel, on_delete=models.CASCADE, null=True)

# Example usage
om = OtherModel()  # Assuming this instance has not been saved yet

def is_some_model_set(instance):
    return instance.some_model_id is not None

# Check if foreign key is set
if is_some_model_set(om):
    # Do something with om.some_model
    pass
else:
    # Handle the case where some_model is not set
    pass
