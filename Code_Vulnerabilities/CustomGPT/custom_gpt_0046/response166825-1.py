
from django.db import models

class SomeModel(models.Model):
    pass

class OtherModel(models.Model):
    some_model = models.ForeignKey(SomeModel, on_delete=models.CASCADE, null=True)

# Assuming you have an instance of OtherModel
om = OtherModel.objects.get(id=1)  # Example retrieval; replace with actual logic

# Check if the foreign key is set
if om.some_model_id is not None:
    # The related SomeModel instance exists
    related_instance = om.some_model
    # Do something with related_instance
else:
    # No related SomeModel instance
    pass
