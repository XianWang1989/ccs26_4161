
# views.py
from django.shortcuts import render, redirect

@login_required
def architect_details(request):
    if request.method == "POST":
        # Handle form submission
        pass
    return render(request, 'architect_details.html')
