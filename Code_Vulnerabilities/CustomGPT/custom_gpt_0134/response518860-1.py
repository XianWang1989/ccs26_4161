
class EditSpaceView(View):
    def post(self, request, *args, **kwargs):
        print('edit space view', request)
        if request.POST:
            print('request.post')
            response = HttpResponse('')
            rental = Rental.objects.get(slug=self.kwargs['slug'])  # Ensure slug is retrieved
            # Set properties from request.POST
            for field in ['ownerName', 'email', 'phoneNumber', 'listingName', 'summary',
                          'property', 'room', 'price', 'city', 'place', 'water', 'amenities']:
                setattr(rental, field, request.POST.get(field))
            rental.save()
            response['pk-user'] = rental.slug
            print('response slug', response['pk-user'])
            return response

        return HttpResponseRedirect('/')
