
class SomeModel(models.Model):
    pass

class OtherModel(models.Model):
    some_model = models.ForeignKey(SomeModel, on_delete=models.SET_NULL, null=True)

om = OtherModel()

# Instead of directly accessing the foreign key, check if it exists
if om.some_model_id is not None:
    # Fetch the related object if necessary
    related_object = om.some_model
else:
    # Handle the case where the foreign key is not set
    print("Foreign key not set.")
