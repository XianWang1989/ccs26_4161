
from django.db import models

class SomeModel(models.Model):
    pass

class OtherModel(models.Model):
    some_model = models.ForeignKey(SomeModel, on_delete=models.CASCADE, null=True)

# Create an instance of OtherModel
om = OtherModel()

# Check if the foreign key object is set
if om.some_model_id:  # This checks if the foreign key field is set
    some_model_instance = om.some_model
else:
    print("Foreign key is not set.")
