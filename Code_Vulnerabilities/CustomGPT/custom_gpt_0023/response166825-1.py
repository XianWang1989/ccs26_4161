
from django.db import models

class SomeModel(models.Model):
    # Fields here
    pass

class OtherModel(models.Model):
    some_model = models.ForeignKey(SomeModel, on_delete=models.SET_NULL, null=True)

# Create an instance of OtherModel
om = OtherModel.objects.create()

# Check if the foreign key is set
if om.some_model_id is not None:
    # The ForeignKey is set
    print("Foreign key is set.")
else:
    # The ForeignKey is not set
    print("Foreign key is not set.")
