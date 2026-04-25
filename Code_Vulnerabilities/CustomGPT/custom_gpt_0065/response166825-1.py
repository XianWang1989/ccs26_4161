
class SomeModel(models.Model):
    pass

class OtherModel(models.Model):
    some_model = models.ForeignKey(SomeModel, on_delete=models.CASCADE)

# When retrieving the OtherModel instance
om = OtherModel.objects.select_related('some_model').get(id=some_id)

# Check if some_model is set
if om.some_model_id is not None:
    # some_model is set
    pass
else:
    # some_model is not set
    pass
