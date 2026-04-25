
class SomeModel(models.Model):
    pass

class OtherModel(models.Model):
    some_model = models.ForeignKey(SomeModel, null=True, on_delete=models.SET_NULL)

# Assuming you have an instance of OtherModel
om = OtherModel()

# Use the isnull check to determine if some_model is set
if om.some_model_id is not None:  # Check the foreign key field directly
    # Do something if some_model is set
    pass
else:
    # Handle the case where it is not set
    pass
