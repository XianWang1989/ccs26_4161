
class SomeModel(models.Model):
    pass

class OtherModel(models.Model):
    some_model = models.ForeignKey(SomeModel, null=True, blank=True, on_delete=models.SET_NULL)

# Usage
om = OtherModel()
# Instead of checking om.some_model directly, you can check if it is None
if om.some_model_id is not None:
    # Foreign key is set
    related_object = om.some_model
else:
    # Foreign key is not set
    pass
