
from django.db import models

class SomeModel(models.Model):
    pass

class OtherModel(models.Model):
    some_model = models.ForeignKey(SomeModel, on_delete=models.SET_NULL, null=True)

# Check if the foreign key is set
om = OtherModel.objects.get(pk=1)  # Example fetching an instance

# Check if the foreign key is set using the 'isnull' method
if om.some_model_id is not None:
    print("Foreign key is set.")
else:
    print("Foreign key is not set.")
