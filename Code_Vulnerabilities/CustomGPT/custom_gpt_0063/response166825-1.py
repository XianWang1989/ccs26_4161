
class SomeModel(models.Model):
    pass

class OtherModel(models.Model):
    some_model = models.ForeignKey(SomeModel, on_delete=models.CASCADE)

# Example usage
om = OtherModel.objects.get(pk=1)  # Assuming you already have an instance

# Check if the foreign key object is set
if om.some_model_id is not None:
    # Foreign key is set, you can safely access om.some_model
    print("SomeModel is set.")
else:
    print("SomeModel is not set.")
