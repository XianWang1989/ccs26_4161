
class SomeModel(models.Model):
    # Fields for SomeModel
    name = models.CharField(max_length=100)

class OtherModel(models.Model):
    some_model = models.ForeignKey(SomeModel, on_delete=models.SET_NULL, null=True)

# Create an instance of OtherModel
om = OtherModel()

# Check if some_model is set
if om.some_model_id is not None:
    # some_model is set, you can safely access it
    related_instance = om.some_model
    print(f"Related instance: {related_instance}")
else:
    # some_model is not set (i.e., it is None)
    print("No related SomeModel instance is set.")
