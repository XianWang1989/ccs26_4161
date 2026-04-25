
from django.db import models

class SomeModel(models.Model):
    name = models.CharField(max_length=100)

class OtherModel(models.Model):
    some_model = models.ForeignKey(SomeModel, on_delete=models.CASCADE, null=True, blank=True)

# Assuming you have an instance of OtherModel
om = OtherModel()

# Check if the ForeignKey is set using a queryset
if om.some_model_id is not None:
    print("The ForeignKey is set.")
else:
    print("The ForeignKey is not set.")
