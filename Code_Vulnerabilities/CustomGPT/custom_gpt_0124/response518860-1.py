
class EditSpaceView(View):
    def post(self, request, *args, **kwargs):
        print('edit space view', request)
        print('request data:', request.POST)

        if request.POST:
            print('request.post')

            # Check if slug is in the URL kwargs
            slug = self.kwargs.get('slug')
            print('slug from URL:', slug)

            # Make sure to check if rental exists before proceeding
            try:
                rental = Rental.objects.get(slug=slug)
            except Rental.DoesNotExist:
                return HttpResponse(status=404)  # or handle as needed

            # Update the rental object
            rental.ownerName = request.POST.get('ownerName')
            # ... other fields ...
            rental.save()

            response = HttpResponse('')
            response['pk-user'] = rental.slug
            print('response slug', response)
            return response

        return HttpResponseRedirect('/')
