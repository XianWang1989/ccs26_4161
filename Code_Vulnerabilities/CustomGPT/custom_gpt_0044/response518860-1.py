
class EditSpaceView(View):
    def post(self, request, *args, **kwargs):
        print('edit space view', request)
        if request.POST:
            print('request.post')  # Confirm POST request is received
            response = HttpResponse('')
            rental = Rental.objects.get(slug=self.kwargs['slug'])

            # Update rental fields
            rental.ownerName = request.POST.get('ownerName')
            # Add other fields...
            rental.save()

            response['pk-user'] = rental.slug  # Ensure this is correctly set
            return response

        return HttpResponseRedirect('/')
