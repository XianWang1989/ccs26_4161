
from django.db import models

class SomeModel(models.Model):
    name = models.CharField(max_length=255)

class OtherModel(models.Model):
    some_model = models.ForeignKey(SomeModel, on_delete=models.CASCADE, null=True)

# Checking if the ForeignKey is set
om = OtherModel.objects.first()  # Retrieve an instance of OtherModel

if om.some_model_id is not None:
    # Foreign key is set
    print(f'Foreign key is set to: {om.some_model}')
else:
    # Foreign key is not set
    print('Foreign key is not set')
