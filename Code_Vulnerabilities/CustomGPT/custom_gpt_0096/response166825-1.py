
from django.db import models

class SomeModel(models.Model):
    name = models.CharField(max_length=100)

class OtherModel(models.Model):
    some_model = models.ForeignKey(SomeModel, on_delete=models.CASCADE)

# Check if a related SomeModel instance is set
def is_some_model_set(other_model_instance):
    return OtherModel.objects.filter(id=other_model_instance.id, some_model__isnull=False).exists()

# Usage
om = OtherModel()  # Ensure you save it first if checking for an existing instance
if is_some_model_set(om):
    print("The foreign key is set!")
else:
    print("The foreign key is not set.")
