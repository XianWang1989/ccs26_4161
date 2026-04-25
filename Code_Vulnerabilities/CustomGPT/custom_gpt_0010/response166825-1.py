
class SomeModel(models.Model):
    pass

class OtherModel(models.Model):
    some_model = models.ForeignKey(SomeModel, on_delete=models.CASCADE)

# Assuming you have an instance of OtherModel
om = OtherModel()

# Instead of checking with try...except, we can use the following:
if om.some_model_id is not None:
    # foreign key is set
    related_object = SomeModel.objects.filter(id=om.some_model_id).exists()
    if related_object:
        # You can safely access om.some_model
        pass
