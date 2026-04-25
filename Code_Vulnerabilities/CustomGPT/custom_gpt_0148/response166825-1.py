
class SomeModel(models.Model):
    pass

class OtherModel(models.Model):
    some_model = models.ForeignKey(SomeModel, on_delete=models.CASCADE, related_name='other_models')

# Usage
om = OtherModel()

# Check if the foreign key is set
if isinstance(om.some_model_id, int):  # Check if the ID is set
    some_model_instance = om.some_model  # This will not throw DoesNotExist
    # Do something with some_model_instance
