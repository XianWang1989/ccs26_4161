
class SomeModel(models.Model):
    pass

class OtherModel(models.Model):
    some_model = models.ForeignKey(SomeModel, null=True, on_delete=models.SET_NULL)

# Usage
om = OtherModel()

# Check if the foreign key is set
if om.some_model_id is not None:
    # Your logic here
    print("The foreign key is set")
else:
    print("The foreign key is not set")
