
from django.db import models

class SomeModel(models.Model):
    pass

class OtherModel(models.Model):
    some_model = models.ForeignKey(SomeModel, on_delete=models.CASCADE, null=True)  # Allow null references

om = OtherModel()

# Check if the ForeignKey is set
if om.some_model is not None:
    print("ForeignKey is set.")
else:
    print("ForeignKey is not set.")
