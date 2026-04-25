
class SomeModel(models.Model):
    name = models.CharField(max_length=255)

class OtherModel(models.Model):
    some_model = models.ForeignKey(SomeModel, on_delete=models.SET_NULL, null=True)

    @property
    def is_some_model_set(self):
        return self.some_model is not None

# Example of usage
om = OtherModel()
if om.is_some_model_set:
    print("SomeModel is set")
else:
    print("SomeModel is not set")
