
class SomeModel(models.Model):
    pass

class OtherModel(models.Model):
    some_model = models.ForeignKey(SomeModel, on_delete=models.SET_NULL, null=True)

# Example usage
om = OtherModel()

# Check if the foreign key is set
if om.some_model_id is not None:
    # Foreign key is set, you can access it safely
    some_instance = om.some_model
    print(some_instance)
else:
    print("The foreign key is not set.")
