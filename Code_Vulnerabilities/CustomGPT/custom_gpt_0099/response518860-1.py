
class EditSpaceView(View):
    def post(self, request, *args, **kwargs):
        print ('edit space view', request)

        if request.POST:
            print('request.post')
            response = HttpResponse()
            # Ensure rental object is retrieved
            try:
                rental = Rental.objects.get(slug=self.kwargs['slug'])
            except Rental.DoesNotExist:
                return HttpResponse(status=404)  # Not found

            # Update rental information
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

            response['pk-user'] = rental.slug
            print('response slug', response['pk-user'])
            return response

        return HttpResponseRedirect('/')
