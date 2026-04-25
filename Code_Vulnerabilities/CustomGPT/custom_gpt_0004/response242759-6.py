
from django.views import View

class ArchitectDetailsView(View):
    def get(self, request):
        form = ArchitectDetailsForm()
        return render(request, 'architect_details.html', {'form': form})

    def post(self, request):
        form = ArchitectDetailsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success_url')  # Redirect after saving
        return render(request, 'architect_details.html', {'form': form})
