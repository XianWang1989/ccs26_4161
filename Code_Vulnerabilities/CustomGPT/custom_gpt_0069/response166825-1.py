
class SomeModel(models.Model):
    pass

class OtherModel(models.Model):
    some_model = models.ForeignKey(SomeModel, on_delete=models.SET_NULL, null=True)

# Example usage
om = OtherModel.objects.select_related('some_model').first()  # or any other queryset

if om.some_model_id is not None:
    # some_model is set
    print("Foreign key is set.")
else:
    # some_model is not set
    print("Foreign key is not set.")
