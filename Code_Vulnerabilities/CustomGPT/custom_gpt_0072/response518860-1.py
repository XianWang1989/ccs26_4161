
from django.http import JsonResponse

class EditSpaceView(View):
    def post(self, request, *args, **kwargs):
        print('edit space view', request)
        if request.POST:
            print('request.post')
            rental = Rental.objects.get(slug=self.kwargs['slug'])
            # Set attributes from request.POST
            for field in ['ownerName', 'email', 'phoneNumber', 'listingName', 
                          'summary', 'property', 'room', 'price', 
                          'city', 'place', 'water', 'amenities']:
                setattr(rental, field, request.POST.get(field))
            rental.save()
            return JsonResponse({'slug': rental.slug})

        return JsonResponse({'error': 'Invalid request'}, status=400)
