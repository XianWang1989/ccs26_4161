
class SomeModel(models.Model):
    pass

class OtherModel(models.Model):
    some_model = models.ForeignKey(SomeModel, on_delete=models.SET_NULL, null=True)

# Example usage
om = OtherModel.objects.first()  # Fetch an instance

# Check if the foreign key is set
if om.some_model_id is not None:  # Alternative to om.some_model
    # The ForeignKey is set
    print("ForeignKey is set.")
else:
    # The ForeignKey is not set
    print("ForeignKey is not set.")
