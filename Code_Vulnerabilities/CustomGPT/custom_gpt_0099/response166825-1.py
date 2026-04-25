
class SomeModel(models.Model):
    pass

class OtherModel(models.Model):
    some_model = models.ForeignKey(SomeModel, on_delete=models.CASCADE)

# Example usage
om = OtherModel.objects.select_related('some_model').get(id=1)  # Use actual ID

if om.some_model_id is not None:
    # some_model is set, do something with it
    print("Foreign key is set.")
else:
    print("Foreign key is not set.")
