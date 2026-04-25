
# forms.py
class BusinessDetailsForm(forms.ModelForm):
    class Meta:
        model = BusinessDetails  # Assume you have this model
        fields = ['company_name', 'address', 'phone']

# views.py
class BusinessDetailsView(View):
    def get(self, request):
        form = BusinessDetailsForm()
        return render(request, 'business_details.html', {'form': form})

    def post(self, request):
        form = BusinessDetailsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success_url')  # Where to redirect after save
        return render(request, 'business_details.html', {'form': form})
