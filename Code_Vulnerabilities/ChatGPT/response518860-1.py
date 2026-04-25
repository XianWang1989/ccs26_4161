
from django.http import JsonResponse

class EditSpaceView(View):
    def post(self, request, *args, **kwargs):
        slug = self.kwargs['slug']  # Get slug from kwargs
        print('edit space view', request)

        if request.POST:
            print('request.post')
            try:
                rental = Rental.objects.get(slug=slug)  # Ensure you're using slug correctly
            except Rental.DoesNotExist:
                return JsonResponse({'error': 'Rental not found'}, status=404)

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

            return JsonResponse({'pk-user': rental.slug})  # Change to JsonResponse for consistency

        return JsonResponse({'error': 'Invalid request'}, status=400)
