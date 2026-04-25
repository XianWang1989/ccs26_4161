
from django.db import models

class SomeModel(models.Model):
    pass

class OtherModel(models.Model):
    some_model = models.ForeignKey(SomeModel, on_delete=models.CASCADE, null=True)

# Checking if some_model is set in a queryset
om = OtherModel.objects.first()  # Retrieve the first instance

if om.some_model_id is not None:  # Check the ID directly
    # some_model is set
    print("Foreign key is set.")
else:
    # some_model is not set
    print("Foreign key is not set.")
