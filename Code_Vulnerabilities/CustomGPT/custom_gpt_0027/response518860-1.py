
class EditSpaceView(View):
    def post(self, request, *args, **kwargs):
        print('edit space view', request)

        if request.POST:
            print('request.post')
            slug = self.kwargs['slug']  # Ensure we have the slug extracted

            # Try to get the rental object by slug
            try:
                rental = Rental.objects.get(slug=slug)
            except Rental.DoesNotExist:
                return JsonResponse({'error': 'Rental not found'}, status=404)

            # Update rental object
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

            response = JsonResponse({'pk-user': rental.slug})
            print('response slug', rental.slug)
            return response

        return JsonResponse({'error': 'Invalid request'}, status=400)

