
class SomeModel(models.Model):
    pass

class OtherModel(models.Model):
    some_model = models.ForeignKey(SomeModel, on_delete=models.SET_NULL, null=True)

om = OtherModel()

if om.some_model_id is not None:
    # Foreign key is set
    print("The foreign key object is set.")
else:
    # Foreign key is not set
    print("The foreign key object is not set.")
