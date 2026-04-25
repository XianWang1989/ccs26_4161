
from django.db import models

class SomeModel(models.Model):
    # Define fields here
    pass

class OtherModel(models.Model):
    some_model = models.ForeignKey(SomeModel, null=True, on_delete=models.CASCADE)

# When checking if the foreign key is set
om = OtherModel.objects.first()  # Fetching an instance or creating one

# Check if some_model is set
if om.some_model_id is not None:  # This checks if the foreign key value is set
    print("Foreign key is set.")
else:
    print("Foreign key is not set.")
