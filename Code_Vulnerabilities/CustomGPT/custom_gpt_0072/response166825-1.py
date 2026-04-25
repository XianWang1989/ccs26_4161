
from django.db import models

class SomeModel(models.Model):
    name = models.CharField(max_length=100)

class OtherModel(models.Model):
    some_model = models.ForeignKey(SomeModel, on_delete=models.SET_NULL, null=True)

# Checking if ForeignKey is set
om = OtherModel.objects.get(id=1)  # Replace with your logic to get the instance

if om.some_model_id is not None:
    # ForeignKey is set
    some_model_instance = om.some_model
else:
    # ForeignKey is not set
    pass
