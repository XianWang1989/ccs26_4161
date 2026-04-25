
from django.db import models

class SomeModel(models.Model):
    name = models.CharField(max_length=100)

class OtherModel(models.Model):
    some_model = models.ForeignKey(SomeModel, on_delete=models.CASCADE, null=True, blank=True)

# Example usage:
om = OtherModel()

# Check if the foreign key is set
if om.some_model_id is not None:
    # This will not throw an exception
    some_model_instance = SomeModel.objects.filter(id=om.some_model_id).first()
    if some_model_instance:
        print("Foreign key is set and the related SomeModel instance exists.")
    else:
        print("Foreign key is set but the related SomeModel instance does not exist.")
else:
    print("Foreign key is not set.")
