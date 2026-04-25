
class SomeModel(models.Model):
    pass

class OtherModel(models.Model):
    some_model = models.ForeignKey(SomeModel, null=True, blank=True, on_delete=models.SET_NULL)

# Usage
om = OtherModel()

# Check if the foreign key is set using isinstance
if isinstance(om.some_model, SomeModel):
    # Foreign key is set
    pass
else:
    # Foreign key is not set
    pass
