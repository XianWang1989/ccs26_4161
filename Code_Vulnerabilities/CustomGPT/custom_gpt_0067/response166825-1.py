
from django.db import models

class SomeModel(models.Model):
    pass

class OtherModel(models.Model):
    some_model = models.ForeignKey(SomeModel, on_delete=models.CASCADE, null=True)

# Example usage
om = OtherModel()

if om.some_model_id is not None:  # Use the primary key directly
    # The ForeignKey is set
    print("ForeignKey is set.")
else:
    # The ForeignKey is not set
    print("ForeignKey is not set.")
