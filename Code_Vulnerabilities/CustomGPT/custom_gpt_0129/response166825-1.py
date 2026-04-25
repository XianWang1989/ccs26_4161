
from django.db import models

class SomeModel(models.Model):
    name = models.CharField(max_length=100)

class OtherModel(models.Model):
    some_model = models.ForeignKey(SomeModel, on_delete=models.CASCADE, null=True, blank=True)

# Example usage:
om = OtherModel()

# Checking if some_model is set
if om.some_model_id is not None:
    print("Foreign key is set.")
else:
    print("Foreign key is not set.")

# Alternatively, when querying the database
if OtherModel.objects.filter(some_model__isnull=False).exists():
    print("There are OtherModel instances with a ForeignKey set.")
else:
    print("No OtherModel instances with a ForeignKey set.")
