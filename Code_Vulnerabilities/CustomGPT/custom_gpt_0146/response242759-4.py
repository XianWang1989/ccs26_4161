
# forms.py
class BusinessDetailsForm(forms.ModelForm):
    class Meta:
        model = Business  # Assume you have a Business model
        fields = ['business_name', 'business_address', 'website']

# views.py
from django.shortcuts import render

def architect_business_details(request):
    if request.method == 'POST':
        form = BusinessDetailsForm(request.POST)
        if form.is_valid():
            business = form.save(commit=False)
            business.user = request.user
            business.save()
            return redirect('success_url')
    else:
        form = BusinessDetailsForm()
    return render(request, 'business_details.html', {'form': form})
