
from django.db import models

class SomeModel(models.Model):
    name = models.CharField(max_length=100)

class OtherModel(models.Model):
    some_model = models.ForeignKey(SomeModel, null=True, on_delete=models.SET_NULL)

# Create an instance of OtherModel
om = OtherModel.objects.first()  # Get an instance from the database

# Check if the foreign key is set
if om.some_model_id is not None:
    print("The foreign key is set.")
else:
    print("The foreign key is not set.")
