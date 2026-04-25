
from django.db import models

class SomeModel(models.Model):
    pass

class OtherModel(models.Model):
    some_model = models.ForeignKey(SomeModel, on_delete=models.CASCADE)

# Create an instance of OtherModel
om = OtherModel()

# Check if the ForeignKey object is set
if om.some_model_id is not None and SomeModel.objects.filter(id=om.some_model_id).exists():
    # The ForeignKey is set and the referenced object exists
    pass
else:
    # The ForeignKey is not set or the referenced object does not exist
    pass
