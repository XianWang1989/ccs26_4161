
from django.http import JsonResponse

class EditSpaceView(View):
    def post(self, request, *args, **kwargs):
        print('edit space view', request)

        if request.POST:
            print('request.post')
            rental = Rental.objects.get(slug=self.kwargs['slug'])
            rental.ownerName = request.POST.get('ownerName')
            # Update other rental fields...
            rental.save()

            # Return JSON response with the slug
            return JsonResponse({'slug': rental.slug})  # Use JSON response to send slug back
        return JsonResponse({'error': 'Invalid request'}, status=400)
