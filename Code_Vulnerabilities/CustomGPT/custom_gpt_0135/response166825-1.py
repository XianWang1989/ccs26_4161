
from django.db import models

class SomeModel(models.Model):
    name = models.CharField(max_length=255)

class OtherModel(models.Model):
    some_model = models.ForeignKey(SomeModel, on_delete=models.CASCADE, null=True)

# Assume we have an instance of OtherModel
om = OtherModel()

# Check if the foreign key object is set using exists()
if om.some_model_id is not None:
    some_model_exists = SomeModel.objects.filter(id=om.some_model_id).exists()
    if some_model_exists:
        # Proceed with logic when the related object exists
        pass
else:
    # The foreign key is not set
    pass
