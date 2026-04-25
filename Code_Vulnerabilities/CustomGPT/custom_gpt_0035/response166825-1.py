
from django.db import models

class SomeModel(models.Model):
    pass

class OtherModel(models.Model):
    some_model = models.ForeignKey(SomeModel, on_delete=models.CASCADE)

# Usage example
om = OtherModel.objects.get(id=1)  # Example to fetch an instance

if om.some_model_id is not None:
    # Foreign key is set
    print("Foreign key is set.")
else:
    # Foreign key is not set
    print("Foreign key is not set.")
