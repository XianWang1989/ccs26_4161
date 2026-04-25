
from django.http import JsonResponse

class EditSpaceView(View):
    def post(self, request, *args, **kwargs):
        print('edit space view', request)
        if request.POST:
            response_data = {}
            print('request.post')
            response_data['edited_owner_name'] = request.POST.get('ownerName')
            # ... (other fields)
            rental = Rental.objects.get(slug=self.kwargs['slug'])
            # Update rental fields as before...
            rental.save()
            response_data['slug'] = rental.slug  # This should not be null
            print('response slug', response_data)
            return JsonResponse(response_data)

        return JsonResponse({'error': 'Invalid POST request'}, status=400)
