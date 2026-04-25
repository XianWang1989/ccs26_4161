
class SomeModel(models.Model):
    pass

class OtherModel(models.Model):
    some_model = models.ForeignKey(SomeModel, on_delete=models.CASCADE)

# Usage example
om = OtherModel()

# Check if the foreign key is set
if om.some_model_id is not None:
    # The foreign key is set
    print("Foreign key is set.")
else:
    # The foreign key is not set
    print("Foreign key is not set.")
