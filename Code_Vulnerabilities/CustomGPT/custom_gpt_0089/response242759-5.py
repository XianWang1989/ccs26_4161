
# yourapp/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

@login_required
def business_details(request):
    if request.method == 'POST':
        # Process form data here
        return redirect('success_url')  # Redirect to a success page

    return render(request, 'yourapp/business_details.html')
