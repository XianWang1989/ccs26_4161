
from django.views import View

class BusinessDetailsView(View):
    def get(self, request):
        form = BusinessDetailsForm()
        return render(request, 'business_details.html', {'form': form})

    def post(self, request):
        form = BusinessDetailsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success_page')  # Define success URL
        return render(request, 'business_details.html', {'form': form})
