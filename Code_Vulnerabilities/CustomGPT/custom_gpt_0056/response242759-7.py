
# myapp/views.py

class BusinessDetailsView(View):
    def get(self, request):
        return render(request, 'business_details_form.html')

    def post(self, request):
        # handle form submission
        return redirect('home')
