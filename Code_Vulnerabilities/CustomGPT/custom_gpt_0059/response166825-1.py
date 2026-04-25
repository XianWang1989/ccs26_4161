
from django.db import models

class SomeModel(models.Model):
    # Your model fields here
    pass

class OtherModel(models.Model):
    some_model = models.ForeignKey(SomeModel, on_delete=models.CASCADE)

# Example usage
om = OtherModel()

# Check if the foreign key is set
if om.some_model_id is not None:
    # The foreign key is set
    pass
else:
    # The foreign key is not set
    pass
