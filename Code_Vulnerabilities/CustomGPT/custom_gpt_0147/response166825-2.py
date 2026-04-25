
class OtherModel(models.Model):
    some_model = models.ForeignKey(SomeModel, on_delete=models.SET_NULL, null=True)

    @property
    def is_some_model_set(self):
        return self.some_model_id is not None
