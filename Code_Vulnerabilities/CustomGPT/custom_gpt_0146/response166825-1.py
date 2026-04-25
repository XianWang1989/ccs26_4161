
from django.db import models

class SomeModel(models.Model):
    # Sample fields for SomeModel
    name = models.CharField(max_length=100)

class OtherModel(models.Model):
    some_model = models.ForeignKey(SomeModel, null=True, on_delete=models.SET_NULL)

# Creating an instance of OtherModel
om = OtherModel()

# A nice way to check if the foreign key is set
# This can be done on instances saved to the database or unsaved instances if needed.
def is_foreign_key_set(other_model):
    return other_model.some_model_id is not None

# Example usage:
if is_foreign_key_set(om):
    print("Foreign key is set.")
else:
    print("Foreign key is not set.")
