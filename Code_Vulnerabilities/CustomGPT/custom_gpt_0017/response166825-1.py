
from django.db import models

class SomeModel(models.Model):
    pass

class OtherModel(models.Model):
    some_model = models.ForeignKey(SomeModel, on_delete=models.CASCADE)

# Example usage
def check_foreign_key_set(om):
    if om.some_model_id is not None:  # Use the foreign key ID directly
        print("Foreign key is set.")
    else:
        print("Foreign key is not set.")

# Creating an instance of OtherModel and checking the foreign key
om = OtherModel()
check_foreign_key_set(om)
