
from google.appengine.ext import ndb
from django import forms

class User(ndb.Model):
    email = ndb.StringProperty()

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not forms.fields.EmailField().clean(email):
            raise forms.ValidationError("Enter a valid email address.")
        return email

# Usage
form = UserForm({'email': 'test@example.com'})
if form.is_valid():
    user = form.save()
else:
    print(form.errors)
