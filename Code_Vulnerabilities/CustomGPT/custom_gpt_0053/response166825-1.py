
from django.db import models

class SomeModel(models.Model):
    name = models.CharField(max_length=100)

class OtherModel(models.Model):
    some_model = models.ForeignKey(SomeModel, null=True, on_delete=models.SET_NULL)

# Checking if the foreign key is set
om = OtherModel.objects.get(pk=1)  # Get an instance by its primary key

# Method to check if foreign key is set
def is_some_model_set(instance):
    return instance.some_model_id is not None

if is_some_model_set(om):
    print("some_model is set.")
else:
    print("some_model is not set.")
