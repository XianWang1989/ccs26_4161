
from django.db import models

class SomeModel(models.Model):
    # Your fields here
    name = models.CharField(max_length=100)

class OtherModel(models.Model):
    some_model = models.ForeignKey(SomeModel, null=True, on_delete=models.SET_NULL)

# Creating an instance of OtherModel
om = OtherModel()

# Check if the ForeignKey attribute is set
if om.some_model is not None:
    print("ForeignKey is set")
else:
    print("ForeignKey is not set")
