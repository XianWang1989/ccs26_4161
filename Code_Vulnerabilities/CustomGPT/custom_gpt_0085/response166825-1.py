
from django.db import models

class SomeModel(models.Model):
    pass

class OtherModel(models.Model):
    some_model = models.ForeignKey(SomeModel, null=True, on_delete=models.SET_NULL)

om = OtherModel.objects.get(id=1)  # Assuming you get an instance of OtherModel

# Check if the foreign key is set
if om.some_model_id is not None:
    # The foreign key object is set
    print("Foreign key is set.")
else:
    print("Foreign key is not set.")
