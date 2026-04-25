
from django.db import models

class SomeModel(models.Model):
    pass

class OtherModel(models.Model):
    some_model = models.ForeignKey(SomeModel, null=True, on_delete=models.CASCADE)

# Example usage
def check_foreign_key_set(om):
    if om.some_model_id is not None:
        # Foreign key is set; you can access om.some_model here
        some_model_instance = om.some_model
        # Do something with some_model_instance
    else:
        # Foreign key is not set
        pass

# Assuming om is an instance of OtherModel
om = OtherModel()
check_foreign_key_set(om)
