
from django.http import JsonResponse

class EditSpaceView(View):
    def post(self, request, *args, **kwargs):
        print('edit space view', request)
        if request.POST:
            print('request.post')
            rental = Rental.objects.get(slug=self.kwargs['slug'])
            rental.ownerName = request.POST.get('ownerName')
            # (Other fields updates here)
            rental.save()
            return JsonResponse({'slug': rental.slug}, status=200)  # Return slug as JSON response
        return JsonResponse({'error': 'Invalid request'}, status=400)
