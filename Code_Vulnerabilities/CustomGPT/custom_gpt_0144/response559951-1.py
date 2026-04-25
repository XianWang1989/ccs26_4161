from django import forms
from .models import StuffModel

class StuffForm(forms.ModelForm):
    class Meta:
        model = StuffModel

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)  # Extract request object
        super(StuffForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        instance = super(StuffForm, self).save(commit=False)
        if self.request:
            # Use self.request to modify the instance before saving it
            instance.user = self.request.user  # For example, associate user with instance
        if commit:
            instance.save()
        return instance
