
# views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

@login_required
def business_details(request):
    if request.method == 'POST':
        # Handle form submission
        # Save business details logic here
        return redirect('success_page')  # Redirect to success page or profile

    return render(request, 'business_details.html')
