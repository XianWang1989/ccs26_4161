
from django.http import JsonResponse
import json

class EditSpaceView(View):
    def post(self, request, *args, **kwargs):
        print('edit space view', request)

        if request.body:
            data = json.loads(request.body)
            print('request.data', data)  # Log received data
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

            return JsonResponse({'slug': rental.slug})

        return JsonResponse({'error': 'Invalid data'}, status=400)
