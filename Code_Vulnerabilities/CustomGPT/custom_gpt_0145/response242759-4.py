
# views.py
from django.views import View
from django.shortcuts import render, redirect

class BusinessDetailsView(View):
    def get(self, request):
        return render(request, 'business_details.html')

    def post(self, request):
        # Handle the form for business details
        # Process and save the business details
        return redirect('/success/')  # Or any success page
