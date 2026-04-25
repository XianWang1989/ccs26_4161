
class EditSpaceView(View):
    def post(self, request, *args, **kwargs):
        print('edit space view', request)
        if request.POST:
            print('request.post')
            rental = Rental.objects.get(slug=self.kwargs['slug'])  # Adjusted for exception handling
            # Update the rental instance with new data
            rental.ownerName = request.POST.get('ownerName')
            # ... other fields ...
            rental.save()

            response = HttpResponse('')
            response['pk-user'] = rental.slug  # Ensure this is set correctly
            print('response slug', response['pk-user'])
            return response
        return HttpResponseRedirect('/')
