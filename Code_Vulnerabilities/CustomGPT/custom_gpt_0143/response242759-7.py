
# views.py
from django.views import View

class YourBusinessDetailsView(View):
    def get(self, request):
        form = BusinessDetailsForm()
        return render(request, 'business_details.html', {'form': form})

    def post(self, request):
        form = BusinessDetailsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success_url')  # Redirect after saving
        return render(request, 'business_details.html', {'form': form})
