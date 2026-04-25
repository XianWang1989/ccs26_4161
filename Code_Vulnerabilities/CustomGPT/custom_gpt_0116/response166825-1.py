
from django.db import models

class SomeModel(models.Model):
    name = models.CharField(max_length=100)

class OtherModel(models.Model):
    some_model = models.ForeignKey(SomeModel, null=True, on_delete=models.SET_NULL)

# Create an instance of OtherModel
om = OtherModel()

# Check if some_model is set
if om.some_model_id is not None:
    # Safe to access the related object
    related_instance = om.some_model
    print(f'Related instance: {related_instance.name}')
else:
    print('some_model is not set')
