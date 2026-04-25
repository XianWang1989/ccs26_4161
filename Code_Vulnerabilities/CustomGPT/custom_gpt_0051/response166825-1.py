
from django.db import models

class SomeModel(models.Model):
    pass

class OtherModel(models.Model):
    some_model = models.ForeignKey(SomeModel, on_delete=models.SET_NULL, null=True)

# Assuming `om` is an instance of OtherModel
om = OtherModel()

# Check if the foreign key is set using a query
is_some_model_set = om.some_model_id is not None

if is_some_model_set:
    # Foreign key is set
    print("Foreign key is set.")
else:
    # Foreign key is not set
    print("Foreign key is not set.")
