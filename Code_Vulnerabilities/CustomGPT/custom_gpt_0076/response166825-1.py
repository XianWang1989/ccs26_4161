
from django.db import models

class SomeModel(models.Model):
    # Your fields here
    pass

class OtherModel(models.Model):
    some_model = models.ForeignKey(SomeModel, on_delete=models.CASCADE)

# Example usage
om = OtherModel()

# Checking if the foreign key is set
if om.some_model_id is not None:
    # This will be true if some_model is set
    some_model_exists = SomeModel.objects.filter(id=om.some_model_id).exists()
    if some_model_exists:
        # Proceed knowing the related object exists
        pass
