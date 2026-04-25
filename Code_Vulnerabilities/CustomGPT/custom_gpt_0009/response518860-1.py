
class EditSpaceView(View):
    def post(self, request, *args, **kwargs):
        print('edit space view', request)
        if request.POST:
            print('request.post')
            response = HttpResponse('')
            # Check if slug is in kwargs
            slug = self.kwargs.get('slug')  
            rental = Rental.objects.get(slug=slug)  # Improved this line
            # ... rest of your code remains unchanged
