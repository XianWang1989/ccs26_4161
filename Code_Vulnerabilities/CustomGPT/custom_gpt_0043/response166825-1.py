
class SomeModel(models.Model):
    # Your SomeModel fields here
    name = models.CharField(max_length=100)

class OtherModel(models.Model):
    some_model = models.ForeignKey(SomeModel, on_delete=models.CASCADE)

# Assuming you have an instance of OtherModel
om = OtherModel()

# Use a query to check if the related object exists
if om.some_model_id is not None:
    # some_model is set, you can safely access it now
    related_obj = om.some_model  # This will not raise DoesNotExist
    print("Related object:", related_obj)
else:
    print("some_model is not set.")
