
class SomeModel(models.Model):
    pass

class OtherModel(models.Model):
    some_model = models.ForeignKey(SomeModel, on_delete=models.CASCADE, null=True)

om = OtherModel()

# Check if the foreign key is set
if om.some_model_id is not None:
    # The foreign key object is set
    pass
