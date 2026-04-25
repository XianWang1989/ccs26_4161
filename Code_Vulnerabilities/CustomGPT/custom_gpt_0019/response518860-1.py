
from django.http import JsonResponse

class EditSpaceView(View):
    def post(self, request, *args, **kwargs):
        print('edit space view', request)
        if request.POST:
            print('request.post')
            rental = Rental.objects.get(slug=self.kwargs['slug'])
            rental.ownerName = request.POST.get('ownerName')
            # ... (other fields)
            rental.save()
            return JsonResponse({'slug': rental.slug})  # Send back the slug as JSON
        return JsonResponse({'error': 'Invalid Request'}, status=400)
