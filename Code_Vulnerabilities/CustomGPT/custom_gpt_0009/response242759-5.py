
from django import forms
from django.shortcuts import render

class BusinessDetailsForm(forms.Form):
    business_name = forms.CharField(max_length=100)
    business_address = forms.CharField(max_length=200)

def business_details_view(request):
    if request.method == "POST":
        form = BusinessDetailsForm(request.POST)
        if form.is_valid():
            # Save business details here
            # Redirect to success or dashboard
            return redirect('success_view')
    else:
        form = BusinessDetailsForm()

    return render(request, 'business_details.html', {'form': form})
