
class EditSpaceView(View):
    def post(self, request, *args, **kwargs):
        print('edit space view', request)

        if request.method == 'POST':
            print('request.post')
            response = HttpResponse('')
            print('edited owner name is', request.POST.get('ownerName'))
            # Fetch the rental record based on slug
            try:
                rental = Rental.objects.get(slug=self.kwargs['slug'])
            except Rental.DoesNotExist:
                return JsonResponse({'error': 'Rental not found'}, status=404)

            # Update rental fields
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

            # Here we set the slug in the response header
            response['pk-user'] = rental.slug
            print('response slug', response)
            return response

        # In case of other methods, return a bad request response
        return JsonResponse({'error': 'Invalid request'}, status=400)
