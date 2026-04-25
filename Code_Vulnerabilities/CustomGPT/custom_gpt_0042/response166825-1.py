
from django.db import models

class SomeModel(models.Model):
    name = models.CharField(max_length=100)

class OtherModel(models.Model):
    some_model = models.ForeignKey(SomeModel, on_delete=models.SET_NULL, null=True)

# Example usage
def check_foreign_key_set(om):
    # Ensure the instance has a primary key (i.e., it's saved)
    if om.pk is None:
        # Object isn't saved yet
        return False

    # Check if related object exists
    return SomeModel.objects.filter(id=om.some_model_id).exists()

# Create an instance of OtherModel
om = OtherModel()
# Check if the foreign key is set
if check_foreign_key_set(om):
    # Do something
    print("Foreign key is set.")
else:
    print("Foreign key is not set.")
