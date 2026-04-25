
from django.db import models

class SomeModel(models.Model):
    name = models.CharField(max_length=100)

class OtherModel(models.Model):
    some_model = models.ForeignKey(SomeModel, on_delete=models.CASCADE)

# Example usage:
om = OtherModel.objects.select_related('some_model').get(id=1)  # Assuming id=1 exists

if om.some_model_id is not None:
    # some_model is set
    print("Related SomeModel is set:", om.some_model)
else:
    print("Related SomeModel is not set.")
