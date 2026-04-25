
class SomeModel(models.Model):
    pass

class OtherModel(models.Model):
    some_model = models.ForeignKey(SomeModel, on_delete=models.SET_NULL, null=True)

# Creating an instance of OtherModel
om = OtherModel()

# Checking if the foreign key is set without raising exceptions
if om.some_model_id is not None:
    # Do something with om.some_model
    pass
else:
    # Handle the case where no related object is set
    pass
