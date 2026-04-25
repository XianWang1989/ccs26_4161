
# views.py

from django.shortcuts import redirect
from django.views import View
from django import forms

class BusinessDetailsForm(forms.Form):
    business_name = forms.CharField(max_length=100)
    license_number = forms.CharField(max_length=50)

class UserTypeSignupView(View):
    def get(self, request):
        form = BusinessDetailsForm()
        return render(request, 'your_template.html', {'form': form})

    def post(self, request):
        form = BusinessDetailsForm(request.POST)
        if form.is_valid():
            # Save business details here
            # For example, attach them to the user or save in a profile model
            return redirect('success_url')  # Redirect to a success page
        return render(request, 'your_template.html', {'form': form})
