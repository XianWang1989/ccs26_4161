
from django.db import models

class SomeModel(models.Model):
    name = models.CharField(max_length=100)

class OtherModel(models.Model):
    some_model = models.ForeignKey(SomeModel, on_delete=models.SET_NULL, null=True)

# Example usage
om = OtherModel.objects.get(id=1)  # Ensure you retrieve an instance correctly

if om.some_model_id is not None:
    # Do something with the linked SomeModel instance
    print("The foreign key is set.")
else:
    print("The foreign key is not set.")
