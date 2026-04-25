
from django.http import JsonResponse

class EditSpaceView(View):
    def post(self, request, *args, **kwargs):
        if request.POST:
            rental = Rental.objects.get(slug=self.kwargs['slug'])
            # Update fields based on request.POST here...

            rental.save()

            data = {
                'slug': rental.slug,
                'message': 'Update successful'
            }
            return JsonResponse(data)  # Return a JSON response

        return JsonResponse({'error': 'Invalid request'}, status=400)
