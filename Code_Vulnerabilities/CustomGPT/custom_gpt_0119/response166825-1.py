
class SomeModel(models.Model):
    pass

class OtherModel(models.Model):
    some_model = models.ForeignKey(SomeModel, on_delete=models.CASCADE)

# Create an instance of OtherModel
om = OtherModel()

# Check if the related SomeModel instance exists
if SomeModel.objects.filter(id=om.some_model_id).exists():
    # The related object exists
    pass
else:
    # The related object does not exist
    pass
