
class SomeModel(models.Model):
    pass

class OtherModel(models.Model):
    some_model = models.ForeignKey(SomeModel, on_delete=models.CASCADE, null=True, blank=True)

om = OtherModel()
if om.some_model_id is not None:
    # Foreign key is set
    pass
