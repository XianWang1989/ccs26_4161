
from django.db import models

class SomeModel(models.Model):
    # Fields for SomeModel
    name = models.CharField(max_length=100)

class OtherModel(models.Model):
    some_model = models.ForeignKey(SomeModel, on_delete=models.SET_NULL, null=True)

# Assuming you have an instance of OtherModel
om = OtherModel.objects.filter(id=some_id).first()  # Replace 'some_id' with the actual ID

if om and om.some_model_id is not None:
    # do something with om.some_model
    print(om.some_model.name)
else:
    print("No related SomeModel is set.")
