
from django.db import models

class SomeModel(models.Model):
    # Your fields here
    name = models.CharField(max_length=100)

class OtherModel(models.Model):
    some_model = models.ForeignKey(SomeModel, on_delete=models.CASCADE, related_name='other_models')

# Create an instance of OtherModel
om = OtherModel()

# Using `exists()` to check if the foreign key is set
if om.some_model_id is not None:
    related_obj = SomeModel.objects.filter(id=om.some_model_id).exists()
    if related_obj:
        # The related SomeModel object exists
        print("SomeModel object is set.")
    else:
        print("SomeModel object does not exist.")
else:
    print("Foreign key is not set.")
