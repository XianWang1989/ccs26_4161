
# forms.py
class BusinessDetailsForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['business_name', 'business_address', 'phone_number']

# views.py
from django.contrib.auth.decorators import login_required

@login_required
def business_details(request):
    if request.method == 'POST':
        form = BusinessDetailsForm(request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect('home')  # or wherever you want to redirect
    else:
        form = BusinessDetailsForm()
    return render(request, 'your_template.html', {'form': form})
