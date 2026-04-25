
from google.appengine.ext import ndb
from google.appengine.ext.ndb import Model
from django import forms

class UserModel(Model):
    email = ndb.StringProperty()

class UserForm(forms.ModelForm):
    class Meta:
        model = UserModel
        fields = ['email']

    # Override to add email validation
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email or not forms.EmailField().clean(email):
            raise forms.ValidationError("Enter a valid email address.")
        return email
