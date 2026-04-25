
from django.core.exceptions import ObjectDoesNotExist

class SomeModel(models.Model):
    pass

class OtherModel(models.Model):
    some_model = models.ForeignKey(SomeModel, null=True, on_delete=models.SET_NULL)

# Usage
om = OtherModel()

# Check if the foreign key is set
if om.some_model_id is not None:
    try:
        om.some_model  # This will not throw if it's not set
        print("Foreign key is set.")
    except ObjectDoesNotExist:
        print("Foreign key reference does not exist.")
else:
    print("Foreign key is not set.")
