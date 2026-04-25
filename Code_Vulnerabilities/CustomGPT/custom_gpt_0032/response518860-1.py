
class EditSpaceView(View):
    def post(self, request, *args, **kwargs):
        print('edit space view', request)
        slug = self.kwargs['slug']
        rental = Rental.objects.filter(slug=slug).first()  # Safe way to get the rental

        if rental and request.POST:
            print('request.post')
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
            response['pk-user'] = rental.slug
            return response

        # Handle fallback
        return HttpResponseBadRequest("Invalid request")
