
from django.db import models

class SomeModel(models.Model):
    # Your fields here
    name = models.CharField(max_length=100)

class OtherModel(models.Model):
    some_model = models.ForeignKey(SomeModel, on_delete=models.SET_NULL, null=True)

# Creating an instance of OtherModel
om = OtherModel()

# Method to check if ForeignKey is set
def is_some_model_set(other_model_instance):
    return other_model_instance.some_model_id is not None

# Usage
if is_some_model_set(om):
    print("The ForeignKey is set.")
else:
    print("The ForeignKey is not set.")
