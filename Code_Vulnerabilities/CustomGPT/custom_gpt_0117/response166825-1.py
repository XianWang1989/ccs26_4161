
class SomeModel(models.Model):
    name = models.CharField(max_length=100)

class OtherModel(models.Model):
    some_model = models.ForeignKey(SomeModel, on_delete=models.CASCADE, null=True, blank=True)

# Create an instance of OtherModel
om = OtherModel()

# Check if the foreign key is set
if om.some_model_id is not None:  # Check foreign key field directly
    # Safe to access the related object
    related_object = om.some_model
    print(related_object.name)
else:
    print("Foreign key is not set.")
