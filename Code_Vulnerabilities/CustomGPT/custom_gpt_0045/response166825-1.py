
class SomeModel(models.Model):
    pass

class OtherModel(models.Model):
    some_model = models.ForeignKey(SomeModel, on_delete=models.SET_NULL, null=True)

# Assuming om is an instance of OtherModel:
om = OtherModel()

# Check if the ForeignKey reference is set
if om.some_model_id is not None:
    # Use the ID to check existence without hitting the foreign key
    if SomeModel.objects.filter(id=om.some_model_id).exists():
        print("The related SomeModel object exists.")
    else:
        print("The related SomeModel object does not exist.")
else:
    print("No SomeModel object is set.")
