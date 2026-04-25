
class SomeModel(models.Model):
    pass

class OtherModel(models.Model):
    some_model = models.ForeignKey(SomeModel, on_delete=models.CASCADE)

# Create an instance of OtherModel
om = OtherModel()

# Check if the foreign key is set by checking if the primary key is None
if om.some_model_id is not None:  # Use .some_model_id for the underlying ID
    # Now you can safely access om.some_model
    print("Foreign key is set.")
else:
    print("Foreign key is not set.")
