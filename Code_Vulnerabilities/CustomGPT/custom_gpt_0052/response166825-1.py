
from django.db import models

class SomeModel(models.Model):
    name = models.CharField(max_length=100)

class OtherModel(models.Model):
    some_model = models.ForeignKey(SomeModel, on_delete=models.SET_NULL, null=True)

# Assuming you have an instance of OtherModel
om = OtherModel.objects.get(id=1)  # Replace with actual ID or query

# Check if the foreign key is set
if om.some_model_id is not None:  # Checks if the foreign key ID is not None
    # The related SomeModel object is set
    related_object = om.some_model
    print(f"Related object: {related_object.name}")
else:
    print("The foreign key is not set.")
