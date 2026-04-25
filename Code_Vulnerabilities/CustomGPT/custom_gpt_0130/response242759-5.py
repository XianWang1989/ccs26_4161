
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

@login_required
def architect_details(request):
    if request.method == 'POST':
        # Handle form submission for business details
        pass
    return render(request, 'architect_details.html')
