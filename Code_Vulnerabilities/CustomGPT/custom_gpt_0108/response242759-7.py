
from django.views import View

class ArchitectDetailsView(View):
    def get(self, request):
        form = ArchitectDetailsForm()
        return render(request, 'architect_details.html', {'form': form})

    def post(self, request):
        form = ArchitectDetailsForm(request.POST)
        if form.is_valid():
            architect = form.save(commit=False)
            architect.user = request.user
            architect.save()
            return redirect('home')  # or wherever you need
        return render(request, 'architect_details.html', {'form': form})
