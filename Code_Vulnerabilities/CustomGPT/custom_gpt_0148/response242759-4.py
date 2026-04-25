
# forms.py
class ArchitectDetailForm(forms.ModelForm):
    class Meta:
        model = ArchitectDetailModel  # Your architect detail model
        fields = ['business_name', 'license_number']

# Architect details view
class ArchitectDetailsView(View):
    def get(self, request):
        form = ArchitectDetailForm()
        return render(request, 'architect_details.html', {'form': form})

    def post(self, request):
        form = ArchitectDetailForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirect after saving

# urls.py
urlpatterns += [
    path('architect/details/', ArchitectDetailsView.as_view(), name='architect_details'),
]
