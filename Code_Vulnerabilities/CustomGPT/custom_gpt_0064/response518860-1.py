
from django.http import JsonResponse  # Import for JSON response
class EditSpaceView(View):
    def post(self, request, *args, **kwargs):
        print('edit space view', request)
        if request.POST:
            print('request.post')
            rental = Rental.objects.get(slug=self.kwargs['slug'])
            # Update rental properties here...
            rental.save()
            return JsonResponse({'slug': rental.slug})  # Return JSON response

        return JsonResponse({'error': 'No POST data'}, status=400)  # Handle error
