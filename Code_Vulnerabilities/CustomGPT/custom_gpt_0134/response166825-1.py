
from django.db import models

class SomeModel(models.Model):
    name = models.CharField(max_length=100)

class OtherModel(models.Model):
    some_model = models.ForeignKey(SomeModel, on_delete=models.CASCADE, null=True)

# Create an instance of OtherModel
om = OtherModel()

# Check if the foreign key is set
if om.some_model_id is not None:
    print("Foreign key is set.")
else:
    print("Foreign key is not set.")
