
class SomeModel(models.Model):
    # Fields for SomeModel
    name = models.CharField(max_length=100)

class OtherModel(models.Model):
    some_model = models.ForeignKey(SomeModel, on_delete=models.CASCADE, null=True, blank=True)

om = OtherModel()

# Check if the foreign key reference is set and the related object exists
if om.some_model_id is not None and SomeModel.objects.filter(id=om.some_model_id).exists():
    print("The related object is set.")
else:
    print("The related object is not set.")
