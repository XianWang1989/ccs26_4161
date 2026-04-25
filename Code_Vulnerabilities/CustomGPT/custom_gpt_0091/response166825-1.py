
from django.db import models

class SomeModel(models.Model):
    pass

class OtherModel(models.Model):
    some_model = models.ForeignKey(SomeModel, null=True, on_delete=models.SET_NULL)

# Assuming you're working within a view or similar context
om = OtherModel.objects.create()  # Example of creating an instance

# Check if the foreign key is set
if om.some_model_id is not None:
    # Do something if the foreign key is set
    print("SomeModel is set.")
else:
    # Handle the case where it's not set
    print("SomeModel is not set.")
