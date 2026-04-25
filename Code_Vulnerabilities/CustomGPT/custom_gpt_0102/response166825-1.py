
class SomeModel(models.Model):
    pass

class OtherModel(models.Model):
    some_model = models.ForeignKey(SomeModel, on_delete=models.CASCADE)

# Instance of OtherModel
om = OtherModel.objects.get(pk=your_object_id)  # Replace with your actual object ID

# Check if the ForeignKey is set
if om.some_model_id is not None:  # This checks the ID directly
    # ForeignKey is set
    print("ForeignKey is set.")
else:
    # ForeignKey is not set
    print("ForeignKey is not set.")
