
from django.http import JsonResponse  # Import for JsonResponse

class EditSpaceView(View):
    def post(self, request, *args, **kwargs):
        print('edit space view', request)
        if request.POST:
            print('request.post')
            rental = Rental.objects.get(slug=self.kwargs['slug'])
            # Update rental fields
            rental.ownerName = request.POST.get('ownerName')
            rental.email = request.POST.get('email')
            rental.phoneNumber = request.POST.get('phoneNumber')
            # ... other fields
            rental.save()
            response_data = {'slug': rental.slug}  # Package response data
            print('edited rental slug', rental.slug)
            return JsonResponse(response_data)  # Use JsonResponse for AJAX
        return JsonResponse({'error': 'Invalid form submission'}, status=400)
