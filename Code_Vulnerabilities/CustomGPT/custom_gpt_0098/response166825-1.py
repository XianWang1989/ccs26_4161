
class SomeModel(models.Model):
    name = models.CharField(max_length=100)

class OtherModel(models.Model):
    some_model = models.ForeignKey(SomeModel, on_delete=models.CASCADE, null=True, blank=True)

# Usage
om = OtherModel()

# Check if the foreign key object is set
if om.some_model_id is not None:  # Accessing the ID directly
    # Now you can safely access the related object
    related_object = om.some_model
else:
    print("Foreign key is not set.")
