
from django.db import models

class SomeModel(models.Model):
    name = models.CharField(max_length=255)

class OtherModel(models.Model):
    some_model = models.ForeignKey(SomeModel, on_delete=models.CASCADE)

# Checking if foreign key is set
om = OtherModel()

# Instead of accessing the attribute directly,
# you can check if the related object exists
if om.some_model_id is not None:
    # The foreign key is set
    pass
else:
    # The foreign key is not set
    pass
