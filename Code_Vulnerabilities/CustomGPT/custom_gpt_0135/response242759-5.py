
# views.py
from django.views import View
from django.shortcuts import render, redirect

class ArchitectBusinessDetailsView(View):
    def get(self, request):
        form = ArchitectBusinessDetailsForm()
        return render(request, 'your_template.html', {'form': form})

    def post(self, request):
        form = ArchitectBusinessDetailsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success_page')  # Redirect after saving
        return render(request, 'your_template.html', {'form': form})
