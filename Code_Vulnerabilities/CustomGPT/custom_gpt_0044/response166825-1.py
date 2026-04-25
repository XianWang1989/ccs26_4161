
class SomeModel(models.Model):
    pass

class OtherModel(models.Model):
    some_model = models.ForeignKey(SomeModel, on_delete=models.CASCADE)

# Check if the ForeignKey is set
om = OtherModel()

# Example of checking if the foreign key is set using a queryset
if OtherModel.objects.filter(pk=om.pk, some_model__isnull=False).exists():
    # Foreign key is set
    pass
else:
    # Foreign key is not set
    pass
