
class EditSpaceView(View):
    def post(self, request, *args, **kwargs):
        print('edit space view', request)
        if request.POST:
            print('request.post')
            slug = self.kwargs['slug']  # Ensure slug is fetched from kwargs
            try:
                rental = Rental.objects.get(slug=slug)
                rental.ownerName = request.POST.get('ownerName')
                rental.email = request.POST.get('email')
                rental.phoneNumber = request.POST.get('phoneNumber')
                rental.listingName = request.POST.get('listingName')
                rental.summary = request.POST.get('summary')
                rental.property = request.POST.get('property')
                rental.room = request.POST.get('room')
                rental.price = request.POST.get('price')
                rental.city = request.POST.get('city')
                rental.place = request.POST.get('place')
                rental.water = request.POST.get('water')
                rental.amenities = request.POST.get('amenities')
                rental.save()

                response = HttpResponse('')
                response['pk-user'] = rental.slug  # Return the slug in response
                print('response slug', response)
                return response
            except Rental.DoesNotExist:
                return HttpResponseBadRequest('Rental not found')

        return HttpResponseRedirect('/')
