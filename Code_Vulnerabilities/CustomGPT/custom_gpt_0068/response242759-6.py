
# views.py
from django.shortcuts import render, redirect
from .forms import BusinessDetailsForm
from django.contrib.auth.decorators import login_required

@login_required
def business_details(request):
    if request.method == 'POST':
        form = BusinessDetailsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success_url')  # Redirect to a success page or the next step
    else:
        form = BusinessDetailsForm()
    return render(request, 'business_details.html', {'form': form})
