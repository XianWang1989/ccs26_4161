
# views.py
from django.views import View

class BusinessDetailsView(View):
    def get(self, request):
        form = BusinessDetailsForm()
        return render(request, 'yourapp/business_details.html', {'form': form})

    def post(self, request):
        form = BusinessDetailsForm(request.POST)
        if form.is_valid():
            form.save()  # Save the business details
            return redirect('success_page')  # Redirect after save
        return render(request, 'yourapp/business_details.html', {'form': form})
