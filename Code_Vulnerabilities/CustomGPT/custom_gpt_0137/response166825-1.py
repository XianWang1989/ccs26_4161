
from django.db import models

class SomeModel(models.Model):
    pass

class OtherModel(models.Model):
    some_model = models.ForeignKey(SomeModel, on_delete=models.CASCADE, null=True, blank=True)

# Example usage
om = OtherModel()  # This instance has not been saved and thus doesn't have a foreign key set yet.

# Check if the foreign key is set and safely avoid DoesNotExist:
if om.some_model_id is not None:  # Checks if foreign key ID is set
    # Do something with the related SomeModel instance
    some_instance = om.some_model
    pass
else:
    print("Foreign key is not set.")
