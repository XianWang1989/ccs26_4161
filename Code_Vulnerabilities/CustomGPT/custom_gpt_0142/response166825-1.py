
from django.db import models

class SomeModel(models.Model):
    name = models.CharField(max_length=100)

class OtherModel(models.Model):
    some_model = models.ForeignKey(SomeModel, on_delete=models.SET_NULL, null=True)

# Assuming you have an instance of OtherModel
om = OtherModel.objects.get(id=1)  # Replace 1 with your actual ID

# Check if the foreign key is set
if om.some_model_id is not None:
    print("Foreign key is set:", om.some_model)
else:
    print("Foreign key is not set.")
