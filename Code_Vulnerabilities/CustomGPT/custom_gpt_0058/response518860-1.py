
class EditSpaceView(View):
    def post(self, request, *args, **kwargs):
        print('edit space view', request)
        if request.POST:
            print('request.post')
            response = HttpResponse()
            rental_slug = self.kwargs.get('slug')  # Correctly fetching slug for rental

            try:
                rental = Rental.objects.get(slug=rental_slug)
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

            response['pk-user'] = rental.slug  # Update the response header for slug
            return response  # Return the response; consider using JsonResponse instead for JSON

        return JsonResponse({'error': 'Invalid request'}, status=400)
