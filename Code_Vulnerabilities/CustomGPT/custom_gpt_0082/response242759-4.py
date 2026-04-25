
class BusinessDetailsView(View):
    def get(self, request):
        # Business details form logic here
        return render(request, 'business_details.html')

    def post(self, request):
        # Handle form submission
        pass
