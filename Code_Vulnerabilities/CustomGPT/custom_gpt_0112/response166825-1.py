
from django.db import models

class SomeModel(models.Model):
    # Example fields for SomeModel
    name = models.CharField(max_length=100)

class OtherModel(models.Model):
    some_model = models.ForeignKey(SomeModel, on_delete=models.SET_NULL, null=True)

# Create an instance of OtherModel
om = OtherModel()

# Save the instance to the database first
om.save()

# Check if ForeignKey is set using a query
if OtherModel.objects.filter(id=om.id, some_model__isnull=False).exists():
    print("Foreign key is set")
else:
    print("Foreign key is not set")
