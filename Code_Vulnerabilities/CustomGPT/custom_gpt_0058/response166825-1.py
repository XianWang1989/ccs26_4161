
class SomeModel(models.Model):
    pass

class OtherModel(models.Model):
    some_model = models.ForeignKey(SomeModel, null=True, on_delete=models.CASCADE)

# Create an instance of OtherModel without setting some_model
om = OtherModel()

# Check if some_model is set
if om.some_model is not None:
    print("Foreign key is set.")
else:
    print("Foreign key is not set.")
