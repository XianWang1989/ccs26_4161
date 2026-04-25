
class EditSpaceView(View):
    def post(self, request, *args, **kwargs):
        print('edit space view', request)
        if request.POST:
            print('request.post')

            # Fetch rental using the slug
            try:
                rental = Rental.objects.get(slug=self.kwargs['slug'])
            except Rental.DoesNotExist:
                return HttpResponseBadRequest('Rental not found')

            rental.ownerName = request.POST.get('ownerName')
            rental.email = request.POST.get('email')
            # ... other fields as needed
            rental.save()

            print('Edited rental slug:', rental.slug)
            response = HttpResponse('')
            response['pk-user'] = rental.slug  # Ensure the slug is set here
            return response
        return HttpResponseRedirect('/')
