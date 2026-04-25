
from django.db import models

class SomeModel(models.Model):
    pass

class OtherModel(models.Model):
    some_model = models.ForeignKey(SomeModel, on_delete=models.CASCADE, null=True)

# Example usage
om = OtherModel.objects.first()  # Assuming you retrieve an instance

if om.some_model_id is not None:  # Check if foreign key id is set
    # Foreign key is set
    print("Foreign key is set.")
else:
    # Foreign key is not set
    print("Foreign key is not set.")
