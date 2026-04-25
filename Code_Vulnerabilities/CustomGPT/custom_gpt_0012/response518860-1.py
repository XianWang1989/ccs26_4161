
class EditSpaceView(View):
    def post(self, request, *args, **kwargs):
        print('edit space view', request)
        if request.body:  # Check for body data
            print('request.post')
            data = json.loads(request.body.decode('utf-8'))  # Decode JSON data
            response = HttpResponse('')  # Create a response object

            # Assume the data comes correctly formatted
            rental = Rental.objects.get(slug=self.kwargs['slug'])
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

            response['pk-user'] = rental.slug
            print('response slug', response)
            return response

        return HttpResponseRedirect('/')
