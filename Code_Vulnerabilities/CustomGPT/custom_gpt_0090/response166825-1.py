
from django.db import models

class SomeModel(models.Model):
    pass

class OtherModel(models.Model):
    some_model = models.ForeignKey(SomeModel, on_delete=models.SET_NULL, null=True)

# Assuming 'om' is an instance of OtherModel
om = OtherModel.objects.get(id=some_id)  # Replace 'some_id' with the actual ID.

if om.some_model_id is not None:
    # some_model is set
    some_model_instance = om.some_model
else:
    # some_model is not set
    pass
