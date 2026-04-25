
class SomeModel(models.Model):
    pass

class OtherModel(models.Model):
    some_model = models.ForeignKey(SomeModel, on_delete=models.CASCADE, null=True)

# Assuming 'om' is an instance of OtherModel
om = OtherModel.objects.get(pk=some_id)  # Replace some_id with your actual ID

# Check if the foreign key is set
if om.some_model_id is not None:
    print("some_model is set:", om.some_model)
else:
    print("some_model is not set.")
