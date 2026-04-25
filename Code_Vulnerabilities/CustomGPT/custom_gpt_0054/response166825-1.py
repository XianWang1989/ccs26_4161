
class SomeModel(models.Model):
    pass

class OtherModel(models.Model):
    some_model = models.ForeignKey(SomeModel, on_delete=models.CASCADE, null=True)

# Create an instance of OtherModel without setting some_model
om = OtherModel()

# Check if the foreign key is set
if om.some_model_id is not None:
    # Foreign key is set
    # You can safely access om.some_model here
    pass
else:
    # Foreign key is not set
    pass
