
import json
from django.http import JsonResponse

class EditSpaceView(View):
    def post(self, request, *args, **kwargs):
        print('edit space view', request)

        # Get the JSON data from the request body
        data = json.loads(request.body)
        print('Request Body Data:', data)

        rental_slug = self.kwargs['slug']
        try:
            rental = Rental.objects.get(slug=rental_slug)
            print('Edited Owner Name:', data.get('ownerName'))
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

            return JsonResponse({'pk-user': rental.slug})

        except Rental.DoesNotExist:
            return JsonResponse({'error': 'Rental not found'}, status=404)
