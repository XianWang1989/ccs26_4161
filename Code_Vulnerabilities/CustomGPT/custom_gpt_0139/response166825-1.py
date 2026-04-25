
from django.db import models

class SomeModel(models.Model):
    # Some fields for SomeModel
    pass

class OtherModel(models.Model):
    some_model = models.ForeignKey(SomeModel, null=True, on_delete=models.SET_NULL)

# Example usage
def check_some_model_set(om):
    if om.some_model_id is not None:
        print("The related SomeModel object is set.")
    else:
        print("The related SomeModel object is not set.")

# Creating an instance of OtherModel without setting the ForeignKey
om = OtherModel()
check_some_model_set(om)  # Output: The related SomeModel object is not set.

# Now let's set the ForeignKey
some_instance = SomeModel()
om.some_model = some_instance
om.save()

check_some_model_set(om)  # Output: The related SomeModel object is set.
