
class SomeModel(models.Model):
    pass

class OtherModel(models.Model):
    some_model = models.ForeignKey(SomeModel, null=True, on_delete=models.CASCADE)

# Example usage
om = OtherModel.objects.get(id=1)  # Assume we have an instance with id=1

# Check if the foreign key is set
if om.some_model_id is not None:
    # Proceed with the logic
    print("Foreign key is set.")
else:
    print("Foreign key is not set.")
