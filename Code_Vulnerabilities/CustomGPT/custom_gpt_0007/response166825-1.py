
class SomeModel(models.Model):
    # Your fields here
    pass

class OtherModel(models.Model):
    some_model = models.ForeignKey(SomeModel, on_delete=models.CASCADE)

# Assuming `om` is an instance of OtherModel that has been created
om = OtherModel.objects.get(id=1)  # For example, fetching an instance by ID

# Check if the foreign key reference is set
if om.some_model_id is not None:
    # The foreign key is set, you can proceed with your logic
    print("Foreign key is set:", om.some_model_id)
else:
    # The foreign key hasn't been set
    print("Foreign key is not set.")
