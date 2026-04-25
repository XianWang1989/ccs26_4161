
# views.py
from django.views import View
from django.shortcuts import render

class ArchitectDetailsView(View):
    def get(self, request):
        form = ArchitectDetailsForm()
        return render(request, 'architect_details.html', {'form': form})

    def post(self, request):
        form = ArchitectDetailsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('profile')  # Redirect after saving
        return render(request, 'architect_details.html', {'form': form})
