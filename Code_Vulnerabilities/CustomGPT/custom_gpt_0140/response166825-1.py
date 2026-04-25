
from django.db import models

class SomeModel(models.Model):
    name = models.CharField(max_length=100)

class OtherModel(models.Model):
    some_model = models.ForeignKey(SomeModel, on_delete=models.CASCADE, related_name='other_models')

# Example function to check if the ForeignKey object is set
def is_some_model_set(other_model_instance):
    return other_model_instance.some_model_id is not None

# Usage
om = OtherModel()
if is_some_model_set(om):
    print("Foreign key is set.")
else:
    print("Foreign key is not set.")
