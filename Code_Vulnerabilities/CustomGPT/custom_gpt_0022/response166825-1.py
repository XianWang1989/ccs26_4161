
class SomeModel(models.Model):
    pass

class OtherModel(models.Model):
    some_model = models.ForeignKey(SomeModel, on_delete=models.CASCADE, null=True, blank=True)

# Example usage
om = OtherModel()

# Check if the foreign key is set
if om.some_model_id is not None:
    # Do something with om.some_model
    pass
else:
    # The foreign key is not set
    pass
