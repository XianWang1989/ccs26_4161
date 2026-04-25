
from django.db import models

class SomeModel(models.Model):
    pass

class OtherModel(models.Model):
    some_model = models.ForeignKey(SomeModel, on_delete=models.CASCADE)

# Create an instance of OtherModel
om = OtherModel()

# Use the isnull query to check if the foreign key is set
if not OtherModel.objects.filter(id=om.id, some_model__isnull=True).exists():
    # The foreign key is set
    print("some_model is set")
else:
    # The foreign key is not set
    print("some_model is not set")
