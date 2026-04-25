
from django.http import JsonResponse

class EditSpaceView(View):
    def post(self, request, *args, **kwargs):
        print('edit space view', request)
        if request.POST:
            print('request.post')
            rental = Rental.objects.get(slug=self.kwargs['slug'])
            rental.ownerName = request.POST.get('ownerName')
            rental.email = request.POST.get('email')
            # ... (update other fields) ...
            rental.save()
            return JsonResponse({'slug': rental.slug})  # Return slug in the response

        return JsonResponse({'error': 'Invalid request'}, status=400)
