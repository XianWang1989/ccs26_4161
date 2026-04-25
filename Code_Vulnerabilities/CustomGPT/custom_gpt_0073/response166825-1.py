
class SomeModel(models.Model):
    pass

class OtherModel(models.Model):
    some_model = models.ForeignKey(SomeModel, on_delete=models.CASCADE)

# Assuming you have an instance of OtherModel
om = OtherModel()

# Check if the foreign key is set using isnull
if OtherModel.objects.filter(id=om.id, some_model__isnull=False).exists():
    # The foreign key is set
    pass
else:
    # The foreign key is not set
    pass
