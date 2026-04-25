
class SomeModel(models.Model):
    pass

class OtherModel(models.Model):
    some_model = models.ForeignKey(SomeModel, on_delete=models.SET_NULL, null=True, related_name='other_models')

# Example usage
om = OtherModel.objects.first()  # Fetch an instance of OtherModel

# Check if the foreign key is set
if om.some_model_id is not None:
    some_model_instance = om.some_model
    # Do something with some_model_instance
else:
    # Handle the case where the foreign key is not set
    pass
