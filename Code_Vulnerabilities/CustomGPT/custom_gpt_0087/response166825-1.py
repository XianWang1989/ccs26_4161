
from django.db import models

class SomeModel(models.Model):
    # Your fields here
    pass

class OtherModel(models.Model):
    some_model = models.ForeignKey(SomeModel, on_delete=models.CASCADE, null=True)

# Usage Example
om = OtherModel.objects.create()  # Assuming you have created an instance

# Check if the foreign key object is set
if om.some_model_id is not None:
    # This means the foreign key is set
    some_model_exists = SomeModel.objects.filter(id=om.some_model_id).exists()
    if some_model_exists:
        print("The related SomeModel object exists.")
    else:
        print("The related SomeModel object does not exist.")
else:
    print("The foreign key is not set.")
