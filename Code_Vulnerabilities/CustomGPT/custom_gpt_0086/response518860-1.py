
class EditSpaceView(View):
    def post(self, request, *args, **kwargs):
        print('edit space view', request)

        # Ensure `slug` is being retrieved correctly
        slug = self.kwargs.get('slug')
        if not slug:
            return HttpResponseBadRequest("Slug is missing.")

        rental = Rental.objects.filter(slug=slug).first()  # Get rental safely
        if not rental:
            return HttpResponseNotFound("Rental not found.")

        data = json.loads(request.body)  # Adjust to read JSON body
        print('request body', data)  # Debug data consumed

        if data:  # Only proceed if data is present
            rental.ownerName = data.get('ownerName')
            rental.email = data.get('email')
            rental.phoneNumber = data.get('phoneNumber')
            rental.listingName = data.get('listingName')
            rental.summary = data.get('summary')
            rental.property = data.get('property')
            rental.room = data.get('room')
            rental.price = data.get('price')
            rental.city = data.get('city')
            rental.place = data.get('place')
            rental.water = data.get('water')
            rental.amenities = data.get('amenities')
            rental.save()

            response = HttpResponse('')
            response['pk-user'] = rental.slug
            print('response slug', response['pk-user'])
            return response

        return HttpResponseBadRequest("Invalid data received.")
