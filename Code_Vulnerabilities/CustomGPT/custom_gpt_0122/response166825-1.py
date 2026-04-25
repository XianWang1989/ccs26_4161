
class SomeModel(models.Model):
    pass

class OtherModel(models.Model):
    some_model = models.ForeignKey(SomeModel, on_delete=models.CASCADE, null=True, blank=True)

# Example usage
om = OtherModel()

# Checking if the ForeignKey is set
if om.some_model_id is not None:
    # Foreign key is set
    related_object = om.some_model  # Access the related object safely
else:
    # Foreign key is not set
    pass
