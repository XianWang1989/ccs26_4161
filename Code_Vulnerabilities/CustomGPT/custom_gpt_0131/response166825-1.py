
from django.db import models

class SomeModel(models.Model):
    name = models.CharField(max_length=100)

class OtherModel(models.Model):
    some_model = models.ForeignKey(SomeModel, on_delete=models.SET_NULL, null=True)

# Assuming you have an instance of OtherModel
om = OtherModel.objects.get(id=1)  # Fetching an instance for the example

# Checking if the foreign key is set using 'isnull'
if om.some_model_id is not None:
    print("The related SomeModel object is set.")
else:
    print("The related SomeModel object is not set.")

# Alternatively, prefetch related objects can be used when querying multiple instances
other_models = OtherModel.objects.prefetch_related('some_model').all()
for other in other_models:
    if other.some_model is not None:
        print(f"{other.id} has a related SomeModel object: {other.some_model.name}")
    else:
        print(f"{other.id} does not have a related SomeModel object.")
