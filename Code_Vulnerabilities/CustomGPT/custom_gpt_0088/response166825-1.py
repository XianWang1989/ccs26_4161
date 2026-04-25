
from django.db import models

class SomeModel(models.Model):
    name = models.CharField(max_length=100)

class OtherModel(models.Model):
    some_model = models.ForeignKey(SomeModel, on_delete=models.SET_NULL, null=True)

    def is_some_model_set(self):
        return self.some_model_id is not None

# Usage
om = OtherModel()

if om.is_some_model_set():
    # SomeModel instance is set; proceed with your logic here
    print("Foreign key is set.")
else:
    print("Foreign key is not set.")
