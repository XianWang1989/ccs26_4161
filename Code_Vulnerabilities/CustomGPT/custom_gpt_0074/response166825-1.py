
class SomeModel(models.Model):
    pass

class OtherModel(models.Model):
    some_model = models.ForeignKey(SomeModel, on_delete=models.CASCADE, null=True, blank=True)

# Creating an instance of OtherModel
om = OtherModel()

# Check if the ForeignKey is set
if om.some_model_id is None:
    print("The ForeignKey is not set.")
else:
    print("The ForeignKey is set.")
