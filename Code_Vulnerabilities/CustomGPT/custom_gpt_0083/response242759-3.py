
# views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import BusinessDetailsForm  # Your form for business details

@login_required
def additional_info(request):
    if request.method == 'POST':
        form = BusinessDetailsForm(request.POST)
        if form.is_valid():
            # Save business details logic
            return redirect('home')  # Redirect to home or another page
    else:
        form = BusinessDetailsForm()

    return render(request, 'yourapp/additional_info.html', {'form': form})
