
from django.db import models

class SomeModel(models.Model):
    pass

class OtherModel(models.Model):
    some_model = models.ForeignKey(SomeModel, on_delete=models.CASCADE, null=True)

# Checking if the foreign key is set
om = OtherModel()

# Use the 'isnull' filter in a queryset
if not OtherModel.objects.filter(pk=om.pk, some_model__isnull=True).exists():
    # The foreign key 'some_model' is set
    print("Foreign key is set.")
else:
    # The foreign key 'some_model' is not set
    print("Foreign key is not set.")
