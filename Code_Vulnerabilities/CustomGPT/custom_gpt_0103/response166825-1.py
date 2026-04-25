
class SomeModel(models.Model):
    pass

class OtherModel(models.Model):
    some_model = models.ForeignKey(SomeModel, on_delete=models.SET_NULL, null=True)

# Assuming 'om' is an instance of OtherModel
om = OtherModel.objects.get(pk=1)  # Adjust the pk as needed

# Check if the ForeignKey is set
if om.some_model_id is not None:
    print("Foreign key is set.")
else:
    print("Foreign key is not set.")
