
from django.db import models

class SomeModel(models.Model):
    name = models.CharField(max_length=100)

class OtherModel(models.Model):
    some_model = models.ForeignKey(SomeModel, on_delete=models.SET_NULL, null=True, related_name='other_models')

# Example usage
om = OtherModel()

# Instead of using try...except:
if om.some_model_id is not None:  # Check the foreign key field directly
    some_model_instance = om.some_model  # This will not raise DoesNotExist
    print("Foreign key is set:", some_model_instance)
else:
    print("Foreign key is not set.")
