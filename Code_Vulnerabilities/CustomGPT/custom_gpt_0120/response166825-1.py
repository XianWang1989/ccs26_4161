
from django.db import models

class SomeModel(models.Model):
    name = models.CharField(max_length=100)

class OtherModel(models.Model):
    some_model = models.ForeignKey(SomeModel, on_delete=models.SET_NULL, null=True)

# Assuming you have an instance of OtherModel
om = OtherModel()

# Method to check if some_model is set
def is_some_model_set(other_model_instance):
    return other_model_instance.some_model_id is not None

# Usage
if is_some_model_set(om):
    print("some_model is set.")
else:
    print("some_model is not set.")
