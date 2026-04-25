
from django.http import JsonResponse

class EditSpaceView(View):
    def post(self, request, *args, **kwargs):
        print('edit space view', request)
        if request.POST:
            print('request.post')
            response_data = {}
            rental = Rental.objects.get(slug=self.kwargs['slug'])
            # Update fields here...
            rental.save()
            response_data['slug'] = rental.slug  # Save the slug to response data
            return JsonResponse(response_data)  # Return JSON response

        return JsonResponse({'error': 'Invalid request'}, status=400)
