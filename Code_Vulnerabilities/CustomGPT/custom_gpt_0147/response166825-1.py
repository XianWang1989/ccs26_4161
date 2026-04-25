
from django.db import models

class SomeModel(models.Model):
    name = models.CharField(max_length=100)

class OtherModel(models.Model):
    some_model = models.ForeignKey(SomeModel, on_delete=models.SET_NULL, null=True)

# Example usage
def check_foreign_key_set(other_model_id):
    try:
        om = OtherModel.objects.get(id=other_model_id)
        if om.some_model_id is not None:  # Check if ForeignKey is set
            print("SomeModel is set.")
        else:
            print("SomeModel is not set.")
    except OtherModel.DoesNotExist:
        print("OtherModel does not exist.")

# Call the function with a specific ID
check_foreign_key_set(1)
