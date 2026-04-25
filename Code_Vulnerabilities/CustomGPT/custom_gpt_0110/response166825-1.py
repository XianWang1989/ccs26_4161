
from django.db import models

class SomeModel(models.Model):
    pass

class OtherModel(models.Model):
    some_model = models.ForeignKey(SomeModel, on_delete=models.SET_NULL, null=True)

# Assuming `om` is an instance of OtherModel
om = OtherModel()

# Check if the foreign key is set
if om.some_model_id is not None:
    # Access the related SomeModel instance safely
    some_model_instance = om.some_model
    # Do something with some_model_instance
    print("Foreign key is set:", some_model_instance)
else:
    print("Foreign key is not set.")
