
from django.db import models

class SomeModel(models.Model):
    pass

class OtherModel(models.Model):
    some_model = models.ForeignKey(SomeModel, on_delete=models.SET_NULL, null=True)

# Example usage
om = OtherModel.objects.get(id=1)  # Assuming this object already exists

# Check if some_model is set
if om.some_model_id is not None:
    # some_model is set
    print("some_model is set.")
else:
    # some_model is not set
    print("some_model is not set.")
