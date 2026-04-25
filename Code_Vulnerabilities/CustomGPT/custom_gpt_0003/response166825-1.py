
from django.db import models

class SomeModel(models.Model):
    name = models.CharField(max_length=100)

class OtherModel(models.Model):
    some_model = models.ForeignKey(SomeModel, on_delete=models.CASCADE, null=True, blank=True)  # Added null=True and blank=True

# Example usage
om = OtherModel()

# Check if the foreign key reference is set
if isinstance(om.some_model, SomeModel):
    print("The foreign key is set.")
else:
    print("The foreign key is not set.")
