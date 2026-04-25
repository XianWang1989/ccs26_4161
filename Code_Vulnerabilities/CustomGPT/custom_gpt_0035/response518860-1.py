
from django.http import JsonResponse  # Import JsonResponse

class EditSpaceView(View):
    def post(self, request, *args, **kwargs):
        print('edit space view', request)
        if request.POST:
            print('request.post')
            rental = Rental.objects.get(slug=self.kwargs['slug'])

            # Update rental attributes
            for field in ['ownerName', 'email', 'phoneNumber', 'listingName', 'summary', 
                          'property', 'room', 'price', 'city', 'place', 'water', 'amenities']:
                setattr(rental, field, request.POST.get(field))

            rental.save()
            # Return JSON response
            return JsonResponse({'slug': rental.slug})  # JSON response includes slug

        return JsonResponse({'error': 'Invalid request'})
