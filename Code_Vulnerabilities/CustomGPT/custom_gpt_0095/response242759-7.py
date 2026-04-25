
# myapp/views.py

from django.shortcuts import render

def architect_details_view(request):
    if request.method == 'POST':
        # Process form data here
        pass
    return render(request, 'myapp/architect_details.html')
