
class EditSpaceView(View):
    def post(self, request, *args, **kwargs):
        print('edit space view', request)
        if request.POST:
            print('request.post')
            response = HttpResponse('')
            rental = Rental.objects.get(slug=self.kwargs['slug'])  # Fetch rental before modifying
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

            # Return the slug of the updated rental
            response['pk-user'] = rental.slug
            print('response slug', response['pk-user'])
            return response

        return HttpResponseRedirect('/')

